import pytest
import base64
import pytest_html
import shutil
import os

from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pathlib import Path

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")
        
        # Di environment CI (GitHub Actions), gunakan headless=True otomatis
        is_ci = os.getenv("CI", "false").lower() in ("true", "1")
        is_headless = True if is_ci else os.getenv("HEADLESS", "false").lower() in ("true", "1")
        
        browser = p.chromium.launch(headless=is_headless)

        context = browser.new_context()
        page = context.new_page()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        yield page

        try:
            report = getattr(request.node, "rep_call", None)
            trace_name = request.node.name.replace("[", "_").replace("]", "")
            trace_dir = Path("traces")
            trace_file = trace_dir / f"{trace_name}.zip"

            if report and report.failed:
                trace_dir.mkdir(exist_ok=True)
                context.tracing.stop(path=str(trace_file))
            else:
                # Jika test berhasil, buang rekaman dan hapus trace lama (jika ada)
                if trace_file.exists():
                    trace_file.unlink()
                context.tracing.stop()

        finally:
            context.close()
            browser.close()

@pytest.fixture
def logged_in_user(page):
    # Login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

    yield page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is None:
            for arg in item.funcargs.values():
                if hasattr(arg, "screenshot"):
                    page = arg
                    break
        if page is not None:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screenshot_path = screenshot_dir / f"{item.name}.png"

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            image_bytes = screenshot_path.read_bytes()

            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.image(
                    image_base64,
                    mime_type="image/png"
                )
            )
            report.extras = extras

def pytest_sessionstart(session):
    """Dijalankan sekali sebelum semua test dimulai untuk membersihkan folder lama."""
    for folder_name in ["traces", "screenshots"]:
        folder = Path(folder_name)
        if folder.exists():
            shutil.rmtree(folder)
        folder.mkdir(exist_ok=True)
    

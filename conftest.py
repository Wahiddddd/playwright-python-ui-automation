import pytest
import base64
import pytest_html

from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pathlib import Path

@pytest.fixture
def page():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

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
    

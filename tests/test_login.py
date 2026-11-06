import pytest
from pages.login_page import LoginPage

from playwright.sync_api import expect

@pytest.mark.parametrize("username, password, expected", [
    pytest.param("standard_user", "secret_sauce", "success", id="tc01"),
    pytest.param("standard_user", "salah123", "failed,", id="tc02"),
    pytest.param("salah_user", "secret_sauce", "failed", id="tc03"),
])
def test_login_success(page, username, password, expected):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    if expected == "success":
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
        expect(page.get_by_text("Products", exact=True)).to_be_visible()

    else:
        expect(page).to_have_url(
            "https://www.saucedemo.com/"
        )

        expect(
            page.get_by_test_id("error")
        ).to_be_visible()
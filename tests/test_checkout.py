import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from playwright.sync_api import expect

@pytest.mark.parametrize("first_name, last_name, postal_code, expected", [
    pytest.param("andy", "ferdian", "1234", "success", id="TC01"),
    pytest.param("", "ferdian", "1234", "failed", id="TC02"),
    pytest.param("andy", "", "1234", "failed", id="TC03"),
    pytest.param("andy", "ferdian", "", "failed", id="TC04"),
])
def test_checkout(logged_in_user, first_name, last_name, postal_code, expected):
    page = logged_in_user

    # Inventory
    inventory_page = InventoryPage(page)
    inventory_page.is_page_open()

    # Add to Cart
    inventory_page.click_add_backpack_button()

    inventory_page.open_cart()

    # cart page
    cart_page = CartPage(page)
    cart_page.is_page_open()
    cart_page.is_backpack_visible()

    cart_page.click_checkout()

    # checkout page
    checkout_page = CheckoutPage(page)
    checkout_page.is_page_open()
    checkout_page.fill_field(first_name, last_name, postal_code)
    if expected == "success":
        expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
        expect(page.get_by_text("Checkout: Overview", exact=True)).to_be_visible()
    else:
        expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
        expect(
            page.get_by_test_id("error")
        ).to_be_visible()

        error = checkout_page.get_error_message()
        if first_name == "":
            assert error == "Error: First Name is required" 
        elif last_name == "":
            assert error == "Error: Last Name is required"
        else:
            assert error == "Error: Postal Code is required"

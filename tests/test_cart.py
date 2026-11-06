from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_cart(logged_in_user):
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
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(page.get_by_text("Checkout: Your Information", exact=True)).to_be_visible()

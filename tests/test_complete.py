from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.complete_page import CompletePage

from playwright.sync_api import expect

def test_complete(logged_in_user):
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
    checkout_page.fill_field("andy", "ferdian", "12")

    # checkout_oerview_page
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.open_checkout_overview()
    checkout_overview_page.click_finish()

    # complete page
    complete_page = CompletePage(page)
    complete_page.is_page_open()
    complete_page.is_order_successful()

    complete_page.click_back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

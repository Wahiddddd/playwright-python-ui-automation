from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_inventory(logged_in_user):
    page = logged_in_user

    # Inventory
    inventory_page = InventoryPage(page)
    inventory_page.is_page_open()

    # Add to Cart
    inventory_page.click_add_backpack_button()

    # Verifikasi jumlah item di cart
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    inventory_page.open_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()




from playwright.sync_api import expect

class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.products = page.get_by_text("Products", exact=True)

        self.backpack = self.page.locator(
            ".inventory_item"
        ).filter(has_text="Sauce Labs Backpack")

        self.add_backpack_button = self.backpack.get_by_role(
            "button", name="Add to cart"
        )

        self.shopping_cart = page.locator(".shopping_cart_link")

    def open_cart(self):
        self.shopping_cart.click()

        
    def is_page_open(self):
        expect(self.products).to_be_visible()

    def click_add_backpack_button(self):
        self.add_backpack_button.click()

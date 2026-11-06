from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

        # judul
        self.title = page.get_by_text("Your Cart", exact=True)

        # periksa isi cart ada sauce labs backpack
        self.backpack = page.get_by_text("Sauce Labs Backpack", exact=True)

        # periksa tombol remove
        self.remove = page.get_by_role("button", name="Remove")
        self.checkout = page.get_by_role("button", name="Checkout")
        self.continue_shopping= page.get_by_role("button", name="Continue Shopping")

    def is_page_open(self):
        expect(self.title).to_be_visible()

    def is_backpack_visible(self):
        expect(self.backpack).to_be_visible()

    def click_checkout(self):
        self.checkout.click()
from playwright.sync_api import expect

class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_text("Checkout: Overview")
        self.product = self.page.locator(".cart_item").filter(has_text="Sauce Labs Backpack")
        self.price = self.product.locator(".inventory_item_price")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.cancel_button = page.get_by_role("button", name="Cancel")

    def open_checkout_overview(self):
        expect(self.heading).to_be_visible()

    def click_finish(self):
        self.finish_button.click()

    def click_cancel(self):
        self.cancel_button.click()

    def get_price(self):
        return self.price.inner_text()

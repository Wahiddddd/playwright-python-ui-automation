from playwright.sync_api import expect

class CompletePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_text("Checkout: Complete!", exact=True)
        self.message = self.page.get_by_test_id("complete-header")
        self.back_button = page.get_by_role("button", name="Back Home")

    def is_page_open(self):
        expect(self.heading).to_be_visible()

    def is_order_successful(self):
        expect(self.message).to_be_visible()

    def click_back_home(self):
        self.back_button.click()
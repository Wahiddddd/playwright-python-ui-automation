from playwright.sync_api import expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.title = page.get_by_text("Checkout: Your Information", exact=True)

        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")

        self.continue_button = page.get_by_role("button", name="Continue")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.error_message = page.get_by_test_id("error")

    def is_page_open(self):
        expect(self.title).to_be_visible()

    def fill_field(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    def continue_checkout(self):
        self.continue_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()
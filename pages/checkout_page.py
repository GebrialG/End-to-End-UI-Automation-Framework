from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.success_header = page.locator(".complete-header")

    def fill_info(self, first, last, zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()
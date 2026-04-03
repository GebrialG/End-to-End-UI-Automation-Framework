from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def proceed_to_checkout(self):
        self.checkout_button.click()
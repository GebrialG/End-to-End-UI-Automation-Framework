from playwright.sync_api import Page, expect
import re

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_text("Products")
        self.cart_link = page.locator(".shopping_cart_link")

    def is_loaded(self):
        expect(self.page).to_have_url(re.compile(".*inventory.html"))
        expect(self.heading).to_be_visible()

    def add_item_to_cart(self, item_name: str):
        self.page.locator(f"//div[text()='{item_name}']/../../..//button").click()

    def go_to_cart(self):
        self.cart_link.click()
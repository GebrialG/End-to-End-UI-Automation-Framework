from playwright.sync_api import Page, expect
import re

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_text("Products")

    def is_loaded(self):
        expect(self.page).to_have_url(re.compile(".*inventory.html"))
        expect(self.heading).to_be_visible()
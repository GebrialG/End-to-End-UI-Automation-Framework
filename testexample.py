import re

from playwright.sync_api import Page, expect


def test_saucedemo_loads(page: Page):

    page.goto("https://www.saucedemo.com")

    expect(page).to_have_title(re.compile("Swag Labs"))


def test_login_form_is_visible(page: Page):

    page.goto("https://www.saucedemo.com")

    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
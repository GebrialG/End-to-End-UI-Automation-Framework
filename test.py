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

def test_valid_login(page: Page):

    page.goto("https://www.saucedemo.com")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()

def test_invalid_login_shows_error(page: Page):

    page.goto("https://www.saucedemo.com")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text(
        "Username and password do not match any user in this service"
    )).to_be_visible()
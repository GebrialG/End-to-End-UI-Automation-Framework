from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import re

def test_saucedemo_loads(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_login_form_is_visible(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    products_page.is_loaded()

def test_invalid_login_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login("standard_user", "wrong_password")
    
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )
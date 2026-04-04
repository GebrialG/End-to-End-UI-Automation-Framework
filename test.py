from playwright.sync_api import expect
import re

def test_saucedemo_loads(login_page):
    login_page.navigate()
    expect(login_page.page).to_have_title(re.compile("Wrong Title"))

def test_login_form_is_visible(login_page):
    login_page.navigate()
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()

def test_invalid_login_shows_error(login_page):
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()

# --- AUTHENTICATED FLOWS (Using the new fixture) ---

def test_valid_login(authenticated_page):
    authenticated_page.is_loaded()

def test_add_product_to_cart(authenticated_page):
    authenticated_page.add_item_to_cart("Sauce Labs Backpack")
    expect(authenticated_page.cart_link).to_have_text("1")

def test_remove_product_from_cart(authenticated_page):
    authenticated_page.add_item_to_cart("Sauce Labs Backpack")
    authenticated_page.page.get_by_role("button", name="Remove").click()
    expect(authenticated_page.cart_link).to_have_text("")

def test_navigate_to_cart(authenticated_page, cart_page):
    authenticated_page.go_to_cart()
    expect(cart_page.checkout_button).to_be_visible()

def test_full_checkout_flow(authenticated_page, cart_page, checkout_page):
    # End-to-end journey
    authenticated_page.add_item_to_cart("Sauce Labs Onesie")
    authenticated_page.go_to_cart()
    
    cart_page.proceed_to_checkout()
    
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.finish_checkout()
    
    expect(checkout_page.success_header).to_contain_text("Thank you for your order!")
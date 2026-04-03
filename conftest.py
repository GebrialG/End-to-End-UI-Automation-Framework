import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def authenticated_page(page, login_page, products_page):
    """Logs in and returns a ready-to-use ProductsPage object."""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    products_page.is_loaded()
    return products_page

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
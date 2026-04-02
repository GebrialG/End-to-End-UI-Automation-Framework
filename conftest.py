import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture
def login_page(page):
    """
    This fixture creates the LoginPage object. 
    'page' is a built-in Playwright fixture that manages the browser setup/teardown.
    """
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    """Creates the ProductsPage object so tests can use it immediately."""
    return ProductsPage(page)
import pytest
import base64
from datetime import datetime
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_bytes = page.screenshot()
            encoded = base64.b64encode(screenshot_bytes).decode("utf-8")

            # pytest-html 4.x uses report.extras (plural) and a dict format
            from pytest_html import extras
            rep.extras = getattr(rep, "extras", [])
            rep.extras.append(
                extras.image(f"data:image/png;base64,{encoded}")
            )
# End-to-End UI Automation Framework

A Python-based UI test automation framework built with pytest and Playwright,
targeting the [Sauce Demo](https://www.saucedemo.com) e-commerce application.

>This project is being built incrementally as part of my structured SDET learning path which includes much use of the Playwright and pytest documentation at playwright.dev/python/docs/intro & docs.pytest.org/en/stable/getting-started.html. Current status and planned work are listed below.

---

## Project Goals

- Build a maintainable E2E test suite using the Page Object Model pattern
- Demonstrate professional pytest fixture and conftest structure
- Integrate with GitHub Actions CI for automated test runs on every push
- Generate HTML reports with automatic screenshot capture on failure

---

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.14.3 | Language |
| pytest | 9.0.2 | Test framework |
| Playwright | 1.56.0 | Browser automation |
| pytest-playwright | 0.7.2 | Playwright fixture integration for pytest |
| pytest-html | 4.2.0 | HTML report generation |
| pytest-base-url | 2.1.0 | Base URL configuration |
| pytest-metadata | 3.1.1 | Environment metadata in reports |

---

## Virtual Environment

This project uses a Python virtual environment to isolate its dependencies
from your system Python and any other projects on your machine.

**Why this matters:**
- Prevents version conflicts between projects (e.g. two projects needing
  different versions of pytest)

- Ensures `requirements.txt` only captures what this project actually needs

- Means the project behaves consistently on any machine that follows
  the setup steps

**The `venv/` folder is intentionally excluded from version control** via
`.gitignore`. Anyone cloning this repo creates their own local environment by following the setup instructions above.

To confirm the environment is active, your terminal prompt should show
`(venv)` at the start. To deactivate it at any time:

```bash
deactivate
```

To reactivate in a future session, navigate back to the project folder and run:

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

## Current Status

- [x] Virtual environment configured
- [x] Dependencies installed and pinned in `requirements.txt`
- [x] Playwright browsers installed
- [x] Sauce Demo loads correctly and login form elements confirmed visible
- [x] Login flow tests — valid credentials, invalid credentials, error states
- [x] Page Object Model structure — `LoginPage`, `ProductsPage`, `CartPage`, `CheckoutPage`
- [x] Product browsing tests — add to cart, remove from cart
- [x] Cart and checkout tests — full end-to-end checkout flow
- [x] Failure screenshot capture — embedded in HTML report via `conftest.py` hook
- [x] HTML report generation — `pytest-html` with base64-encoded screenshots on failure
- [ ] GitHub Actions CI workflow

---

## Setup

**Prerequisites:** Python 3.8 or higher

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries (required separately — not in pip)
playwright install
```

---

## Running Tests

```bash
# Run all tests (headless by default)
pytest test_saucedemo.py

# Run with visible browser window
pytest test_saucedemo.py --headed

# Run with HTML report
pytest test_saucedemo.py --html=report.html

# Run a specific test by name
pytest test_saucedemo.py -k "test_valid_login"
```

---

## Test Coverage

| Test | Description |
|---|---|
| `test_saucedemo_loads` | Confirms site loads with correct page title |
| `test_login_form_is_visible` | Confirms all login form elements are present |
| `test_invalid_login_shows_error` | Verifies error message on wrong credentials |
| `test_valid_login` | Successful login navigates to products page |
| `test_add_product_to_cart` | Adding an item updates the cart counter |
| `test_remove_product_from_cart` | Removing an item clears the cart counter |
| `test_navigate_to_cart` | Cart page loads with checkout button visible |
| `test_full_checkout_flow` | End-to-end: login → add item → cart → checkout → confirmation |

---

## Project Structure

```
.
├── pages/
│   ├── login_page.py       # Login page — navigate, fill credentials, read errors
│   ├── products_page.py    # Products page — verify loaded, add to cart, go to cart
│   ├── cart_page.py        # Cart page — proceed to checkout
│   └── checkout_page.py    # Checkout page — fill info, finish, confirm success
├── conftest.py             # Shared fixtures and screenshot-on-failure hook
├── test_saucedemo.py       # All test functions
├── requirements.txt        # Pinned dependencies
└── README.md
```

---

## Screenshot on Failure

Test failures automatically capture and embed a screenshot inside the HTML report.
This is implemented via a `pytest_runtest_makereport` hook in `conftest.py` —
no additional configuration is needed.

To see it in action, run with `--html=report.html` and open the report in a browser.
Failed tests will show an embedded screenshot beneath the failure log.

---

## Target Application

Tests run against [Sauce Demo](https://www.saucedemo.com), a purpose-built
demo e-commerce site designed for automation practice.

Test credentials: `standard_user` / `secret_sauce`

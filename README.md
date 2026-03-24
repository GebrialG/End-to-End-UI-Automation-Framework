# End-to-End UI Automation Framework

This is a Python-based UI test automation framework built with pytest and Playwright,
targeting the [Sauce Demo](https://www.saucedemo.com) e-commerce application.

> 🚧 **Work in progress** — this project is being built incrementally as part of my structured SDET learning path which includes much use of the Playwright and pytest documentation at playwright.dev/python/docs/intro & docs.pytest.org/en/stable/getting-started.html. Current status and planned work are listed below.

---

## Project Goals

- Build a maintainable E2E test suite using the Page Object Model pattern
- Demonstrate professional pytest fixture and conftest structure
- Integrate with GitHub Actions CI for automated test runs on every push
- Generate HTML reports with automatic screenshot capture on failure

---

## Tech Stack

| Tool | Purpose |

| Python 3.x | Language |

| pytest | Test framework |

| Playwright | Browser automation |

| pytest-playwright | Playwright fixture integration for pytest |

| pytest-html | HTML report generation |

---

## Virtual Environment

As part of this project uses a Python virtual environment to isolate its dependencies
from your system Python and any other projects on your machine.

**Why this matters:**
- Prevents version conflicts between projects (e.g. two projects needing
  different versions of pytest)
- Ensures `requirements.txt` only captures what this project actually needs
- Means the project behaves consistently on any machine that follows
  the setup steps

**The `venv/` folder is intentionally excluded from version control** via
`.gitignore`. Anyone cloning this repo creates their own local environment
by following the setup instructions above.

To confirm the environment is active, your terminal prompt should show
`(venv)` at the start. To deactivate it at any time:
```bash
deactivate
```

To reactivate in a future session, navigate back to the project folder and run:
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## Current Status

- [x] Virtual environment configured
- [x] Dependencies installed (`pytest`, `playwright`, `pytest-playwright`)
- [x] Playwright browsers installed
- [x] Example test confirmed working
- [ ] Page Object Model structure
- [ ] Login flow tests
- [ ] Product browsing tests
- [ ] Cart and checkout tests
- [ ] Failure screenshot capture
- [ ] HTML report generation
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

# Install Playwright browser binaries
playwright install
```

---

## Running Tests

```bash
# Run all tests (headless)
pytest

# Run with visible browser window
pytest --headed

# Run a specific file
pytest tests/test_login.py

# Run with HTML report
pytest --html=report.html
```

---

## Project Structure

.
├── pages/              # Page Object classes (one per page)
├── tests/              # Test files
├── conftest.py         # Shared pytest fixtures
├── requirements.txt    # Pinned dependencies
└── README.md

> Note: this structure is the intended final structure so it is currently being built out so some directories above do not exist yet.

---

## Target Application

Tests run against [Sauce Demo](https://www.saucedemo.com), a purpose-built
demo e-commerce site designed for automation practice.

Test credentials used: `standard_user` / `secret_sauce`
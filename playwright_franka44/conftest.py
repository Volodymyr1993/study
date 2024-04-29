import pytest
from playwright_franka44.components.pages import LoginPage, CalendarPage
from playwright.sync_api import Browser, Page, Playwright
from typing import Generator
from urllib.parse import urljoin


URL = "https://demarapart.otelms.com/login_c2/"
PAGE_TIMEOUT = 15 * 1000

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict,
                             request):
    """ Update browser parameters """
    return {
        **browser_type_launch_args,
        'slow_mo': 500,
        'timeout': 60 * 1000,  # 60 sec
        # 'devtools': True,
    }


@pytest.fixture(scope="session")
def saved_login(playwright: Playwright):
    chromiun = playwright.chromium
    browser = chromiun.launch(headless=False)
    page = browser.new_page()
    # go to login page
    login_page = LoginPage(page, url=URL)
    login_page.goto()
    login_page.login_do()
    yield
    page.close()


@pytest.fixture
def calendar(saved_login, page: Page) -> Generator[CalendarPage, None, None]:
    page.set_default_timeout(PAGE_TIMEOUT)

    calendar_page = CalendarPage(page, url=urljoin(URL, url='calendar'))
    calendar_page.goto()

    yield calendar_page
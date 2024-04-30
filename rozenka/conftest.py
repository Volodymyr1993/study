import pytest
from playwright.sync_api import Page, Browser
from rozenka.components.pages import PythonPage
from urllib.parse import urljoin
from typing import Generator
from pathlib import Path
import pickle


BASE_URL = "https://playwright.dev"
PYTHON_PAGE = "python"
PAGE_TIMEOUT = 15 * 1000


@pytest.fixture(scope='session')
def project_dir():
    """
    Returns pathlib.Path instance of project data directory
    """
    return Path(__file__).parent.absolute()


@pytest.fixture(scope="session")
def saved_login(project_dir,
                browser: Browser):
    cookies_file = project_dir / 'cookies.pkl'
    if cookies_file.exists():
        return pickle.load(cookies_file.open('rb'))
    br_context = browser.new_context()
    page = br_context.new_page()
    page.goto(BASE_URL)
    storage_state = {'cookies': br_context.cookies()}

    with cookies_file.open('wb') as f:
        pickle.dump(storage_state, f)
    br_context.close()
    return storage_state


@pytest.fixture
def use_login_state(browser_context_args: dict, saved_login: dict) -> dict:
    """ Use previously saved login state.

    Update `browser_context_args` with storage state that will be used in context
    creation.

    NOTE: to apply `browser_context_args` on the context `use_login_state` fixture should
    be specified before `page` fixture!
    """
    browser_context_args['storage_state'] = saved_login
    yield
    del browser_context_args['storage_state']


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict):
    """ Update browser parameters """
    return {
        **browser_type_launch_args,
        'headless': False,
        'slow_mo': 500,
        'timeout': 60 * 1000,  # 60 sec
        'devtools': False,
    }


@pytest.fixture
def python_page(use_login_state: dict,
                page: Page) -> Generator[PythonPage, None, None]:

    python_page = PythonPage(page, url=urljoin(BASE_URL, PYTHON_PAGE))
    python_page.goto()
    yield python_page
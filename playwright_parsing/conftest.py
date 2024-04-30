import pytest
from main import PageElement, CalendarPage
from playwright.sync_api import Playwright, sync_playwright, expect, Page


@pytest.fixture
def calendar(page: Page):
    calendar = CalendarPage(page)
    yield page

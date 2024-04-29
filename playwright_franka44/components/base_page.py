from playwright.sync_api import Page
import logging
from playwright_franka44.components.elements import PageElement


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.log = logging.getLogger(self.__class__.__name__)

    def __getattr__(self, attr):
        if hasattr(self.page, attr):
            return getattr(self.page, attr)

    def goto(self, url=None, **kwargs):
        self.log.info(f"Navigating to page: {url or self.url}")
        timeout = kwargs.pop('timeout', 30) * 1000
        self.page.goto(self.url if url is None else url, timeout=timeout, **kwargs)

    @property
    def page_url(self):
        return self.page.url

    def _set_element(self, element_type: PageElement, locator: str):
        return element_type(self.page, locator)



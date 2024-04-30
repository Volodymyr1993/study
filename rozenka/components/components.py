from rozenka.components.base_page import BasePage
from playwright.sync_api import Page
from rozenka.components.elements import PageElement
from playwright._impl import _errors
from playwright.sync_api import Page, expect

class PythonMixin:
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        self.language_selector = PageElement(self.page, "//a[@role='button']")
        self.installation = PageElement(self.page, "//a[text()='Installation']")
        self.writing_tests = PageElement(self.page, "//a[text()='Writing tests']")


class CommonMixin:
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        # General
        self.get_started_button = PageElement(self.page, "//a[text()='Get started']")

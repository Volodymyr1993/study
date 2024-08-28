from rozenka.components.base_page import BasePage
from rozenka.components.components import PythonMixin, CommonMixin
from playwright.sync_api import Page, TimeoutError, expect


class PythonPage(CommonMixin, PythonMixin, BasePage):
    pass





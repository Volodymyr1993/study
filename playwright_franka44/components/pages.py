from playwright_franka44.components.components import LoginMixin, CalendarPageMixin
from playwright_franka44.components.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(LoginMixin, BasePage):
    USERNAME = 'volodymyr.tkachenko93@gmail.com'
    PASSWORD = 'Password123!'

    def login_do(self):
        self.username_field.fill(self.USERNAME)
        self.password_field.fill(self.PASSWORD)
        self.enter_button.click()

class CalendarPage(LoginPage, CalendarPageMixin, BasePage):
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
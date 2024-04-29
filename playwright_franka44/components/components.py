from playwright.sync_api import Page, expect
from playwright_franka44.components.elements import PageElement


class CalendarPageMixin:
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        self.header_time = PageElement(self.page, "//span[@class='header-time']")
        self.shahivnutsy_drop_down = PageElement(self.page, "//span[text()='Шахівниця']")
        self.the_shahivnutsya_button = PageElement(self.page, "//span[text()='Шахівниця']")
        self.zaselenist_and_prices = PageElement(self.page, "//span[text()='Заселеність і ціни']")
        self.franka_1_row = PageElement(self.page, "//div[@data-original-title='DeMar Apart Franka 1']")
        self.franka_2_row = PageElement(self.page, "//div[@id='btn_close32']")
        self.x_alert = PageElement(self.page, "//div[@id='btn_close33']")
        self.calendar_sidebar = PageElement(self.page, "")


class LoginMixin:
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        self.username_field = PageElement(self.page, "//input[@id='userLogin']")
        self.password_field = PageElement(self.page, "//input[@id='password']")
        self.enter_button = PageElement(self.page, "//input[@value='Увійти']")
import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect, Page


class PageElement:
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
        self._locator = self.page.locator(selector)

class CalendarPage:
    def __init__(self, page: Page):
        self.some_button = PageElement(self.page, "//div[@id='btn_close32']")
        self.some_button2 = PageElement(self.page, "//div[@id='btn_close33']")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demarapart.otelms.com/login_c2/")
    page.locator("#userLogin").click()
    page.locator("#userLogin").fill("volodymyr.tkachenko93@gmail.com")
    page.locator("#userLogin").press("Tab")
    page.locator("#password").fill("Password123!")
    page.locator("#password").press("Enter")
    page.get_by_text("×").click()
    time.sleep(5)
    page.some_button.click()
    time.sleep(5)
    page.some_button2.click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

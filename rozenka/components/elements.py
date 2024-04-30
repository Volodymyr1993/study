from __future__ import annotations

from playwright.sync_api import Page
from typing import Type, List
import logging


class PageElement:
    """ Base parent-class for all elements """
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
        self._locator = self.page.locator(selector)
        self.log = logging.getLogger(self.__class__.__name__)

    def __getattr__(self, attr: str):
        if hasattr(self._locator, attr):
            self.log.debug(f'Doing `{attr}` to: `{self.selector}`')
            return getattr(self._locator, attr)

    def __dir__(self) -> List[str]:
        """Include methods from self._locator in dir() output"""
        return sorted(set(dir(type(self)) + list(self.__dict__.keys()) + dir(self._locator)))


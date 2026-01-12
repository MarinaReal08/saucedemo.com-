import re
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def element(self, locator: str):
        return self.page.locator(locator)

    def should_have_url_contains(self, part: str):
        # Playwright принимает только строку или regex, поэтому используем regex
        expect(self.page).to_have_url(re.compile(part))

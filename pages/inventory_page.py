from playwright.sync_api import expect
from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"

    def should_be_opened(self):
        self.should_have_url_contains("inventory.html")
        expect(self.element(self.TITLE)).to_have_text("Products")
        expect(self.element(self.INVENTORY_ITEM).first).to_be_visible()

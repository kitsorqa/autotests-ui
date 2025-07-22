from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator


class Input(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return self.get_locator(**kwargs).locator('textarea').first #Если ошибка, то использовать super().get_locator...

    def fill(self, value: str, **kwargs):
        locator = self.get_locator()
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        locator = self.get_locator()
        expect(locator).to_have_text(value)

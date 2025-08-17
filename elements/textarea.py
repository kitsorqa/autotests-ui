from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator
import allure

from tools.logger import get_logger

logger = get_logger("Textarea")


class Textarea(BaseElement):

    @property
    def type_of(self) -> str:
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth=0, **kwargs):
        step = f"fill {self.type_of} '{self.name}' to value '{value}'"

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth=0, **kwargs):
        step = f"fill {self.type_of} '{self.name}' to value '{value}'"

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(value)

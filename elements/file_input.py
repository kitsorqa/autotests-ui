from elements.base_element import BaseElement
import allure

from tools.logger import get_logger

logger = get_logger("FileInput")


class FileInput(BaseElement):

    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f"Set file '{file}' to the {self.type_of} '{self.name}'"

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(locator)
            locator.set_input_files(file)

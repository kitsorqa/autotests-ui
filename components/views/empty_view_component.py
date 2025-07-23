from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier

        self.icon = Icon(page, f"{self.identifier}-empty-view-icon", "Icon")
        self.title = Text(page, f"{self.identifier}-empty-view-title-text", "Title")
        self.description = Text(page, f"{self.identifier}-empty-view-description-text", "Description")

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)

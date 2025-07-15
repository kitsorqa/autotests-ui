from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Courses")

    def click_create_course_button(self):
        expect(self.create_course_button).click()
        self.check_current_url(re.compile(".*/#/courses/create"))
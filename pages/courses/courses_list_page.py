from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

from playwright.sync_api import Page


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(title='There is no results',
                                      description='Results from the load test pipeline will be displayed here')

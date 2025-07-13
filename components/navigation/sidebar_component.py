from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SideBarListItemComponent
from playwright.sync_api import Page, expect
import re

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SideBarListItemComponent(page, 'logout')
        self.courses_list_item = SideBarListItemComponent(page, 'courses')
        self.dashboard_list_item = SideBarListItemComponent(page, 'dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_dashboard(self):
        self.logout_list_item.navigate(re.compile(r".*/#/dashboard"))

    def click_courses(self):
        self.logout_list_item.navigate(re.compile(r".*/#/courses"))
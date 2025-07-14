import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from playwright.sync_api import Page


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(chromium_page)


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)

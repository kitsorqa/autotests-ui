import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page


@pytest.fixture(scope='function')
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)


@pytest.fixture(scope='function')
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(chromium_page)

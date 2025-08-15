from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.tags import AllureTag
from tools.epics import AllureEpic
from tools.features import AllureFeature
from tools.stories import AllureStories
from allure_commons.types import Severity
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:
    @allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
    @allure.title("Registration with correct email and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password)
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

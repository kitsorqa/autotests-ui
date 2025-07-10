from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                 email="user.name@gmail.com", username="user", password="pass"):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()
    registration_page.check_registration_form_has_not_error_alert()
    dashboard_page.check_dashboard_title()

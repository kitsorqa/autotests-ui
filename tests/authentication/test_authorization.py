import pytest
from pages.authentication.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")],
    ids=[
        "User with invalid email and password",
        "User with invalid email and empty password",
        "User with empty email and invalid password"
    ]
)
def test_wrong_email_or_password_authorization(email: str, password: str, login_page: LoginPage):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.login_form.fill(email=email, password=password)

    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

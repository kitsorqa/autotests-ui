from components.base_component import BaseComponent
from playwright.sync_api import expect, Page


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_field = page.get_by_test_id("login-form-email-input").locator("input")
        self.password_field = page.get_by_test_id("login-form-password-input").locator("input")

    def fill(self, email: str, password: str):
        self.email_field.fill(email)
        expect(self.email_field).to_have_value(email)

        self.password_field.fill(password)
        expect(self.password_field).to_have_value(password)

    def check_visible(self, email: str, password: str):
        expect(self.email_field).to_be_visible()
        expect(self.email_field).to_have_value(email)

        expect(self.password_field).to_be_visible()
        expect(self.password_field).to_have_value(password)

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_field).to_be_visible()
    expect(email_field).to_be_empty()
    email_field.fill('user.name@gmail.com')

    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_field).to_be_visible()
    expect(username_field).to_be_empty()
    username_field.fill('username')

    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_field).to_be_visible()
    expect(password_field).to_be_empty()
    password_field.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
    registration_button.click()

    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()

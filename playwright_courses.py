from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    context.storage_state(path="local_storage_state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="local_storage_state.json")
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    folder_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    courses_result_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_result_title).to_be_visible()
    expect(courses_result_title).to_have_text("There is no results")

    description_of_result_courses = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(description_of_result_courses).to_be_visible()
    expect(description_of_result_courses).to_have_text("Results from the load test pipeline will be displayed here")

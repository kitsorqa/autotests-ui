from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    folder_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    courses_result_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_result_title).to_be_visible()
    expect(courses_result_title).to_have_text("There is no results")

    description_of_result_courses = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(description_of_result_courses).to_be_visible()
    expect(description_of_result_courses).to_have_text("Results from the load test pipeline will be displayed here")

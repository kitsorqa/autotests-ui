from tools import set_environment
import pytest


@pytest.fixture(autouse=True, scope="session")
def save_environment_file_for_allure_report():
    yield
    set_environment.create_environment_file_for_allure()

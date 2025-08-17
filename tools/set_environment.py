from config import settings
import sys
import platform


def create_environment_file_for_allure() -> None:
    items = [f'{k}={v}' for k, v in settings.model_dump().items()]
    items.append(f'os_info={platform.system()}, {platform.version()}')
    items.append(f'python_version={sys.version}')
    items = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(items)

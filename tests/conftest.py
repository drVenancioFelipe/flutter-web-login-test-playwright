import pytest
from tests.config import load_env


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Ambiente: dev, staging ou prod"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return load_env(env)
import logging
from collections.abc import Generator

import allure
import pytest
from _pytest.fixtures import FixtureRequest


def pytest_configure() -> None:
    """Configure logging for the tests."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@pytest.fixture(autouse=True)
def logger_and_allure(request: FixtureRequest) -> Generator[None]:
    """Fixture to automatically log test steps and attach logs to Allure."""
    logger = logging.getLogger(request.node.name)
    log_messages = []

    logger.info("Starting test: %s", request.node.name)
    log_messages.append(f"Starting test: {request.node.name}")

    yield

    logger.info("Finished test: %s", request.node.name)
    log_messages.append(f"Finished test: {request.node.name}")

    allure.attach(
        "\n".join(log_messages),
        name="Test Logs",
        attachment_type=allure.attachment_type.TEXT,
    )

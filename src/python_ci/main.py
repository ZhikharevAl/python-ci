# pylint: disable=missing-module-docstring


import logging


def main() -> None:
    """The main function logs the string 'Hello from python-ci!' at the INFO level."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Hello from python-ci!")


def generate_list() -> int:
    """This function returns 42."""
    return 42

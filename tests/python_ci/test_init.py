import allure

from src.python_ci.main import generate_list


@allure.title("Test function generate_list")
@allure.description("Проверяет, что функция generate_list возвращает ожидаемое значение.")
def test_generate_list() -> None:
    """Test that `generate_list` returns the expected value."""
    with allure.step("Вызов функции generate_list"):  # type: ignore
        result = generate_list()

    with allure.step("Проверка результата"):  # type: ignore
        assert result == 42, f"Ожидалось 42, но получено {result}"

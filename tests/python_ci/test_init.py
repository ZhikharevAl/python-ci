import allure

from src.python_ci.main import generate_list


@allure.epic("List Generation")
@allure.feature("Generate List Functionality")
@allure.description_html("""
<h2>Testing List Generation Functionality</h2>
<p>Test verifies the functionality of the `generate_list` function, including:</p>
<ul>
    <li>Calling the `generate_list` function</li>
    <li>Validating the returned result</li>
</ul>
<p>The test performs the following checks:</p>
<ul>
    <li>Confirms that the function returns the expected value</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>The function should return the value `42`</li>
</ul>
""")
class TestGenerateList:
    """The test class for the `generate_list` function."""

    @allure.story("List Generation")
    @allure.severity(severity_level="CRITICAL")
    def test_generate_list(self) -> None:
        """Test that `generate_list` returns the expected value."""
        with allure.step("Call the `generate_list` function"):  # type: ignore
            result = generate_list()

        with allure.step("Validate the result"):  # type: ignore
            assert result == 42, f"Expected 42, but got {result}"

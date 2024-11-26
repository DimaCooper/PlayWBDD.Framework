from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging


logger = logging.getLogger('TestLogger')

# Given dropdown "Some dropdown" has the following values
#   |value       |
#   |First option|
# Then dropdown "Some dropdown" should have the following values
#   |value       |
#   |First option|
@given("dropdown \"{element_name}\" has the following values")
@then("dropdown \"{element_name}\" should have the following values")
def check_dropdown_items(context, element_name):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        # Retrieve expected items from table
        expected_items = [row["value"] for row in context.table.rows]
        
        # Collect actual items inside the dropdown
        actual_items = element_name.locator('xpath=.//option').all()
        actual_values = [item.text_content() for item in actual_items]
        
        assert set(expected_items) == set(actual_values), f"Expected items: {expected_items}, Actual items: {actual_values}"
        logger.info(f"Dropdown {element_name} has the following values")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise

# Given (partially|exactly): dropdown "Some dropdown" (contains|not contains) the following values
#   |value       |
#   |First option|
# Then (partially|exactly): dropdown "Some dropdown" (contains|not contains) the following values
#   |value       |
#   |First option|
@given("{completeness}: dropdown \"{element_name}\" {behavior} the following values")
@then("{completeness}: dropdown \"{element_name}\" {behavior} the following values")
def check_dropdown_contains_multiple_items(context, element_name, behavior, completeness):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])

        # Retrieve expected items from table
        expected_values = [row['value'] for row in context.table.rows]

        actual_items = element_name.locator('xpath=.//option').all()
        actual_values = [item.text_content() for item in actual_items]

        if behavior == 'contains':
            if completeness == 'partially':
                assert any(value in option for value in expected_values for option in actual_values), f"Dropdown does not partially contain all expected items: {expected_values}"
                logger.info(f"{completeness}: dropdown {element_name} has the following values")
            elif completeness == 'exactly':
                assert all(option in expected_values for option in actual_values), f"Dropdown does not exactly match the expected values: {expected_values}"
                logger.info(f"{completeness}: dropdown {element_name} has the following values")
        elif behavior == 'not contains':
            if completeness == 'partially':
                assert all(value not in option for value in expected_values for option in actual_values), f"Dropdown should not partially contain any of the expected items: {expected_values}"
                logger.info(f"{completeness}: dropdown {element_name} not contains the following values")
            elif completeness == 'exactly':
                assert not any(option in expected_values for option in actual_values), f"Dropdown should not exactly match any of the expected values: {expected_values}"
                logger.info(f"{completeness}: dropdown {element_name} not contains the following values")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given the following values are selected in "Some dropdown"
#   |value       |
#   |First option|
# Then the following values should be selected in "Some dropdown"
#   |value       |
#   |First option|
@given("the following values are selected in \"{element_name}\"")
@then("the following values should be selected in \"{element_name}\"")
def check_multiple_selected_values(context, element_name):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])

        # Retrieve expected items from table
        expected_items = [row["value"] for row in context.table.rows]

        actual_items = element_name.locator('xpath=.//option[@selected]').all()

        # Collect actual selected options inside the dropdown
        actual_selected_options = [item.text_content() for item in actual_items]

        assert set(expected_items) == set(actual_selected_options), (
                f"Expected items: {expected_items}, Actual selected items: {actual_selected_options}"
            )
        logger.info(f"The following values are selected in {element_name}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
    

# NOT TESTED
# Given the following values (enabled|disabled) in "Some dropdown" dropdown
#   |value       |
#   |First option|
# Then the following values should be (enabled|disabled) in "Some dropdown" dropdown
#   |value       |
#   |First option|
@given("the following values {behavior} in \"{element_name}\" dropdown")
@then("the following values should be {behavior} in \"{element_name}\" dropdown")
def check_dropdown_values_enabled(context, behavior, element_name):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])

        expected_items = [row["value"] for row in context.table.rows]


        if behavior == 'enabled':
            actual_items = element_name.locator("xpath=.//option[@disabled='false']").all()
            actual_enabled_options = [item.text_content() for item in actual_items]
            assert set(expected_items) == set(actual_enabled_options), (
                f"Expected items: {expected_items}, Actual selected items: {actual_enabled_options}"
            )
            logger.info(f"The following values enabled in {element_name} dropdown")
        elif behavior == 'disabled':
            actual_items = element_name.locator("xpath=.//option[@disabled='true']").all()
            actual_disabled_options = [item.text_content() for item in actual_items]
            assert set(expected_items) == set(actual_disabled_options), (
                f"Expected items: {expected_items}, Actual selected items: {actual_disabled_options}"
            )
            logger.info(f"The following values disabled in {element_name} dropdown")
        else:
            logger.info(f"Unsupported behavior: {behavior}")
            raise ValueError(f"Unsupported behavior: {behavior}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given no values are selected in "Some dropdown"
# Then no values should be selected in "Some dropdown"
@given("no values are selected in \"{element_name}\"")
@then("no values should be selected in \"{element_name}\"")
def check_no_values_selected_in_dropdown(context, element_name):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        actual_items = element_name.locator("xpath=.//option[@selected='selected']").all()
        # Collect actual selected options inside the dropdown
        actual_selected_options = [item.text_content() for item in actual_items]
        
        assert not actual_selected_options, f"No values should be selected, but found: {actual_selected_options}"
        logger.info(f"No values are selected in {element_name}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise

# NOT TESTED
# Given deselected all values in "Some dropdown"
# When deselects all values in "Some dropdown"
@given("deselected all values in \"{element_name}\"")
@when("deselects all values in \"{element_name}\"")
def clear_multi_select_dropdown_values(context, element_name):
    try:
        # Get the dropdown list by name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        actual_items = element_name.locator("xpath=.//option[@selected='selected']").all()
        # Deselect all options inside the dropdown
        for option in actual_items:
            option.click()

        # Verify that no values are selected
        actual_selected_options = [item.text_content() for item in actual_items]
        
        assert not actual_selected_options, f"No values should be selected, but found: {actual_selected_options}"
        logger.info(f"Deselected all values in {element_name}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given user selects values in "Some dropdown"
#   |value       |
#   |First option|
# When user selects values in "Some dropdown"
#   |value       |
#   |First option|
@given("user selects values in \"{element_name}\"")
@when("user selects values in \"{element_name}\"")
def step_select_multi_select_dropdown_values(context, element_name):
    try:
        # Get the dropdown locator by the element name
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        
        # Open the drop-down list
        element_name.click()

        # Extract values ​​from the table
        value_list = [row['value'] for row in context.table]

        # Select each of the specified values
        for value in value_list:
            option_locator = element_name.locator(f"xpath=.//option[text()='{value}']")
            
            option_locator.click()

        # Check that the selected values ​​are actually present
        actual_selected_options = [
            option.text_content() for option in element_name.locator("xpath=.//option[@selected='selected']")
        ]

        assert set(value_list) == set(actual_selected_options), f"Selected values do not match: expected {value_list}, but found {actual_selected_options}"
        logger.info(f"User selected values in {element_name}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
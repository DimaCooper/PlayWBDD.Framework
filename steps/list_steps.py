from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging


logger = logging.getLogger('TestLogger')

# Given list "Some list" (has|does not have) the following items
#   |itemName     |
#   |Test value 1 |
#   |Test value 2 |
# Then list "Some list" (have|not have) the following items
#   |itemName     |
#   |Test value 1 |
#   |Test value 2 |
@given("list \"{element_name}\" {behavior} the following items")
@then("list \"{element_name}\" {behavior} the following items")
def check_list_items(context, element_name, behavior):
    try:
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        expected_values = [row['itemName'] for row in context.table]

        print(f"Expected values: {expected_values}")
        
        # Get the items inside your locator in their order of appearance on the page
        list_items = element_name.locator('xpath=.//*[not(*)]').all()
        
        # Extract text from the elements in the order they appear on the page
        list_values = [item.text_content() for item in list_items]
        # Debug: Print each list value in its order of appearance
        for idx, value in enumerate(list_values):
            print(f"List value {idx}: '{value}'")  # Print each value as it appears
        
        # Debug: Print the actual values found in the list in the order they appear on the page
        print(f"Actual values in the list in the order they appear: {list_values}")
        if behavior in ["has", "have"]:
            for expected_value in expected_values:
                assert expected_value in list_values, f"{element_name} does not have the expected item: {expected_value}"
                logger.info(f"list {element_name} has the following items")
        elif behavior in ["does not have", "not have"]:
            for expected_value in expected_values:
                assert expected_value not in list_values, f"{element_name} has the unexpected item: {expected_value}"
                logger.info(f"list {element_name} does not have the following items")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given in exact order list "Some list" (has|does not have) the following items
#   |itemName     |
#   |Test value 1 |
#   |Test value 2 |
# Then in exact order list "Some list" (have|not have) the following items
#   |itemName     |
#   |Test value 1 |
#   |Test value 2 |
@given("in exact order list \"{element_name}\" {behavior} the following items")
@then("in exact order list \"{element_name}\" should {behavior} the following items")
def check_list_items_in_exact_order(context, element_name, behavior):
    try:
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        expected_values = [row['itemName'] for row in context.table]
        
        # Debug: Print the expected values
        print(f"Expected values: {expected_values}")
        
        # Get items inside your locator in their order of appearance on the page
        list_items = element_name.locator('xpath=.//*[not(*)]').all()
        
        # Extract text from elements in the order they appear on the page
        list_values = [item.text_content() for item in list_items]
        # Debug: Print each list value in its order of appearance
        for idx, value in enumerate(list_values):
            print(f"List value {idx}: '{value}'")  # Print each value as it appears
        
        # Debug: Print the actual values found in the list
        print(f"Actual values in the list: {list_values}")
        
        # Check if the list has the expected items in exact order
        if behavior in ["has", "have"]:
            assert list_values == expected_values, f"{element_name} does not have the expected items in exact order: {expected_values}"
            logger.info(f"in exact order list {element_name} have the following items")
        elif behavior in ["does not have", "not have"]:
            assert list_values != expected_values, f"{element_name} has the unexpected items in exact order: {expected_values}"
            logger.info(f"in exact order list {element_name} does not have the following items")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise

from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging

logger = logging.getLogger('TestLogger')

# Given user entered "test string" into "Test" input
# When user enters "test string" into "Test" input
@given("user entered \"{input}\" into \"{element_name}\" input")
@when("user enters \"{input}\" into \"{element_name}\" input")
def enter_input(context, input, element_name):
    try:
        locators = collect_all_locators()
        element_name = context.page.locator(locators[element_name])
        element_name.fill(input)
        logger.info(f"User entered {input} into {element_name} input")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given user cleared "Test" input
# When user clears "Test" input
@given("user cleared \"{element_name}\" input")
@when("user clears \"{element_name}\" input")
def clear_input(context, element_name):
    try:
        locators = collect_all_locators()
        element_name = context.page.locator(locators[element_name])
        element_name.fill("")
        logger.info(f"user cleared {element_name} input")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
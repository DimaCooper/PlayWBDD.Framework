from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging

logger = logging.getLogger('TestLogger')
# Given user clicked on "Test button"
# When user clicks on "Test button"
@given('user clicked on \"{element_name}\"')
@when('user clicks on \"{element_name}\"')
def step_impl(context, element_name):
    try:
        locators = collect_all_locators()
        element = context.page.locator(locators[element_name])
        element.click()
        logger.info(f"Successfully click on {element_name}")
    except Exception as e:
            logger.error(f"Error click on: {str(e)}")
            raise

# Given user clicked twice on "Test button"
# When user clicks twice on "Test button"
@given('user clicked twice on \"{element_name}\"')
@when('user clicks twice on \"{element_name}\"')
def step_impl(context, element_name):
    try:
        locators = collect_all_locators()
        element = context.page.locator(locators[element_name])
        element.click()
        element.click()
        logger.info(f"Successfully click twice on {element_name}")
    except Exception as e:
            logger.error(f"Error click twice on: {str(e)}")
            raise


# Given user hovered mouse over "Test button"
# When user hovers mouse over "Test button"
@given('user hovered mouse over \"{element_name}\"')
@when('user hovers mouse over \"{element_name}\"')
def step_impl(context, element_name):
    try:
        locators = collect_all_locators()
        element = context.page.locator(locators[element_name])
        element.hover()
        logger.info(f"Successfully hover mouse over {element_name}")
    except Exception as e:
            logger.error(f"Error hover mouse over: {str(e)}")
            raise
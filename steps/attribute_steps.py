from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging


logger = logging.getLogger('TestLogger')

# Given the "Some element" (is|is not|become| become not) (enabled|disabled)
# When the "Some element" (is|is not|become| become not) (enabled|disabled)
# Then the "Some element" should (be|be not|become|become not) (enabled|disabled)
@given("the \"{element_name}\" {behavior} {enabled}")
@when("the \"{element_name}\" {behavior} {enabled}")
@then("the \"{element_name}\" should {behavior} {enabled}")
def check_element_name_enabled(context, element_name, behavior, enabled):
    try:
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        status = "enabled" if element_name.is_enabled() else "disabled"
        print(f"{element_name} is {status}")
        enabled = enabled == "enabled"
        if behavior in ["is", "be", "become"]:
            assert element_name.is_enabled() == enabled, f"{element_name} is{'' if enabled else ' not'} enabled"
            logger.info("Element {element_name} is enabled")
        elif behavior in ["is not", "be not", "become not"]:
            assert element_name.is_enabled() != enabled, f"{element_name} is{'' if enabled else ' not'} enabled"
            logger.info(f"Element {element_name} is disabled")
    except Exception as e:
            logger.error(f"Error enabled check: {str(e)}")
            raise


# Given the "Some element" (is|is not|become| become not) (visible|invisible)
# When the "Some element" (is|is not|become| become not) (visible|invisible)
# Then the "Some element" should (be|be not|become|become not) (visible|invisible)
@given("element \"{element_name}\" {behavior} {visible}")
@when("element \"{element_name}\" {behavior} {visible}")
@then("element \"{element_name}\" should {behavior} {visible}")
def check_element_name_visible(context, element_name, behavior, visible):
    try:
        locator = collect_all_locators()
        element_name = context.page.locator(locator[element_name])
        status = "visible" if element_name.is_visible() else "invisible"
        print(f"{element_name} is {status}")
        visible = visible == "visible"
        if behavior in ["is", "be", "become"]:
            assert element_name.is_visible() == visible, f"{element_name} is{'' if visible else ' not'} visible"
            logger.info("Element {element_name} is visible")
        elif behavior in ["is not", "be not", "become not"]:
            assert element_name.is_visible() != visible, f"{element_name} is{'' if visible else ' not'} visible"
            logger.info(f"Element {element_name} is invisible")
    except Exception as e:
            logger.error(f"Error visible check: {str(e)}")
            raise


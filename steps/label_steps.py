from behave import given, when, then
from playwright.sync_api import sync_playwright
from utils.locator_utils import collect_all_locators
import logging


logger = logging.getLogger('TestLogger')

# Given the element "Test-element" text (is|is not|become) "expected text"
# Then the element "Test-element" text should (be|be not|become not) "expected text"
@given("the element \"{element_name}\" text {behavior} \"{expected_text}\"")
@then("the element \"{element_name}\" text should {behavior} \"{expected_text}\"")
def check_element_text(context, element_name, behavior, expected_text):
    try:
        locator = collect_all_locators()
        element = context.page.locator(locator[element_name])
        actual_text = element.text_content()
        print(f"{element_name} text is \"{actual_text}\"")
        expected_text = expected_text.replace("\\n", "\n")
        if behavior in ["is", "be", "become"]:
            assert actual_text == expected_text, f"{element_name} text is{'' if actual_text == expected_text else ' not'} \"{expected_text}\""
            logger.info(f"the element {element_name} text is {expected_text}")
        elif behavior in ["is not", "be not", "become not"]:
            assert actual_text != expected_text, f"{element_name} text is{'' if actual_text != expected_text else ' not'} \"{expected_text}\""
            logger.info(f"the element {element_name} text is not {expected_text}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given inside "Test-element" (contains|does not contains) "expected string" text
# Then inside "Test-element" should (contain|not contain) "expected string" text
@given("inside \"{element_name}\" {behavior} \"{expected_text}\" text")
@then("inside \"{element_name}\" should {behavior} \"{expected_text}\" text")
def check_element_text_contains(context, element_name, behavior, expected_text):
    try:
        locator = collect_all_locators()
        element = context.page.locator(locator[element_name])
        actual_text = element.text_content()
        print(f"{element_name} text is \"{actual_text}\"")
        expected_text = expected_text.replace("\\n", "\n")
        if behavior in ["contains", "contain"]:
            assert expected_text in actual_text, f"{element_name} text does{'' if expected_text in actual_text else ' not'} contain \"{expected_text}\""
            logger.info(f"inside {element_name} contains {expected_text} text")
        elif behavior in ["does not contains", "not contain"]:
            assert expected_text not in actual_text, f"{element_name} text does{'' if expected_text not in actual_text else ' not'} contain \"{expected_text}\""
            logger.info(f"inside {element_name} not contains {expected_text} text")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given text (is|is not|become) empty inside "Test-element"
# Then text should (be|be not|become not) empty inside "Test-element"
@given("text {behavior} empty inside \"{element_name}\"")
@then("text should {behavior} empty inside \"{element_name}\"")
def check_element_text_empty(context, element_name, behavior):
    try:
        locator = collect_all_locators()
        element = context.page.locator(locator[element_name])
        actual_text = element.text_content()
        print(f"{element_name} text is \"{actual_text}\"")
        if behavior in ["is", "be", "become"]:
            assert actual_text == "", f"{element_name} text is{'' if actual_text == '' else ' not'} empty"
            logger.info(f"text is empty inside {element_name}")
        elif behavior in ["is not", "be not", "become not"]:
            assert actual_text != "", f"{element_name} text is{'' if actual_text != '' else ' not'} empty"
            logger.info(f"text is not empty inside {element_name}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
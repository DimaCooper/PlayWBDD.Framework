from behave import given, when, then
from playwright.sync_api import Page
from config import BASE_URL  # Import the base URL from config.py
import logging


logger = logging.getLogger('TestLogger')

# Given URL is opened
# When user opens URL
@given("URL is opened")
@when("user opens URL")
def open_url(context):
    try:
        context.page.goto(BASE_URL)  # Use BASE_URL from config
        logger.info(f"URL is opened {context}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given URL "https://example.com/" is opened
# When user opens URL "https://example.com/"
@given("URL \"{url}\" is opened")
@when("user opens URL \"{url}\"")
def navigate_custom_url(context, url):
    try:
        context.page.goto(url)  # Use url from step
        logger.info(f"URL {url} is opened")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given relative URL "/test-url" is opened
# When user opens relative URL "/test-url"
@given("relative URL \"{url}\" is opened")
@when("user opens relative URL \"{url}\"")
def navigate_to_relative_url(context, url):
    try:
        context.page.goto(BASE_URL + url)  # Use BASE_URL from config and relative URL from step
        logger.info(f"Relative URL {url} is opened")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given page URL "https://example.com/" (is|is not|becomes|becomes not) opened
# Then page URL "https://example.com/" should (be|not be|become|not become) opened
@given("page URL \"{url}\" {behavior} opened")
@then("page URL \"{url}\" should {behavior} opened")
def check_url(context, url, behavior):
    try:
        if behavior in ["is", "be"]:
            assert context.page.url == url, f"current URL is {context.page.url}"
        elif behavior in ["is not", "not be"]:
            assert context.page.url != url, f"current URL is {context.page.url}"
        elif behavior in ["becomes", "become"]:
            assert context.page.url == url, f"current URL is {context.page.url}"
        elif behavior in ["becomes not", "not become"]:
            assert context.page.url != url, f"current URL is {context.page.url}"
        logger.info(f"Page URL {url} is opened")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given relative URL (is|is not|become|become not) "/test-page"
# Then relative URL should (be|be not|become|become not) "/test-page"
@given("relative URL \"{url}\" {behavior}")
@then("relative URL should {behavior} \"{url}\"")
def check_relative_url(context, url, behavior):
    try:
        expected_url = BASE_URL + url
        if behavior in ["is", "be"]:
            assert context.page.url == expected_url, f"current URL is {context.page.url}"
        elif behavior in ["is not", "not be"]:
            assert context.page.url != expected_url, f"current URL is {context.page.url}"
        elif behavior in ["becomes", "become"]:
            assert context.page.url == expected_url, f"current URL is {context.page.url}"
        elif behavior in ["becomes not", "not become"]:
            assert context.page.url != expected_url, f"current URL is {context.page.url}"
        logger.info(f"Relative URL is {url}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given page (contains|not contains) "https://example.com/" URL
# Then page (should|should not) contain "https://example.com/" URL
@given("page {behavior} \"{url}\" URL")
@then("page {behavior} contain \"{url}\" URL")
def check_url_contains(context, behavior, url):
    try:
        current_url = context.page.url
        if behavior in ["contains", "should"]:
            assert url in current_url, f"current URL is {current_url}"
        elif behavior in ["not contains", "should not"]:
            assert url not in current_url, f"current URL is {current_url}"
        logger.info(f"Page contains {url} URL")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given page title (is|is not|become|become not) "{title}"
# Then page title should (be|be not|become|become not) "{title}"
@given("page title {behavior} \"{title}\"")
@then("page title should {behavior} \"{title}\"")
def check_page_title(context, behavior, title):
    try:
        current_title = context.page.title
        if behavior in ["is", "be"]:
            assert current_title == title, f"current title is {current_title}"
        elif behavior in ["is not", "not be"]:
            assert current_title != title, f"current title is {current_title}"
        elif behavior in ["becomes", "become"]:
            assert current_title == title, f"current title is {current_title}"
        elif behavior in ["becomes not", "not become"]:
            assert current_title != title, f"current title is {current_title}"
        logger.info(f"Page title is {title}")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise


# Given user reloaded current page
# When user reloads current page
@given("user reloaded current page")
@when("user reloads current page")
def reload_current_page(context):
    try:
        context.page.reload()
        logger.info("User reloaded current page")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
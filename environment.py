from playwright.sync_api import sync_playwright
from utils.logger import TestLogger

def before_all(context):
    context.logger = TestLogger().logger

def before_feature(context, feature):
    context.logger.info(f"\nStarting feature execution: {feature.name}")

def before_scenario(context, scenario):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.page = browser.new_page()
    context.playwright = playwright
    if "skip" in scenario.tags:
        scenario.skip("Marked with @skip")
    if "wip" in scenario.tags:
        scenario.skip("Test is Work in Progress")
    if "manual" in scenario.tags:
        scenario.skip("This is a manual test")
    # Don't skip automated tests, they should be executed
    context.logger.info(f"\nStarting scenario execution: {scenario.name}")

def after_scenario(context, scenario):
    context.page.close()
    context.playwright.stop()

    # Log scenario execution result
    if scenario.status == "passed":
        context.logger.success(f"Scenario '{scenario.name}' successfully completed")
    elif scenario.status == "skipped":
        if "skip" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: marked with @skip tag")
        elif "wip" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: test in development (WIP)")
        elif "manual" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: manual test")
    else:
        context.logger.error(f"Scenario '{scenario.name}' failed")
    
def after_feature(context, feature):
    context.logger.info(f"Finishing feature execution: {feature.name}")

def after_all(context):
    context.logger.info("Finishing all tests execution")
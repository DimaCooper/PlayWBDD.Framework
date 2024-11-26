from behave import given, when, then
import time
import logging


logger = logging.getLogger('TestLogger')

# Given wait "5" sec
# When wait "5" sec
# Then wait "5" sec
@given('wait \"{sec:d}\" sec')
@when('wait \"{sec:d}\" sec')
@then('wait \"{sec:d}\" sec')
def wait_steps(context, sec):
    # Conversion of sec to an integer is not necessary as int type is used
    try:
        time.sleep(sec)  # Delay in seconds
        logger.info(f"Wait {sec} seconds")
    except Exception as e:
            logger.error(f"Error wait: {str(e)}")
            raise

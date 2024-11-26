from behave import then
import os
import logging
from config import DOWNLOAD_PATH  # Import path from configuration file

logger = logging.getLogger('TestLogger')

# Then "Test.pdf" file should be downloaded
@then('"{filename}" file should be downloaded')
def check_file_downloaded(filename):
    try:
        file_path = os.path.join(DOWNLOAD_PATH, filename)  # Use the path from configuration
        
        # Check if the file exists
        assert os.path.exists(file_path), f"file {file_path} does not exist"

        # Check that the file is not empty
        length = os.path.getsize(file_path)
        assert length != 0, f"file {file_path} is empty"
        logger.info(f"File {filename} downloaded")
    except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise
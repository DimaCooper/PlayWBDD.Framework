import logging
import os
from datetime import datetime

class TestLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
            cls._instance.success = 0
        return cls._instance
    
    def _initialize_logger(self):
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Create log filename with current date
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'test_run_{current_time}.log')
        
        # Configure formatting
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Configure file handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        
        # Configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # Configure logger
        self.logger = logging.getLogger('TestLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        # Add formatting for success messages
        success_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - ✅ %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Create new logging level for success messages
        SUCCESS_LEVEL = 25  # Between INFO (20) and WARNING (30)
        logging.addLevelName(SUCCESS_LEVEL, 'SUCCESS')
        
        def success(self, message):
            self._log(SUCCESS_LEVEL, message, args=())
        
        logging.Logger.success = success
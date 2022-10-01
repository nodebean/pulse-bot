import logging
import sys

class StdErrFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.CRITICAL, logging.ERROR)

class StdOutFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO, logging.WARNING)

class Logger:
    def __init__(self):
        try:
            
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            self.log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

            self.stdout_handler = logging.StreamHandler(sys.stdout)
            self.stdout_handler.setLevel(logging.DEBUG) 
            self.stdout_handler.setFormatter(self.log_formatter)  
            self.stdout_handler.addFilter(StdOutFilter())
            self.logger.addHandler(self.stdout_handler)                                

            self.stderr_handler = logging.StreamHandler(sys.stderr)
            self.stderr_handler.setLevel(logging.WARNING)
            self.stderr_handler.setFormatter(self.log_formatter)
            self.stderr_handler.addFilter(StdErrFilter())
            self.logger.addHandler(self.stderr_handler)

        except Exception as e:
            print("Error while creating logger : ", e)
            raise
# -*- coding: utf-8 -*-
"""
Utility Snippet: Simple Logger for Ansys Scripting
Tested on: IronPython 2.7 (Ansys 2023 R2)

Description:
A simple logging utility that works within Ansys products where 
the standard 'logging' module might be limited or complex to configure.
"""

import datetime

class SimpleLogger(object):
    """
    A simple logger that writes to a file and/or the console.
    """
    def __init__(self, log_path=None):
        self.log_path = log_path
        
    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = "[{}] [{}] {}".format(timestamp, level, message)
        
        # Output to Ansys Console
        print(formatted_message)
        
        # Output to File if path is provided
        if self.log_path:
            try:
                with open(self.log_path, "a") as f:
                    f.write(formatted_message + "\n")
            except Exception as e:
                print("Failed to write to log file: {}".format(e))

    def info(self, message):
        self._log("INFO", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)

# Usage Example:
# logger = SimpleLogger("C:/Temp/ansys_script.log")
# logger.info("Script started")
# logger.error("An error occurred")


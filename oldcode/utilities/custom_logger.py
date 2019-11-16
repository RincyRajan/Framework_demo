import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #gets the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    fileHandler= logging.
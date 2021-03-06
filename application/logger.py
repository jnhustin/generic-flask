import logging
from pythonjsonlogger import jsonlogger


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Logger:
  def __init__(self):
    self.l =  None


  def get_logger(self):
    if not self.l:
      self.l = self.start_logger()
    return self.l


  def start_logger(self):
    # configure logging
    formatter  = jsonlogger.JsonFormatter('(levelname), (module), (funcName), (asctime), (process), (message)')
    logger     = logging.getLogger(__name__)
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    # change log lvls here  ['INFO', 'DEBUG']
    logger.setLevel(logging.DEBUG)

    # Disable flask logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    return logger

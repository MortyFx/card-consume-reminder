import logging

class log:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s [%(levelname)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename='sms.log',
                            filemode='a')
        req_logger = logging.getLogger("requests")
        req_logger.setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def info(self,content):
        logging.info(content)

    def warning(self, content):
        logging.warning(content)

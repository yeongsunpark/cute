import logging
# custom_logger.py 와 구분을 위해 이름 바꿈

class MyHandler(logging.StreamHandler):

    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = '[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s >>> %(message)s'
        fmt_date = '%Y-%m-%d_%T %Z'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)

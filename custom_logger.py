__author__ = "Lynn Hong"
__date__ = "04/08/2017"


import logging

class MyHandler(logging.StreamHandler):

    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = '[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s >>> %(message)s'
        fmt_date = '%Y-%m-%d_%T %Z'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)

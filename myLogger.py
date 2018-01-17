import logging


class MyLogger:
    def __init__(self):
        self.name = "Log"

    @staticmethod
    def mylogging():
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='D:/Data/YumWar/log/mc.log',
                            filemode='w')
        return logging

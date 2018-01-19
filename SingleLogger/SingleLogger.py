import logging
import os


class SingleLogger(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if SingleLogger.__instance is None:
            SingleLogger.__instance = object.__new__(cls, *args, **kwargs)
            SingleLogger.__instance.__logger = logging.getLogger("mc_web")
            SingleLogger.__instance.__logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(name)-4s [%(asctime)s] %(levelname)-8s %(message)s',
                                          '%a, %d %b %Y %H:%M:%S', )
            file_handler = logging.FileHandler(r"D:/Data/YumWar/log/mc.log")
            file_handler.setLevel(logging.INFO)
            stream_handler = logging.StreamHandler()
            file_handler.setFormatter(formatter)
            SingleLogger.__instance.__logger.addHandler(file_handler)
            SingleLogger.__instance.__logger.addHandler(stream_handler)
            SingleLogger.__instance.__logger.info("log info: " + os.getcwd())
        return SingleLogger.__instance

    def info(self, message):
        SingleLogger.__instance.__logger.info(message)
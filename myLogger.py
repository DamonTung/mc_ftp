from SingleLogger import SingleLogger


class MyLogger:
    def __init__(self):
        self.name = "Log"

    @staticmethod
    def mylogging():
        my_log = SingleLogger.SingleLogger()
        return my_log

import time


class ClassTime:

    @staticmethod
    def delay():
        print("Checking Account", end="")
        for i in range(5):
            print(".", end="")
            time.sleep(1)

    @staticmethod
    def delay_for_logging_request():
        print()
        print("Logging request", end="")
        for i in range(5):
            print(".", end="")
            time.sleep(1)

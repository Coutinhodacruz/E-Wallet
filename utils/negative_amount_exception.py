class AmountCannotBeNegative(Exception):

    def __init__(self, message):
        self.__message = message

from enum import Enum


class TransactionType(Enum):
    DEBIT = "D"
    CREDIT = "C"
    NULL = ""

# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# AutoNumberEnum
#

from enum import Enum


class AutoNumberEnum(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

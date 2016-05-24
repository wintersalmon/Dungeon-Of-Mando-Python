# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Status Interface

class Status:
    def __init__(self,code):
        self.__code = code

    def code(self):
        return self.__code
    
    def update(self,data):
        pass

    def next_status(self,data):
        pass

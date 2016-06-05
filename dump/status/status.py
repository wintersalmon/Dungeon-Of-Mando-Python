# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# Status
#

# from mandom.status.status_type import StatusType

class Status():    
    def __init__(self, name, start_status, success_end_status, failed_end_status = None):
        self.__name = name
        self.__start_status = start_status
        self.__success_end_status = success_end_status
        self.__failed_end_status  = failed_end_status if failed_end_status != None else start_status
    
    def name(self):
        return self.__name
    
    def start_status(self):
        return self.__start_status
    
    def success_end_status(self):
        return self.__success_end_status
    
    def failed_end_status(self):
        return self.__failed_end_status
        
    def update(dungeon):
        pass
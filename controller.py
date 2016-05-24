# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Controller

from dungeon import Dungeon
from status_for_dungeon import STATUS, START_STATUS_CODE


class Controller():
    def __init__(self, target_data):
        self.__target_data = target_data

    def update(self):
        print('UPDATE')
    
    def data(self):
        return self.__target_data


class DungeonController(Controller):
    def __init__(self,dungeon):
        super().__init__(dungeon)
        self.__cur_status  = START_STATUS_CODE

    def update(self):
        cur_status  = self.__cur_status
        STATUS[cur_status].update(self.data())
        next_status = STATUS[cur_status].next_status(self.data())
        self.__cur_status = next_status
        return True
    
    def running(self):
        return self.__cur_status != None
       
    

# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Viewer

from dungeon import Dungeon


class Viewer():
    def __init__(self, target_data):
        self.__target_data = target_data
    
    def data(self):
        return self.__target_data


class DungeonViewer(Viewer):
    def __init__(self,dungeon):
        super().__init__(dungeon)

    def show(self):
        event_list = self.data()
        idx = self.data().event_list_size() - 1
        print('({}) {}'.format(idx, event_list.event_at(idx).message()))

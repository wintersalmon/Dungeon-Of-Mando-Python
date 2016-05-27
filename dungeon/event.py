# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Event

class Event:
    def __init__(self,msg):
        self.__message = msg

    def __init__(self, prefix, title, content):
        #self.__prefix  = prefix
        #self.__title   = title
        #self.__content = content
        self.__message = '[{}] {} : {}'.format(prefix,title,content)

    def message(self):
        return self.__message
    

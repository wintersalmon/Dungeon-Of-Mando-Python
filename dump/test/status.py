class TreeNode():
    def __init__(self, data):
        self.__data = data
        
    def data(self):
        return self.__data
        
    def has_child(self, idx):
        pass
    
    def get_child(self, idx):
        pass
        

        

class DungeonStatusGame(TreeNode):
    def __init__(self, DungeonDataGame):
        pass
    
    def reset(self):
        pass
        
    def has_child(self, idx):
        pass
    
    def get_child(self, idx):
        pass


class TreePreorderVisiter():
    def __init__(self, start_node):
        self.start_node = start_node
        self.reset()
    
    def reset(self):
        self.cur_node = self.start_node
        self.saved_node_stack.clear()
        self.last_visited_child_index = 0
    
    # set current data to next data
    # return True if has next
    def next(self):
        pass
    
    def current_node(self):
        return self.cur_node
    
    
        
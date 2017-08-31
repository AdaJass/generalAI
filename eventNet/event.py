from general import database as db
from nueralNetwork import sceneseparator

class Event:
    def __init__(self):
        para = db.parameter.find_one({'name':'Ada'})
        self.timesires = para['timesires']
        db.parameter.update_one({'name':'Ada'},{"$inc":{"timesires": 1}})        
        self.scene_list = []  #this is a order list, it is time base order. 
        self.mood_list = []
        self.image_list = []
        """
            one element contains layout and concept, they are all output from ANN,
            this ANN try to make layout and concept to rebuild the orignal scene.
        """        
        pass    
    
    

    def addScene(self, raw_data):

        pass
    
    def _isEnd(self):
        """
        judge whether this event comes to an end.
        """
        pass
    def _evenSave(self):

        pass
    

    
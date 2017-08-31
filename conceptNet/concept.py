
from conceptNet import attribute as attr

class Basic_Concept:
    """it define concept base on attributes,
    which can link with other concepts.
    """
    def __init__(self, father=None, child=None, *attribs):
        
        pass

class Virtual_Concept:
    """this concept has no given body. sometimes means the scale too large,
    sometimes it can just learn from life exprience. for example, how to 
    descript 'None'? It will just a life experience. which comes from Event
    but not presented by event.
    """
    pass

class Emotion_Base_Concept:
    """ this kind of concept will almostly be predefine.
    """

    pass

class Event_Base_Concept:
    """ this concept will be, and only be created by learning
    and they are peresented by events.
    """

    pass



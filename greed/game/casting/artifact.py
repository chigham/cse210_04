from game.casting.actor import Actor
import random


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    It may be a gem (good) or a rock (bad).
    
    The artifact provides a point if it is a gem, 
    or takes away a point if it is a rock.

    Attributes:
        Inherits all attributes of actor.
        _type (string): It is either a gem or a rock.
        _value (int): +1 for a gem, -1 for a rock.
    """
    def __init__(self):
        super().__init__()
        #self._type = random.choice('gem', 'rock')
        self._value = 1

        """if self._type == 'gem':
            self._value = 1
        elif self._type == 'rock':
            self._value = -1"""
    
    def get_value(self):
        """Gets the artifact's value.
            
            Returns:
                int: The value(+1 or -1).
        """ 
        return self._value

    def set_value(self, new_value): # Mod ---
        """Updates the value to the given one.
        
        Args:
            new_value (int): The given value.
        """
        self._value = new_value

'''
from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def set_points(self, points):
        self.points = points
    
    def get_points(self):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        return self._points
    
 
'''
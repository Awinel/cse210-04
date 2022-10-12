from casting.actor import Actor

class Objects(Actor):
    """An object that will update the points when the robot touch it.

    The behavior of Objects is to update the points when the robot touch an object.
    
    Attributes:
        """
    
    def __init__(self):
        super().__init__()
        self._points: 0
    
    def get_points(self):
        if (self.get_text() == "*"):
            self._points = 50 
        elif (self.get_text() == "O"):
            self._points = -50

        return self._points
        
    def set_points(self, points):
        self._points = points

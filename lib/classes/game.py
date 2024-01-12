class Game:
    def __init__(self, title):

        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):

        return self._title
    
    @title.setter
    def title(self, title):

        if((isinstance(title, str)) and (0 < len(title)) and 
        not (hasattr(self, "title"))):
            self._title = title
        
        else:
            raise Exception("Invalid title or title was already made and can't be changed.")

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass
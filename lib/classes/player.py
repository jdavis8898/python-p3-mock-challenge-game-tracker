class Player:

    all = []

    def __init__(self, username):

        self.username = username
        self._results = []
        self._games_played = []
    
    @property
    def username(self):

        return self._username
    
    @username.setter
    def username(self, username):

        if((isinstance(username, str)) and (1 < len(username) < 17)):
            self._username = username
        
        else:
            raise Exception("That is not a valid username")

    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._result.append(new_result)

        return self._results # return a list of all the result

    def games_played(self, new_game=None):
        from classes.game import Game
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass
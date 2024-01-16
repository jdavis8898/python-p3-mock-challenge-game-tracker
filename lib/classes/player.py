class Player:

    all = []

    def __init__(self, username):

        self.username = username
        self._results = []
        self._games_played = []

        Player.all.append(self)
    
    @property
    def username(self):

        return self._username
    
    @username.setter
    def username(self, username):

        if isinstance(username, str) and 1 < len(username) < 17:
            self._username = username
        
        else:
            raise Exception("That is not a valid username")

    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)

        return self._results # return a list of all the result

    def games_played(self, new_game=None):
        from classes.game import Game
        
        if new_game and isinstance(new_game, Game) and new_game not in self._games_played:
            self._games_played.append(new_game)
        
        return self._games_played # return a list with all of the games

    def played_game(self, game):
        
        return game in self._games_played

    def num_times_played(self, game):
        
        return len([res for res in self._results if res.game == game])
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

class Result:

    all = []

    def __init__(self, player, game, score):
        
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
    
    @property
    def score(self):

        return self._score

    @score.setter
    def score(self, score):

        if((isinstance(score, int)) and (0 < score < 5001) and 
        not (hasattr(self, "score"))):
            self._score = score
        
        else:
            raise Exception("Invalid score or score was already made and can't be changed.")
    
    @property
    def player(self):

        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player

        if isinstance(player, Player):
            self._player = player
        
        else:
            raise Exception("Player must be of instance of Player class")
    
    @property
    def game(self):

        return self._game
    
    @game.setter
    def game(self, game):
        from classes.game import Game

        if isinstance(game, Game):
            self._game = game
        
        else:
            raise Exception("Game must be of instance of Game class")
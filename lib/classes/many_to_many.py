class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):

        if isinstance(value, str) and 0 < len(value) and not hasattr(self, "title"):
            self._title = value
        else:
            raise Exception

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        
        player_avgs = [result.score for result in self.results() if player == result.player]

        return sum(player_avgs)/len(player_avgs)

class Player:

    all = []

    def __init__(self, username):
        self.username = username

        Player.all.append(self)
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 1 < len(value) < 17:
            self._username = value
        else:
            raise Exception

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self): #gets unique list of games played by player
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        best_player = None
        highest_score = 0

        for player in cls.all:
            if player in game.players():
                if highest_score < game.average_score(player):
                    highest_score = game.average_score(player)
                    best_player = player

        return best_player

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, int) and 0 < value < 5001 and not hasattr(self, "score"):
            self._score = value
        else:
            raise Exception
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if isinstance(value, Player):
            self._player = value
        else:
            raise Exception
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if isinstance(value, Game):
            self._game = value
        else:
            raise Exception
    
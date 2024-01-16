class Result:

    all = []

    def __init__(self, player, game, score):
        
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

        Result.all.append(self)
    
    @property
    def score(self):

        return self._score

    @score.setter
    def score(self, score):

        if isinstance(score, int) and 0 < score < 5001 and not hasattr(self, "score"):
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
import ipdb

class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):

        return self._title
    
    @title.setter
    def title(self, title):

        if((isinstance(title, str)) and (len(title) > 0) and (hasattr(self, "title") == False)):
            self._title = title
        
        else:
            print("Invalid title or title was already made and can't be changed.")

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):

        return self._username
    
    @username.setter
    def username(self, username):

        if((isinstance(username, str)) and (1 < len(username) < 17)):
            self._username = username
        
        else:
            print("That is not a valid username")

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
    
    @property
    def score(self):

        return self._score

    @score.setter
    def score(self, score):

        if((isinstance(score, int)) and (0 < score < 5001) and (hasattr(self.score) == False)):
            self._score = score
        
        else:
            print("Invalid score or score was already made and can't be changed.")


# game = Game("Name of Game")
# ipdb.set_trace()
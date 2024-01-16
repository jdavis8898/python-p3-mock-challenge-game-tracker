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

        if isinstance(title, str) and 0 < len(title) and not hasattr(self, "title"):
            self._title = title
        
        else:
            raise Exception("Invalid title or title was already made and can't be changed.")

    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        
        return self._results

    def players(self, new_player=None):
        from classes.player import Player

        if new_player and isinstance(new_player, Player) and new_player not in self._players:
            self._players.append(new_player)
        
        return self._players
        

    def average_score(self, player):
        
        player_scores = [each_res.score for each_res in self._results if each_res.player == player]

        if player_scores:
            return sum(player_scores) / len(player_scores)
        
        else:
            return 0
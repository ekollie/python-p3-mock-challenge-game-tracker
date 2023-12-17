class Game:

    all = []

    def __init__(self, title=None):
        self.title = title
        Game.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) != str:
            raise Exception ("Title must be a string")
        elif len(title) < 1:
            raise Exception("Title must be longer than 0 characters")
        elif hasattr(self, "title"):
            raise Exception("Cannot change title")
        else: 
            self._title = title 

    def results(self):
        return [result for result in Result.all if result.game == self]
        pass

    def players(self):
        players = [result.player for result in self.results() if isinstance(result.player, Player)]
        players = list(set(players))
        print(players)

        return players

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores)/(len(scores))
        pass

    title = property(get_title, set_title)


class Player:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if type(username) != str:
            raise Exception("Username must be a string")
        elif len(username) < 2:
            raise Exception("Username too short")
        elif len(username) > 16:
            raise Exception("Username too long")
        
        else: self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games_played = [result.game for result in self.results() if isinstance(result.game, Game)]
        games_played = list(set(games_played))

        return games_played

    def played_game(self, game):
        return True if game in [result.game for result in self.results()] else False

    def num_times_played(self, game):
        return [game for game in [result.game for result in self.results() if type(result.game) == Game] if game == game].count(game) 


    username = property(get_username, set_username)


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score


    def get_score(self):
        return self._score

    def set_score(self, score):
        if type(score) != int:
            raise Exception("Score must be an integer")
        elif score < 1 or score > 5000:
            print("Score out of range")
        elif hasattr(self, "score"):
            raise Exception("Score cannot change after instantiation")
        else: 
            self._score = score
            Result.all.append(self)

    def get_player(self):
        return self._player
    
    def set_player(self, player):
        if type(player) != Player:
            raise Exception("player must be an instance of Player")
        
        else: self._player = player
        


    score = property(get_score, set_score)
    player = property(get_player, set_player)
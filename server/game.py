"""
Handles operations related to the game and connections
between, players, board, chat and round
"""
from .player import Player
from .board import Board
from .round import Round

class Game(object):

    def __init__(self, id, players, thread):
        """
        init the game! once the player thresold is met 
        :param id: int
        :param players: Player[]
        """
        self.id = id
        self.players = []
        self.words_used = []
        self.round = Round(self.get_word())
        self.board = Board()
        self.player_draw_ind = 0
        self.connected_threads = thread
        self.start_new_round() 

    def start_new_round(self):
        """
        Starts a new round with a new word
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()
    
    def create_board(self):
        """
        creates 
        """
        self.board = Board()
    
    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return bool
        """
        pass

    def player_disconnected(self, player):
        """
        Calls the cleanup object when the player disconnects
        :param player: Player
        :raises: Exception()
        """
        pass

    def skip(self):
        """
        Increments the round skips, if skips are greater than 
        threshold, start new round.
        :return: None  
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """
        self.skips = 0
        self.start_new_round()
        self.board.clear()

    def update_board(self ,x ,y ,color):
        """
        calls update method on board.
        :param x: int
        :param y: int
        :param color: 0-8
        :return: None
        """
        if not self.board:
            raise Exception(" No board created")
        self.board.update(x,y,color)

    def end_game(self):
        """
        ends the game
        :return:
        """
        # TODO Implement
        pass
    
    def get_word(self):
        """
        gives a word that has not been used
        :return: str
        """
        # todo get list of word from somewhere
        pass
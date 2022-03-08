class AddThreeGame:
    """Two players alternately choose numbers from 1-9. They may not choose a number that has already been selected by
    either player. If at any point exactly three of the player's numbers sum to exactly 15, then that player has won.
    If all numbers from 1-9 are chosen, but neither player  has won, then the game ends in a draw.
    Player "first" has the first turn."""

    def __init__(self):
        """Initialize data members."""
        self.__player_1 = 0
        self.__player_2 = 0
        self.__already_played = []
        self.__current_state = "UNFINISHED"

    def get_current_state(self):
        """Gets current state of game."""
        return self.__current_state

    def make_move(self, player, num_choice):
        """Takes in the player and their number choice and records their move."""
        if num_choice in self.__already_played:
            return False
        if num_choice > 9 or num_choice < 1:
            return False
        if player == "first":
            self.__player_1 = self.__player_1 + num_choice
            self.__already_played.append(num_choice)
        elif player == "second":
            self.__player_2 = self.__player_2 + num_choice
            self.__already_played.append(num_choice)
        if self.__player_1 == 15:
            self.__current_state = "FIRST_WON"
        elif self.__player_2 == 15:
            self.__current_state = "SECOND_WON"
        if len(self.__already_played) == 9:
            self.__current_state = "DRAW"
        return True

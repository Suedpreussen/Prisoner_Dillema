class Simplest_Dillemna:
    # possible outcomes
    both_cooperate_outcome = 5
    both_betray_outcome = -2
    betrayal_reward = 20
    betrayal_punishment = -10

    player_A_points = 100
    player_B_points = 100

    player_A_record = []
    player_B_record = []

    # possible moves for players
    def betray(self, player):
        append.player(1)

    def cooperate(self, player):
        append.player(0)

    def compare(self, round, player_A, player_B):
        if player_A(round) == 0 and player_B == 0:
            self.player_A_points += self.both_cooperate_outcome
            self.player_B_points += self.both_cooperate_outcome

        elif player_A(round) == 1 and player_B == 0:
            self.player_A_points += self.betrayal_reward
            self.player_B_points += self.betrayal_punishment

    def main_loop(self):
        while self.player_A_points <= 0 or self.player_B_points <= 0:
            pass
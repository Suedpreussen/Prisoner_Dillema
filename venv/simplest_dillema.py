import random

class SimplestDillemma:
    # possible outcomes
    both_cooperate_outcome = 1
    both_betray_outcome = -1
    betrayal_reward = 3
    betrayal_punishment = -3

    player_A_points = 10
    player_B_points = 10

    player_A_record = []
    player_B_record = []

    # possible moves for players
    def betray(self, player: list[int]):
        player.append(1)

    def cooperate(self, player: list[int]):
        player.append(0)

    def compare(self, round: int, player_A: list[int], player_B: list[int]):
        if player_A[round] == 0 and player_B[round] == 0:
            self.player_A_points += self.both_cooperate_outcome
            self.player_B_points += self.both_cooperate_outcome

        elif player_A[round] == 1 and player_B[round] == 0:
            self.player_A_points += self.betrayal_reward
            self.player_B_points += self.betrayal_punishment

        elif player_A[round] == 0 and player_B[round] == 1:
            self.player_A_points += self.betrayal_punishment
            self.player_B_points += self.betrayal_reward

        elif player_A[round] == 1 and player_B[round]  == 1:
            self.player_A_points += self.both_betray_outcome
            self.player_B_points += self.both_betray_outcome

    def main_loop(self):
        round = 0
        while self.player_A_points >= 0 and self.player_B_points >= 0 and round >= 0:
            probabilty = random.random()
            print(probabilty)
            if probabilty < 0.25:
                self.cooperate(self.player_A_record)
                self.cooperate(self.player_B_record)
                print(self.player_A_record)
                print(self.player_B_record)
            elif 0.25 < probabilty < 0.5:
                self.betray(self.player_A_record)
                self.cooperate(self.player_B_record)
                print(self.player_A_record)
                print(self.player_B_record)
            elif 0.5 < probabilty < 0.75:
                self.cooperate(self.player_A_record)
                self.betray(self.player_B_record)
                print(self.player_A_record)
                print(self.player_B_record)
            elif 0.75 < probabilty <= 1:
                self.betray(self.player_A_record)
                self.betray(self.player_B_record)
                print(self.player_A_record)
                print(self.player_B_record)

            self.compare(round, self.player_A_record, self.player_B_record)
            print('round: ', round + 1)
            print('points for A: ', self.player_A_points)
            print('points for B: ', self.player_B_points)
            print('____________________________________________')
            round += 1


my_dillemma = SimplestDillemma()
my_dillemma.main_loop()

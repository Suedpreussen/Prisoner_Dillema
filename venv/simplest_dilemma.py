import random


class SimplestDilemma:
    """Simple implementation of the prisoner dilemma

    __init__ initialises two players and system of rewards.
    betray and cooperate records which move did a player choose.
    compare assigns points of reward or punishment according to the moves of both players.
    main_loop runs the simulation, the moves of the players are randomly chosen,
    there is 1/4 chances that one of the four possibles outcomes.
    create_log sums up the game that has been played
    """
    def __init__(self, both_cooperate_outcome, both_betray_outcome, betrayal_reward, betrayal_punishment, initial_points):
        # possible outcomes
        self.both_cooperate_outcome = both_cooperate_outcome
        self.both_betray_outcome = both_betray_outcome
        self.betrayal_reward = betrayal_reward
        self.betrayal_punishment = betrayal_punishment

        # handing out initial points
        self.player_A_points = initial_points
        self.player_B_points = initial_points

        # delcaring record of betrayals and coops
        self.player_A_record = []
        self.player_B_record = []

        self.game_state_count = [0, 0, 0, 0]
        self.rounds = 0

    # two possible moves for players
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

        elif player_A[round] == 1 and player_B[round] == 1:
            self.player_A_points += self.both_betray_outcome
            self.player_B_points += self.both_betray_outcome


    def main_loop(self, when_to_end):
        while self.player_A_points >= 0 and self.player_B_points >= 0 and self.rounds <= when_to_end:
            probability = random.random()
            if probability < 0.25:
                self.cooperate(self.player_A_record)
                self.cooperate(self.player_B_record)
                self.game_state_count[0] += 1

            elif 0.25 < probability < 0.5:
                self.betray(self.player_A_record)
                self.cooperate(self.player_B_record)
                self.game_state_count[1] += 1

            elif 0.5 < probability < 0.75:
                self.cooperate(self.player_A_record)
                self.betray(self.player_B_record)
                self.game_state_count[2] += 1

            elif 0.75 < probability <= 1:
                self.betray(self.player_A_record)
                self.betray(self.player_B_record)
                self.game_state_count[3] += 1


            self.compare(self.rounds, self.player_A_record, self.player_B_record)
            """
            print('round: ', round + 1)
            print('points for A: ', self.player_A_points)
            print('points for B: ', self.player_B_points)
            print('____________________________________________')
            """
            self.rounds += 1

    def create_log(self):
        beatrayal_count_A = sum(self.player_A_record)
        beatrayal_count_B = sum(self.player_B_record)
        both_cooperate, A_betrays, B_betrays, both_betray = self.game_state_count
        print('number of states occurred; \n both_cooperate, A_betrays, B_betrays, both_betray:', *self.game_state_count)
        print('number of A betrayal: ', beatrayal_count_A)
        print('number of B betrayal: ', beatrayal_count_B)
        print('final points for A: ', self.player_A_points)
        print('final points for B: ', self.player_B_points)
        print('number of rounds: ', self.rounds)


my_dilemma = SimplestDilemma(1, -1, 3, -3, 10)
my_dilemma.main_loop(100)
my_dilemma.create_log()

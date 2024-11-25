import random

class RockPaperScissorsGame:
    def __init__(self):
        # agent와 robot의 초기 점수 10점
        self.agent_score = 10
        self.robot_score = 10
        self.choices = ["rock", "paper", "scissors"]
    # 게임 로직
    def play_round(self, agent_choice, robot_choice):
        """가위바위보의 승자를 결정하고 점수를 업데이트"""
        print(f"Agent chose {agent_choice}, Robot chose {robot_choice}")
        
        # 승리 조건
        if agent_choice == robot_choice:
            print("It's a tie!")    # 무승부!
        elif (  # agent 승리(robot 패배)
            (agent_choice == "rock" and robot_choice == "scissors") or
            (agent_choice == "paper" and robot_choice == "rock") or
            (agent_choice == "scissors" and robot_choice == "paper")
        ):
            print("Agent wins this round!")
            self.agent_score += 1
            self.robot_score -= 1
        else:   # agent 패배(robot 승리)
            print("Robot wins this round!")
            self.agent_score -= 1
            self.robot_score += 1

        print(f"Scores -> Agent: {self.agent_score}, Robot: {self.robot_score}\n")

    def is_game_over(self):
        """점수가 0점에 도달한 플레이어 확인"""
        return self.agent_score <= 0 or self.robot_score <= 0

    def play_game(self):
        """게임 실행"""
        print("Starting Rock-Paper-Scissors Game!")
        while not self.is_game_over():
            # 에이전트의 선택 (사용자로부터 입력)
            agent_choice = input("Choose rock, paper, or scissors: ").lower()
            while agent_choice not in self.choices:
                print("Invalid choice! Please choose again.")
                agent_choice = input("Choose rock, paper, or scissors: ").lower()

            # 로봇의 선택 (랜덤)
            robot_choice = random.choice(self.choices)

            # 라운드 실행
            self.play_round(agent_choice, robot_choice)

        # 게임 종료 메시지
        if self.agent_score <= 0:
            print("Agent lost all points. Robot wins the game!")
        else:
            print("Robot lost all points. Agent wins the game!")

# 게임 시작
game = RockPaperScissorsGame()
game.play_game()
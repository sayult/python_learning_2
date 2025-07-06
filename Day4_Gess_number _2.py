import random
from number_game import guess_number_game

total_games = 0
win_games = 0

while True:
    total_games += 1
    if guess_number_game():
        win_games += 1

        print(f'当前成绩{win_games}胜/{total_games - win_games}负.')

        play_again = input('再玩一次？（Y/N）：')
        if play_again.lower() != 'y':
            print('游戏结束！')
        
            break
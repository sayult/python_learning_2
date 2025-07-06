import random


def get_uesr_input(attempt_count):  #输入检查函数
    while True:
        try:
            guess = int(input(f'第{attempt_count + 1}次猜数。'))
            if 1<= guess <= 100:
                return guess
            else:
                print('请输入1-100间的整数！')
        except ValueError:
            print('请输入1-100间的整数！')

        
    
    
def guess_number_game():   #游戏主函数

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print('*******猜数字游戏*******')
    print(f'在1-100里面猜一个数字，你有{max_attempts}次机会。')

    while attempts <= max_attempts:
        guess = 

def check_guess(guess, secret):    #比较函数
    if guess == secret:
        return True
    elif guess <= secret:
        print('太小了！')
    else:
        print('太大了！')
    return False
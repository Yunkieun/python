# 가위바위보 게임

import random

print("가위바위보 게임")
가위바위보 = ['가위', '바위', '보']

result = {0: '무승부', 1:'패', 2:'승'}
state = 0

you = input('당신 : ')

com = random.choice(가위바위보)
print("컴퓨터 :", com)

def play(you, com):
    if you not in 가위바위보:
        print("잘못된 입력")
        return

    if you == com:
        state = 0
    elif you == "가위" and com == "보":
        state = 2
    elif you == "바위" and com == "가위":
        state = 2
    elif you == "보" and com == "바위":
        state = 2
    elif you == "가위" and com == "바위":
        state = 1
    elif you == "바위" and com == "보":
        state = 1
    elif you == "보" and com == "가위":
        state = 1

    print("결과 : ", result[state])

play(you, com)

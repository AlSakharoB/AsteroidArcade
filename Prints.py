def PrintScore(score):
    print("YOUR SCORE:" + "\n" + "➤ " + str(score) + " m")
    print("-" * (5 + len(str(score))))


def PrintRules():
    print("RULES ARE:")
    print("RUS:")
    print("\tПривет, юный космонавт, это твоя очередная миссия по изучению космоса. Попробуй исследовать как можно"
          " больше\n\tкосмического пространства, но остерегайся астероидов, которые будут встречаться тебя на пути."
          "\n\tКстати, у вашего экипажа, по-моему, отказали реактивные тормоза, поэтому вы будете набирать скорость.")
    print("ENG:")
    print("\tHi there, buddy, that's your next space exploration mission. Try your best and explore as much space"
          "\n\touter as possible, but beware of asteroids that can damage yor spaceship on the way."
          "\n\tBy the way, your team got a problem with jet brakes so you will pick up speed.")
    print("----------------------------------------------------------------------------------")

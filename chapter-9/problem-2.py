import random 

def game():
    print("You are playing the game")
    score = random.randint(1,63)
    with open("code-with-harry/chapter-9/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your Score : {score}")
    if(score>hiscore or hiscore == ""):
        with open("code-with-harry/chapter-9/hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()
#Name: Elijah Allen-Straton
#Prog: Magic 8-Ball

import random
answers_8_ball = ( "As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now",
                   "Concentrate and ask again", "Dont count on it", "It is certain", "It is decidedly so",
                   "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good",
                   "Reply hazy try again", "Signs point to yes", "Very Doubtful", "Without a doubt", "Yes",
                   "Yes definitely", "You may rely on it", )

def main():
    print("I am the MAGIC-8 BALL")

    other_question = True
    while other_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC-8 BALL")
        print("\n...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("The MAGIC-8 BALL says: " + answer)

        askAgain = input("\nWould you like to ask me another question? (Y or N): ")
        if askAgain.upper() == "N" or askAgain == "n":
            other_question = False

    print("\nCome back soon with more questions.")

main()
        
    

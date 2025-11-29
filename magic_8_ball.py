import random

print ("Welcome to Magic 8 Ball, Let me tell your future!")
print()


answers_affirmative = ["Yes", "Signs point to yes", "It is certain", "Without a doubt", "Yes, definitely", "Outlook good", "You may rely on it", "As I see it, yes", "Most likely", "It is decidedly so"]

answers_negative = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

answers_neutral = ["Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannont predict now", "Concentrate and ask again"]

choices = answers_affirmative + answers_negative + answers_neutral

computer_answer = random.choice(choices)

#split answers into two different groups
bad_answer = answers_neutral
good_answer = answers_affirmative + answers_negative

#use while loop to make computer ask question again if answer is neutral
while True:
  player_question = input("Shake the Magic 8 Ball!").lower().strip()
  # add computer_answer random generator again inside loop so it will randomize after the first question.
  computer_answer = random.choice(choices)
  print()
  print (computer_answer)
  print()
  
  if computer_answer in bad_answer:
    print ("Ask your question again!")
    
     
  elif computer_answer in good_answer:
    print ("Thank you for playing! Hope you got the answer you were looking for!")
    break

#use break to make sure loop ends
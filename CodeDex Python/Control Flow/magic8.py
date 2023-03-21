#magic8.py

#uses random library to help generate values for 8 ball questions

import random

question = input('Question:      ')
answerNum = random.randint(1,9)
answer = ''

if answerNum == 1:
    answer = 'Yes - definitely.'

elif answerNum == 2:
    answer = 'It is decidedly so.'

elif answerNum == 3:
    answer = 'Without a doubt.'

elif answerNum == 4:
    answer = 'Reply hazy, try again.'

elif answerNum == 5:
    answer = 'Ask again later.'

elif answerNum == 6:
    answer = 'Better not tell you now.'

elif answerNum == 7:
    answer = 'My sources say no.'

elif answerNum == 8:
    answer = 'Outlook not so good.'

else:
    answer = 'Very doubtful.'

print('Magic 8 Ball:  ' + answer)
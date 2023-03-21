#word_counter.py

#Project 16 of 50. Counts the amount of words in a given text. Terminal Only Text

response = True

while(response):
    print("Please Insert Text To Count:")
    text_to_count = input()
    counter = 0

    for i in range(len(text_to_count)):
        if (text_to_count[i] == ' ' and text_to_count[i-1].isalpha()) or (i == len(text_to_count) - 1 and text_to_count[-1].isalpha()):
            counter += 1

    if counter == 1:
        print(f'Word Counter: {counter} word')
    else:
        print(f'Word Counter: {counter} words')

    response = input('Would you like to perform this action again(Y/N)?').upper().strip() == 'Y'

print('Thank You for using my word counter! Hope to see you again!')
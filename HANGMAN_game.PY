import random
import hangman_stages
word=['apples','butter','orange']
lives=6
choosen_option=random.choice(word)
#print(choosen_option)
display=[]
for i in range(len(choosen_option)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guess = input('guess the letter').lower()
    for position in range(len(choosen_option)):
        letter=choosen_option[position]
        if letter == guess:
            display[position]=guess
    print(display)
    if guess not in choosen_option:
        lives -= 1
        if lives==0:
            game_over=True
            print('you lost')
    if '_' not in display:
        game_over=True
        print('you win')
    print(hangman_stages.stages[lives])

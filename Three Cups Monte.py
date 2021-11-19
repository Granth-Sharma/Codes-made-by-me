print('How to play this game:')
print("You must have heard about the game in which we have 3 cups and there is ball in one of them and we have to choose the   correct cup with the ball to win.")
print("We have to do the same thing here. You have three cups shuffled randomly every round and you have to guess in which cup  the ball is.")

from random import shuffle
mylist=[' ','O',' ']
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
def player_guess():
    guess=''
    while guess not in ['1','2','3']:
        guess=input("Pick a number:1,2 or 3. Your answered:")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)
mylist=[' ','O',' ']
mixedup_list=shuffle_list(mylist)
guess=player_guess()
check_guess(mixedup_list,guess)
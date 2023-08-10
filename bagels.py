import random

NUM_DIGITS = 3  # CHANGE
MAX_GUESSES = 2 # CHANGE

def main():
    print('Bagels Guessing Game')
    print(''' I am thinking of {}-digit number with no repeated digit
          Try to guess what it is. Here are some clues:
When I say: That means:
Pico:   One digit is correct but in the wrong position.
Fermi:  One digit is correct and in the right position.
Bagels: No digit is correct.
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(MAX_GUESSES))
    
    while True: #Main loop
        secretNum = getSecretNum() #stores the secret number
        print('I have thought of a number')
        print('You have {} tries'.format(MAX_GUESSES))

        numGuesses =1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looking until valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess # {}'.format(numGuesses))
                guess = input('>')

            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #Correct guess so break out of the loop
            if numGuesses > MAX_GUESSES:
                print("No more guesses")
                print('The answer is {}'.format(secretNum))

        #try again
        print('Do you want to play again?(y or n)')
        if not input('>').lower().startswith('y'):
            break
    print("Thanks for playing!")

def getSecretNum(): #Returns string of random digits
    numbers = list('0123456789') #Create a list of numbers 0 to 9
    random.shuffle(numbers) #Shuffle into random order
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

            
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range (len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()





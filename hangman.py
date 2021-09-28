import random 

def get_word():
    word_list=['marble','talk','transfer','computer','science','impulse',
    'lion','tiger','wares','soup','india','country','mount','extend','work',
    'python','program','water','milk','secret','apple','strawberry', 'orange',
    'grape', 'pineapple', 'apricot','lemon', 'coconut', 'watermelon', 'cherry', 
    'papaya', 'berry', 'peach', 'lychee', 'muskmelon','encourage']
    word=random.choice(word_list)
    return word.upper()


def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=9
    print("lets play")
    print(display_hangman(tries))  
    print(word_completion)
    while not guessed and tries>0:
        guess=input("Please guess a letter:").upper()
        if len(guess)==1 and guess.isalpha():
              if guess in guessed_letters:
                  print("You already guessed the letter",guess)
              elif guess not in word:
                  print(guess, "is not in the word")    
                  tries-=1
                  guessed_letters.append(guess)
              else:
                  print("Good Job!", guess, "is in the word")
                  guessed_letters.append(guess)
                  word_as_list=list(word_completion)  
                  indices=[i for i, letter in enumerate(word) if letter == guess]
                  for index in indices:
                      word_as_list[index]=guess 
                  word_completion="".join(word_as_list)
                  if "_" not in word_completion:
                      guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word",guess)
            elif guess!=word:
                print(guess, "is not the word")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_completion=word
    
        else:
            print("not valid")
        print(display_hangman(tries))
        print(word_completion)
        print("\n") 
    if guessed:  
        print("Congrats!🤩 You Won")
    else:
        print("Oops!🙁 You Lost.\n The word was " +word)  

def display_hangman(tries):
    stages=[ """
             --------
             |      |
             |      o
             |     \|/
             |      |
             |      |
             |     /|\\
             """,
             """
             --------
             |      |
             |      o
             |     \|/
             |      |
             |      |
             |     /|
             """,
             """
             --------
             |      |
             |      o
             |     \|/
             |      |
             |      |
             |      |
             """,
             """
             --------
             |      |
             |      o
             |     \|/
             |      |
             |      |
             |     
             """,
             """
             --------
             |      |
             |      o
             |     \|/
             |      |
             |      
             |   
             """,
             """
             --------
             |      |
             |      o
             |     \|/
             |      
             |      
             |     
             """,
             """
             --------
             |      |
             |      o
             |     \|
             |      
             |      
             |     
             """,
             """
             --------
             |      |
             |      o
             |      |
             |      
             |      
             |     
             """,
             """
             --------
             |      |
             |      o
             |     
             |      
             |      
             |     
             """,
             """
             --------
             |      |
             |      
             |     
             |      
             |      
             |     
             """
             ] 
    return stages[tries]

def main():
    word=get_word()
    play(word)  
    while input("Do you want to Play Again? (y/n)").upper()=="Y": 
        word=get_word()
        play(word)


if __name__=="__main__":
   main()                     


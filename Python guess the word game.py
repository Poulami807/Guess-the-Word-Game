
import random

print("\t\t\t\tWelcome to Guess the Word Game!\t\t\t\t")
print("INSTRUCTIONS:")
print("1.You need to enter any single random alphabet at each turn\n2.If the entered letter is present in the word it will be displayed else a message will be displayed.\n3.The number of wrong attempts to guess the word will vary according to the level you choose.")
print("START")
print("1.EASY(24 wrong attempts)")
print("2.INTERMEDIATE(12 wrong attempts)")
print("3.HARD(8 wrong attempts)")
level=input("Enter the level you want to play: ")
if level=='1':
    attempts=24
    min_length=4
if level=='2':
    attempts=12
    min_length=6
if level=='3':
    attempts=8
    min_length=8

wordlist="words.txt"

#function to randomly select a word
def get_word(min):
    file=open(wordlist,"r")
    content=file.read()
    words=content.split("\n")
    curr_word=((random.choice([w for w in words if len(w)>min])).strip()).lower()
    return curr_word

#Checking if the letter entered is present in the word
def check(ch,word):
    index=[]
    for i in range(len(word)):
        if ch==word[i]:
            index.append(i)
    return index
        
#Checking user enters a sinle alphabet at a time
def single_letter(ch):
    if len(ch)==1:
        return True
    else:
        return False

def play(attempts):
    wrd=get_word(min_length)
    hidden_wrd="*"*len(wrd)
    print("Guess the word:",hidden_wrd)
    flag=0
    count=0
    new_word=hidden_wrd
    condition=True
    match=0
    while(condition):
        ch=input("Enter an alphabet: ")
        res=single_letter(ch)
        if res==False:
           print("Only single letter guesses allowed!")
           continue
        else:
            indices=check(ch,wrd)
            if indices:
                flag=len(indices)
                for i in indices:
                    new_word=new_word[:i]+wrd[i]+new_word[i+1:]
                print(f"The word is: {new_word}")
            else:
               count+=1
               print("Sorry!Wrong Guess")
               print(f"You have {attempts-count} attempts left")
                        
            match+=flag
            flag=0
        if match==len(wrd):
            print("Congratulations!You won")
            condition=False
        if  attempts==count:
            print(f"Sorry!No more attempts lefts!\nThe correct word was: {wrd}")
            condition=False
            
play(attempts)



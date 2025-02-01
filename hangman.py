import random
def x():
    words="python,java,c++,c,go,ruby,django,html,css,javascript"
    words=words.split(",")
    word=random.choice(words)
    return word
def y(word):
    a="_"*len(word)
    b=[]
    c=len(word)+3
    d=0
    print("NUMBER OF CHANCES YOU GET ARE: ",c)
    print("LET'S START THE GAME")
    print(a)
    while c>0:
        print("\nCURRENT WORD: "," ".join(a))
        e=input("PLEASE ENTER A LETTER YOU GUESSED: ").lower()
        if e.isalpha():
            if e in b:
                print("YOU'VE ALREADY GUESSED THE LETTER",e)
            elif e not in word:
                print(e,"IS NOT IN THE WORD")
                c=c-1
            else:
                print("YOU'VE GUESSED CORRECT LETTER")
                b.append(e)
                a="".join([e if word[i]==e else a[i] for i in range(len(word))])
        elif not e.isalpha():
            print("PLEASE ENTER A VALID GUESS")  
            c=c-1
        elif len(e)>1:
            print("PLEASE ENTER ONLY ONE LETTER") 
            c=c-1 
        if "_" not in a:
            print("YOU WON!YOU'VE GUESSED THE WORD: ",word)
            break         
    if c==0 and "_" in a:
        print("YOU LOST!THE WORD WAS: ",word)
word_to_guess = x()
y(word_to_guess)                          


    


     
    
    
    


    



    
    
            

    
    





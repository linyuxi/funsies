
# coding: utf-8

# In[1]:

#this is a simple pig Latin translator
print ("This is a simple Pig Latin word converter.")

def pig_latin():
    original = input("Enter a word: ")

    if original.isalpha() and len(original) > 0:
        first = original[0]
        pig = 'ay'
        second = original[1:len(original)]
        pig_word = second + first + pig
        print ("Pig Latin: " + pig_word)
        
        def pig_latin2():
            new_word = input("Would you like to enter another word (Y/N)? ")

            if new_word.lower() == "y":
                return pig_latin()

            elif new_word.lower() == "n":
                print ("Thanks for participating!")

            else:
                print ("Invalid input.")
                return pig_latin2()
        
        pig_latin2()
        
    elif len(original) == 0:
        print ("Please enter a word.")
        return pig_latin()
    
    elif not original.isalpha() and len(original) > 0:
        print ("No numbers or spaces please!")
        return pig_latin()
    
    else:
        print ("Invalid input.")
        return pig_latin()

pig_latin()


# In[ ]:




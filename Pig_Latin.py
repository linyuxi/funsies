
# coding: utf-8

# In[1]:

#this is a simple pig Latin translator
print ("This is a simple Pig Latin word converter.")

def pig_latin():
    original = input("Enter a word: ")

    two_consonant_cluster= ['th', 'ph', 'pr', 'pl', 'st', 'sh','sr','tr','ch','pt']
    three_consonant_cluster= ['thl','thr','phl','pth','str','stl','sch','shr','shl']
    four_consonant_cluster= ['phth','schr','schl','shch']
    #single syllable vowel cluster
    two_vowel_cluster = ['ae','ao','au','ai','ay','ea','ei','ey','eo','eu','ee','ie','oo','oe','oi','ou','ue','ui'] 
    three_vowel_cluster = ['eye','eau','aou'] #this is why coming up with a rule to just check for clusters would be so much easier

    if original.isalpha() and len(original) > 0:
        if original[0:4] in four_consonant_cluster:
            first = original[0:4]
        elif original[0:3] in three_consonant_cluster or three_vowel_cluster:
            first = original[0:3]
        elif original[0:2] in two_consonant_cluster or two_vowel_cluster:
            first = original[0:2]
        else:
            first = original[0]
        pig = 'ay'
        second = original[len(first):len(original)]
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




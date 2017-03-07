
# coding: utf-8

# In[1]:

def sessions():
    num_participants = input("Enter number of participants: ")
    max_participants_per_session = input("Enter number of participants per session: ")
    num_p = int(num_participants)
    max_p = int(max_participants_per_session)
    max_sessions = (num_p - 1) // max_p + 1
    print ("Number of sessions required:", max_sessions)
   
    if num_p % max_p == 0:
        print ("No spots available")
    else:
        more_participants = max_p - (num_p % max_p)
        print ("Number of available spots before another new session is required:", more_participants)

sessions()


# In[ ]:




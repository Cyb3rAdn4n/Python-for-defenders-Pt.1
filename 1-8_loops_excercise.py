 
from testme import cred_dump, authenticate, testme_1, testme_2


# intiated empty lists required
valid_users: list = []
authenticated_users: list = []

#this one I initiated by myself to check which users are not in the list
unknown_users: list = []

# This is to loop through ranges in 0, length of cred_dump
for c in range(0,(len(cred_dump)-1)):
    result_auth : list = [] # this is to store the output that I can put in if else to set up conditions and put the result in required list, this would become 0 every time the loop runs
    result_auth = authenticate(cred_dump[c][0], cred_dump[c][1])   # this is to put username and password in the authenticate() function

    
    # for this I used the index 1 of the result which would contain the string if user is present, authencitaed or not valid user.
    if result_auth[1] == "":
        authenticated_users.append(cred_dump[c][0])
        valid_users.append(cred_dump[c][0])
    elif result_auth[1] == "Password is incorrect":
        valid_users.append(cred_dump[c][0])
    else:
        unknown_users.append(cred_dump[c][0])
        
testme_1(valid_users)
testme_2(authenticated_users)
#print(valid_users[18])
#print(authenticated_users[0])
#print(unknown_users[23])

#print(cred_dump[65])
#print(cred_dump[65][0], cred_dump[65][1])

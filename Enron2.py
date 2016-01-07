'''

learning objectives: to see how i developed code step by step
removing \n \t etc


Start with allen p inbox, move to others

Why is None in list??
'''




from email.parser import Parser
import os
import re
from collections import Counter
import pdb

# In[3]:

#cd "C:\Users\Shantnu\Desktop\Data Sources\maildir"


# In[6]:
'''
rootDir = '.'
count = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        count += 1

print("Number of files = ", count)        
'''

# In[7]:

def email_count(input_file, to_email_list, from_email_list, email_body):
    with open(input_file, "r") as f:
        email_data = f.read()
    #if input_file == 'C:\\Users\\Shantnu\\Desktop\\Data Sources\\maildir\\allen-p\\inbox\\13':
    #pdb.set_trace()
    #print("File name = ", input_file)
    email = Parser().parsestr(email_data)

    if email['to']:
        to_email = email['to'].replace("\n", "")
        to_email = to_email.replace("\t", "")
        to_email = to_email.replace(" ", "")
        to_email = to_email.split(",")

        for email1 in to_email:
            if email1 == None:
                pdb.set_trace()
            to_email_list.append(email1)
            #print(email1)
        #print("To: ", to_email)
        #print("\n-----\n")
    #print("From: ", email['from'])
    #print("\n-----\n")
    #pdb.set_trace()
    from_email_list.append(email['from'])
    #email_body.append(email.get_payload())
    
    


# In[ ]:

to_email_list = []
from_email_list = []

rootDir = 'C:\\Users\\Shantnu\\Desktop\\Data Sources\\maildir\\'
count = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        email_body = []
        email_count(os.path.join(dirName, filename), to_email_list, from_email_list, email_body)
        #print (str(count)+" ", end="")
        count += 1
        #with open("email_text.txt", "a") as f:
        #    f.write("\n".join(email_body))

#pdb.set_trace()
#print("\n\nTop To email addresses: \n ")        
#print(Counter(to_email_list).most_common(5))
with open("to_email_text.txt", "a") as f:
    for email2 in to_email_list:
        #print(email2)
        if email2:
            f.write(email2)
            f.write("\n")

#print("\n\nTop Fm email addresses: \n ")        
#print(Counter(from_email_list))
print("To: ")
print(Counter(to_email_list).most_common(10))
print("\n\n")
print("From: ")
print(Counter(from_email_list).most_common(10))

with open("from_email_text.txt", "a") as f:
    for l in from_email_list:
        f.write(l)
        f.write("\n")

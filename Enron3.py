import os
from email.parser import Parser
rootdir = "C:\\Users\\Shantnu\\Desktop\\Data Sources\\maildir\\lay-k\\family"


def email_analyse(inputfile, to_email_list, from_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)

    to_email_list.append(email['to'])
    from_email_list.append(email['from'])

    email_body.append(email.get_payload())


to_email_list = []
from_email_list = []
email_body = []

for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )


with open("to_email_list.txt", "w") as f:
    for to_email in to_email_list:
        if to_email:
            f.write(to_email)
            f.write("\n")

with open("from_email_list.txt", "w") as f:
    for from_email in from_email_list:
        if from_email:
            f.write(from_email)
            f.write("\n")        

with open("email_body.txt", "w") as f:
    for email_bod in email_body:
        if email_bod:
            f.write(email_bod)
            f.write("\n")     
   
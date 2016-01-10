from email.parser import Parser

file_to_read = "C:\\Users\\Shantnu\\Desktop\\Data Sources\\maildir\\lay-k\\all_documents\\1"

with open(file_to_read, "r") as f:
    data = f.read()

#print(data)

email = Parser().parsestr(data)

print("\nTo: " , email['to'])
print("\n From: " , email['from'])

print("\n Subject: " , email['subject'])

print("\n \n Body: " , email.get_payload())

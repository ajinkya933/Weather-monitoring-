email = []

email_file = open('emails.txt', 'r')

for line in email_file:
    (email, name) = line.split(',')

print(email)
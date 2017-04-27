email = []

email_file = open('emails.txt', 'r')

for line in email_file:

    email.append(line.strip())      # removing the new line between two emails

print(email)

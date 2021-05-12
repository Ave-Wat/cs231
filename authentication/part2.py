"""466192417

real    7m43.715s
user    7m43.586s
sys     0m0.010s"""

import hashlib

words = [line.strip().lower() for line in open('words.txt')]
md5_passwords = {}

for line in open('p2.txt'):
    line = line.strip().lower()
    line_list = line.split(":")
    hash_list = line_list[1].split("$")
    salt = hash_list[0]
    password = hash_list[1]
    user = line_list[0]
    md5_passwords[password] = {'user':user, 'salt':salt}

cracked_passwords = {}
hash_count = 0

for passwd in md5_passwords:
    for word in words:
        salted_word = md5_passwords[passwd]['salt'] + word
        encoded_word = hashlib.md5(salted_word.encode())
        hash_count = hash_count + 1
        if encoded_word.hexdigest() == passwd:
            cracked_passwords[word] = md5_passwords[passwd]
            break

print(hash_count)

with open('passwords2.txt', 'w') as file:
    for passwd in cracked_passwords.keys():
        file.write("%s:%s\n"%(cracked_passwords[passwd]['user'], passwd))
file.close

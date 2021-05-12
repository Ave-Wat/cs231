import hashlib

words = [line.strip().lower() for line in open('words.txt')]
passwords1 = {}

for line in open('p1.txt'):
    line = line.strip().lower()
    line_list = line.split(":")
    passwd = line_list[1]
    user = line_list[0]
    passwords1[passwd] = user

correct = {}

for passwd in passwords1:
    for word in words:
        encoded_word = hashlib.md5(word.encode())
        if encoded_word.hexdigest() == passwd:
                correct[word] = passwords1[passwd]
                print(word + ", " + correct[word])
                break
        """else:
            for word2 in words:
                word_1_2 = word + word2
                word_2_1 = word2 + word
                encoded_word_1_2 = hashlib.md5(word_1_2.encode())
                encoded_word_2_1 = hashlib.md5(word_2_1.encode())
                if encoded_word_1_2.hexdigest() == passwd:
                    correct[(word + word2)] = passwords1[passwd]
                    print(word + word2 + ", " + correct[(word + word2)])
                    break
                elif encoded_word_2_1.hexdigest() == passwd:
                    correct[(word2 + word)] = passwords1[passwd]
                    print(word2 + word + ", " + correct[(word2 + word)])
                    break"""
print(correct)
with open('correct.txt', 'w') as file:
    for key in correct.keys():
        file.write("%s:%s\n"%(correct[key], key))
file.close

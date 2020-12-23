'''
Idea From:
http://www.edureka.co/blog/ethical-hacking-using-python/
https://www.pythonpool.com/python-hashlib/
'''
'''
Update()– The string that you want to encrypt should be used as the argument in update function.  
encode()– update() function requires encoded string, so we first need to apply encode() on the string, otherwise we will get ‘typeerror unicode objects must be encoded before hashing python hashlib‘.
hexdigest()– This function is used to get the encrypted string. We can also use the digest(), but that does not give us a clean output.  
'''

import hashlib

flag = 0

pass_hash = input("md5 hash: ")

wordlist = input("File name: ")
try:
    pass_file = open(wordlist,"r")
except:
    print("No file found :(")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')

    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest.strip() == pass_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
if flag == 0:
    print("password not in list")




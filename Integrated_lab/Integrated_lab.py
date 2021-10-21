#This script is made for encrypting data using a private key.
import subprocess
import sys
from crypt.Hash import SHA256
subprocess.check_call([sys.executable, '-m', 'pip','install','redis'])





def Encryption():
    hash = new SHA256.new()
    hash.update("message")
    hash.digest()
    print("Test3")



print("Test 1")
Encryption()
print("Test 3")


#https://pypi.org/project/pycrypto/
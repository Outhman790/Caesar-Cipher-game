from logo import Logo
from functions import *
isGameFinished = False

while isGameFinished == False:
    print(Logo)
    encode_or_decode = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n").lower()
    ceaserCipher(encode_or_decode,isGameFinished)
       
   

  



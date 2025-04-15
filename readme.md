*******************************************
Thanks for showing interest in Crypt0tape!
*******************************************

This is a Mini Suite of tools that you can use to encrypt a .txt file. 
It is based on One Time Pad (OTP), an algoritm that requires a key as long as the message. It's the only encryption algoritm considered inviolable, but of course everything depends on how random the key is. For furher information you can check it on wikipedia https://en.wikipedia.org/wiki/One-time_pad?wprov=sfti1

NOTE: in this file i'm talking about what is behind the tools, if you just don't care you can execute the python file in terminal (python3 crypt0tape) and a short help message will teach you briefly how to use all of the tools

--------------------------------------------------------------------------------------------------------------------------------------------------------
This suite comes out with 4 tools: encrypt, decrypt, generate key, shred.
Now follows an explaination of every tool
1. Encrypt: It encrypts a .txt file with a key.bin file given by the user.The encryption works by executing a XOR operation between every nth byte of the key and nth byte of the message, so it is really important for the key to be as long as the message. after this operation the result is put in a .bin file, where all of the bytes are changed
2. Decrypt: it basically does the same but reversed thing of the encryption tool. it takes as input the encrypted.bin file and the same key.bin used for encryption. You get as output the same exact .txt file you encrypted
3. Generate-key: this tool uses the python library secret to generate a pseudo-random string of bytes. The user can choose how long the string should be and the program will output a key.bin file. Even though it is pseudo-random (it's impossible for a computer to generate a random string) this string will not follow any model or scheme. Python's library, secret, is well known for generating numbers with an high rate of randomnacy
4. Shred: it is a tool used to destroy safely a bin file. It is safe for most users because it overwrites every byte of the file with a random generated ones. After that it automatically deletes the file. This tool is important because every used key should be deleted in a safe way right after the use. Please note that this tool alone isn't 100% safe against adavanced forense recovery methods, if you really want to be safe in that scenarios you should also encrypt your storage drive.
Now that you know how the tools work you can just execute the program as i said before, you will understand the sintax of the tools
----------------------------------------------------------------------------------------------------------------------------

DISCLAIMER: This is just a coding excercise done by me, dav_nr, the developer of these tools. I don't take any responsibility for any use made against the laws by the users
 
THANK YOU FOR YOUR ATTENTION AND STAY ALWAYS SAFE,
Dav_nr.

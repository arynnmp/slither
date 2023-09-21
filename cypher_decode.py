#encrypt or decrypt a message

import string
alphabet = string.ascii_lowercase

#enter a message you want to encrypt, and a keyword 
#they keyword is used recursively to offset each of the message's characters!

my_message = "well would you look at that, your coding proficiency is enough to read this!"
my_keyword = "purple"

#takes the message and encrypts it using your keyword
#the index of each letter in the keyword is the offset for the encrption
#the keyword repeats recursively your whole message
def encrypt_message(message, keyword):
    keyword_phrase = ""
    keyword_index = 0
    for character in message:
        #this part allows the keyword to keep cycling through in parallel with your message
        if keyword_index >= len(keyword):
            keyword_index = 0
        #adding a keyword letter for every letter's index in your message 
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        #including everyting that's not a letter!
        else:
            keyword_phrase += character

    encoded_message = ""

    #at every index of the message, subract they keyword's alphabet index at that position
    #add that new character to the encoded message
    for i in range(len(message)):
        if message[i] in alphabet:
            old_message_index = alphabet.find(message[i])
            keyword_offset = alphabet.find(keyword_phrase[i])
            new_message_character = alphabet[(old_message_index - keyword_offset)]
            encoded_message += new_message_character
        else:
            encoded_message += message[i]

    return encoded_message

print(encrypt_message(my_message, my_keyword))

#----------------------------------------------------------------------------------------------------------------

#Now for the opposite! decrypt a message
#this function takes an encrypted message, and the keyword (recursive) used to determine the offset of each letter

#message you want to decode and the keyword to determine offsets
vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

def vigenere_decode(message, keyword):
    #adding a loop to assign every letter in the message to a letter in the keyword phrase
    keyword_phrase = ""
    keyword_index = 0
    for character in message:
        #because the keyword is short, need to make sure
        #the keyword_index starts over at 0 after the lenght of the keyword
        #has been reached
        if keyword_index >= len(keyword):
            keyword_index = 0
        #for characters in the message that are in the alphabet
        #add the letter of the keyword at the keyword index
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            #add 1 to the keyword_index to keep looping through adding 
            #the keyword letters for each letter in the message
            keyword_index += 1
        #takes care of all non-alphabetical letters
        else:
            keyword_phrase += character

    decoded_message = ""

    #for each index of every letter in the encrypted message
    for i in range(len(message)):
        #if the message letter at that index is in the alphabet...
        if message[i] in alphabet:
            #returns the index of the alphabet at the message letter
            old_character_index = alphabet.find(message[i])
            #returns the index of the alphabet at the keyword phrase letter (the offset)
            offset_index = alphabet.find(keyword_phrase[i])
            #calculates the offset for each letter in the message - uses % if it goes over 26 to return to beginning of alphabet
            #uses that caluclation as the index for the alphabet (unencrypted now)
            new_character = alphabet[(old_character_index + offset_index) % 26]
            #adds each of the new unencrypted charactes to the decoded message
            decoded_message += new_character
        else:
            #adds everything else that's not in the alphabet
            decoded_message += message[i]

    return decoded_message


print(vigenere_decode(vigenere_message, vigenere_keyword))
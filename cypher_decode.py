#this function takes an encrypted message, and the keyword (recursive) used to determine the offset of each letter

def vigenere_decode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
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

#message you want to decode and the keyword to determine offsets
vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

print(vigenere_decode(vigenere_message, vigenere_keyword))
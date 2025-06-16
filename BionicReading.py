# This program will take an input of type string then convert it to bionic reading font
# bionic reading is made by making the first half of the letters in each word bold
# if the word has an odd number of characters it will "round up" the number characters to make bold

bold_start = '\033[1m'
bold_end = '\033[0m'

print(f"{bold_start} this text is bold {bold_end}, this text is not")



def bold(text, trans=str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵",),
    ):
    return text.translate(trans)


def convert_word(word):
    #get the number of characters in the word
    #take the first half of the characters
    #convert them to bold with the bold function
    #combine back with the second half of characters
    #return finished word

    finished_word = ""

    word_length = len(word)
    bionic_length = word_length/2
    
    first_half = word[0:word_length]
    second_half = word[word_length+1:]

    bionic_first_half = bold(first_half)



    #check if word length is divisible by 2
    

    finished_word = bionic_first_half + second_half
    return finished_word


def convert_sentence(sentence):
    split_sentence = sentence.split()
    finished_sentence = []
    for word in split_sentence:
        converted_word = convert_word(word)
        finished_sentence.append(converted_word)

    output_string = " ".join(finished_sentence)
    return output_string
    
    #make an array of each word, separated by spaces, then run the convert word for each word in the array
    #recombine the array into a string with spaces in between

word1 = "Family"
word2 = "Hospital"

print(convert_word(word1))
print(convert_word(word2))

sentence1 = "This is a test to see if the bionic reading worked."
print(convert_sentence(sentence1))



#make code to make it do a whole sentence of this. 
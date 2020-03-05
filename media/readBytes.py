##
# Dominick Johnston
# March 2020
# Tagging Project
##

# This file prints a text representation of the beginning of an mp3 file

################################################################################

##
# Helpers
##

# Takes in a len 2 string represneting a hex number. Returns the char that
# hex number represents
def convertHexToChars(word):
    result = ""
    for i in range(0,len(word),2):
        result += chr(int("0x"+word[i:i+2],16))
    return result

################################################################################

##
# Main
##

def main(numBytesToRead = 256, file = "mini.mp3"):
    # open and read from file
    mp3File = open(file,"rb")
    first128 = mp3File.read(numBytesToRead)
    firstHex = first128.hex()

    # build string of "words". We instert spaces between regions of 00s and
    # populated reigons
    firstWords = ""
    lastWasZero = False
    for i in range(0,len(firstHex),2):
        if firstHex[i:i+2] == "00":
            if lastWasZero == False:
                firstWords += " "
            lastWasZero = True
            firstWords += firstHex[i:i+2]
        else:
            if lastWasZero:
                firstWords += " "
            lastWasZero = False
            firstWords += firstHex[i:i+2]

    # We then make a list of these words and transform the nonzero ones into
    # their string representations     
    words = firstWords.split(" ")
    for i in range(len(words)):
        # extremely obtuse. Check if current things is all 0s by seeing if
        # firs char matches exactly a string with the same length of all 0s
        if words[i] != len(words[i])*words[i][0]:
            words[i] = convertHexToChars(words[i])
    words = " ".join(words)

    # finally we print out the results
    print("Raw Bytes:")
    print(first128)
    print()
    print("Hex:")
    print(firstHex)
    print()
    print("Spacing on 00 reigons:")
    print(firstWords)
    print()
    print("Culling long 00 reigons:")
    print(words)
    print()
    mp3File.close()




if __name__ == "__main__":
    main()
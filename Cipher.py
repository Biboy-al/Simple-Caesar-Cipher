

#bounds for upper case chars
maxUpper = ord('Z')
minUpper = ord('A')

#bounds for lower case chars
maxLower = ord('z')
minLower = ord('a')

#function that performs a caesar cipher
def getMessage(shift, cipher):

    #iterates over the message
    for i in range(0, len(cipher)):
        currentChar = cipher[i]
        charOrd = ord(currentChar)+ shift
        #checks if char is upper case
        if(str(currentChar).isupper()):
            #checks if shifting the char goes beyond the bounds
            # if so go to the next logical letter
            if( charOrd >= maxUpper):
                charOrd = minUpper + (charOrd - maxUpper) -1

            elif(charOrd < minUpper):
                charOrd = maxUpper - (minUpper - charOrd) +1

        else:

            if( charOrd >= maxLower):
                charOrd = minLower + (charOrd - maxLower) -1

            elif(charOrd < minLower):
                charOrd = maxLower - (minLower - charOrd)  +1


        cipher[i] = chr(charOrd)
    return "".join(cipher)


#main input
enOrDe = input("1)Encrypt \n2)Decrypt \nChoice: ")

shiftValue = input("shift Value: ")
#checks if shift value is a number
if(shiftValue.isnumeric()):
    shiftValue = int(shiftValue)
#if false exit the program
else:
    print("Invalid shift balue")
    exit()

cipher = list(input("text to be encrypted: "))

#encrypts or decrypts depending on the command
if(enOrDe == "1"):
    print(getMessage(shiftValue, cipher))
elif(enOrDe == "2"):
    print(getMessage(-shiftValue, cipher))
else:
    print("Invalid Choice")









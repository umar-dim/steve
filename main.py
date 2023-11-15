import time

def youAreAGoodFriend(s, shift):
    thisYouCanSee = ""

    for char in s:
        if char.isalpha():  # Check if character is an alphabet
            shift_amount = shift % 26

            if char.islower():
                thisYouCanSee += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                thisYouCanSee += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            # For non-alphabetic characters, just add them as is
            thisYouCanSee += char

    return thisYouCanSee

IAmSorryYouCantReadThis = "Vwhyh, Brx kdyh ehhq d yhub jrrg iulhqg dqg l phdq lw. dovr ixfn brx!"
ThisYouCanRead = youAreAGoodFriend(IAmSorryYouCantReadThis, -3)
LetMePrintItOutForYou = ""

for char in ThisYouCanRead:
    for j in range(32, 127):
        time.sleep(0.005)  # 5000 microseconds = 0.005 seconds
        print(LetMePrintItOutForYou + chr(j))
        if chr(j) == char:
            LetMePrintItOutForYou += chr(j)
            break

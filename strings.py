multiLine_str_tripleQuotation = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(multiLine_str_tripleQuotation[0:6])
print(multiLine_str_tripleQuotation[-23:-1])
print("length is =", len(multiLine_str_tripleQuotation))
print("one line", "two line", sep="-----")  #one line-----two line

stripMethod = "   hello   "
print(stripMethod.strip())#removes spaces

lowerMethod = "hELLo UnIvERse"
print(lowerMethod.lower())#returns lower cases

upperMethod = "these are capital letters"
print(upperMethod.upper())#returns capitals

replaceMethod = "Replace me with yo"
print(replaceMethod.replace("me","yo"))

splitMethod = "hello - universe"
print(splitMethod.split(","))
#method splits the string into subtstrings if it 
#finds instances of the separator

checkIfTxt = 'Check if the wapa is in text'
checkFunc = "wapa" in checkIfTxt
print(checkFunc, ": The word wapa is in")

check_if_not_in_text = "is the word poopy in this string"
checkIf_not_func = "poopy" not in check_if_not_in_text
print(checkIf_not_func,": The word poopy is not in")

hello = "hello "
world = "world"
print(hello+world)

mixedMethods = "   HelLoRZsS  "
print(mixedMethods.lower().strip().split())

arrow_str = "<-----"
arrow_str1 = "----->"
print(arrow_str+" + "+arrow_str1)

if __name__ == '__main__':
    print ("Hello, World!")

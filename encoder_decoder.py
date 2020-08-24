encode_key = {
    "A": "U" , "B" : "S" , "C" : "X" , "D" : "F" , "E" : "A" , "F" : "T" , "G" : "M" , "H" : "J" , "I" : "Y" , "J" : "Z" , "K" : "G" , "L" : "P" , "M" : "B" , "N" : "W" , "O" : "R" ,
    "P" : "V" , "Q" : "I" , "R" : "D" , "S" : "E" , "T" : "Q" , "U" : "C" , "V" : "O" , "W" : "N" , "X" : "L" , "Y" : "H" , "Z" : "K" , 
    "a" :"t" , "b" : "q" , "c" : "n" , "d" : "l" , "e" : "w" , "f" : "r" , "g" : "a" , "h" : "k" , "i" : "o" , "j" : "s" , "k" : "m" , "l" : "c" , "m" : "v" , "n" : "p" , "o" : "u" ,
    "p" : "z", "q" : "d" , "r" : "e" , "s" : "j" , "t" : "y" , "u" : "b" , "v" : "i" , "w" : "g" , "x" : "h" , "y" : "x" , "z" : "f" , '\n' : "\n" , " " : " ", "1" : "1" , "2" : "2:",
    "3" : "3" , "4" : "4" , "5" : "5" , "6" : "6" , "7" : "7" , "8" : "8" , "9" : "9" , "0" : "0" , "!" : "!" , "@" : "@" , "#" : "#" , "%" : "%" , "^" : "^" , "&" : "&" , "*" : "*" ,
    "(" : "(" , ")" : ")" , "_" : "_" , "-" : "-" , "+" : "+" , "/" : "/"   , "?" : "?" , "<" : "<" , ">" : ">" , ":" : ":" , ";" : ";" , "," : "," , "." : "." , "{" : "{" , "}" : "}" , 
    "`" : "`" , "[" : "[" , "]" : "]" , "  " : "  " , "   " : "    " , "    " : "    "  , '"' : '"' , "'" : "'" 
    } 

decode_key = {
    "U" : "A" , "S" : "B" , "X" : "C" , "F" : "D" , "A" : "E" , "T" : "F" , "M" : "G" , "J" : "H" , "Y" : "I" , "Z" : "J" , "G" : "K" , "P" : "L" , "B" : "M" , "W" : 'N' , "R" : "O" , 
    "V" : "P" , "I" : "Q" , "D" : "R" , "E" : "S" , "Q" : "T" , "C" : "U" , "O" : "V" , "N" : "W" , "L" : "X" , "H" : "Y" , "K" : "Z" ,
    "t" : "a" , "q" : "b" , "n" : "c" , "l" : "d" , "w" : "e" , "r" : "f" , "a" : "g" , "k" : "h" , "o" : "i" , "s" : "j" , "m" : "k" ,  "c" : "l" , "v" : "m" , "p" : "n" , "u" : "o" , 
    "z" : "p" , "d" : "q" , "e" : "r" , "j" : "s" , "y" : "t" , "b" : "u" , "i" : "v" , "g" : "w" , "h" : "x" , "x" : "y" , "f" : "z" , "\n" : "\n" , " " : " ", "1" : "1" , "2" : "2:",
    "3" : "3" , "4" : "4" , "5" : "5" , "6" : "6" , "7" : "7" , "8" : "8" , "9" : "9" , "0" : "0" , "!" : "!" , "@" : "@" , "#" : "#" , "%" : "%" , "^" : "^" , "&" : "&" , "*" : "*" ,
    "(" : "(" , ")" : ")" , "_" : "_" , "-" : "-" , "+" : "+" , "/" : "/" , "?" : "?" , "<" : "<" , ">" : ">" , ":" : ":" , ";" : ";" , "," : "," , "." : "." , "{" : "{" , "}" : "}" , 
    "`" : "`" , "[" : "[" , "]" : "]" , "  " : "  " , "   " : "    " , "    " : "    ", '"' : '"' , "'" : "'" 
}

def commands():
    print("Commands")
    print("Count : counts the words")
    print("Replace : replaces a word / text")
    print("Show me : shows you your work")
    print("Delete : delete a line")
    print("Add : adds new line in between already added lines")
    print("Clear : resets everrything")
    print("Done : stops the loop")
    print("to insert a new line just click on enter")

def text(): 
    total_lines = []
    commands()
    print("Enter your text down please")
    while True:
        lines = input("> ")
        if lines != "Done":
            total_lines.append(lines)    
        if lines == "Count":
            total_lines.pop(-1) #this is to remove the last element which is COUNT
            string = "\n".join(total_lines) #to make it a normal string 
            normal_text = string.split() #to split the words so len method will count words instead of letters
            wordsnum = len(normal_text)
            print(f"the number of the words are {wordsnum}")
        if lines == "Show me":
            print("here is what you have written so far")
            total_lines.pop(-1)
            normal_text = "\n".join(total_lines)
            print("-" * 10)
            print(normal_text)
            print("-" * 10)
        if lines == "Clear":
            print("careful what you wish for , are you sure ?")
            answer = input("> ")
            if answer == "yes":
                total_lines.clear()
            else:
                pass
        if lines == "Delete":
            total_lines.pop(-1)
            print("the total lines in the text is " , len(total_lines))
            print("which line do you want to delete ?")
            number = int(input("> "))
            number = number - 1 #converting it into the cardinal order
            total_lines.pop(number)
            print("Done !")
        if lines == "Replace": #alright this is hard and a bit messy so sorry
            total_lines.pop(-1)
            while True :
                print("what is the word you want replaced ?")
                old_word = input("> ")
                print("what is the new word you want to add")
                new_word = input("> ")
                print("which line contains the word ?")
                number = int(input("> "))
                number = number - 1 #converting into cardinal order
                total_lines[number] = total_lines[number].replace(old_word , new_word) #replace the old word by the new_word in the required elemt , then make it equal to the element
                print("done !\ndo you want it to end ?")
                answer = input("> ")
                if answer == "yes":
                    break
        if lines == "Add":
            total_lines.pop(-1)
            print(f"there is {len(total_lines)} lines in the text")
            print("next to which line would you line to insert urs ?")
            number = int(input("> "))
            print("what is your line ?")
            line = input("> ")
            total_lines.insert(number , line)
            print("done !")

        if lines == "Done":
            #the line code : total_lines.pop(-1) , isnt here because 'Done' isnt added to the total line list.
            break

    total_lines = "\n".join(total_lines)
    encode(total_lines)
    
def encode(words):
    encoded_text = []
    for i in words:
        encoded_text.append(encode_key[i]) #append the dictionary value from the 'encode key' to the list
    encoded_text = ''.join(encoded_text) #to make it a normal string
    print("would you like to write over the file or continue whats written ?")
    answer = input("> ")
    if "write over" in answer:
        encoded_file = open("encoded_file.txt" , "w") 
    elif "continue" in answer:
        encoded_text = '\n' + encoded_text
        encoded_file = open("encoded_file.txt" , "a+")
    encoded_file.write(encoded_text)
    encoded_file.close()
    print("Done") 
    
    

def decode():
    decoded_text = []
    with open("encoded_file.txt" , "r") as encoded_file:
        file_content = encoded_file.read()
        encoded_file.close()
    for i in file_content:
        decoded_text.append(decode_key[i]) ##append the dictionary value from the 'decode key' to the list
    decoded_text = ''.join(decoded_text)
    print("here is what is written in the file")
    print("-" * 10)
    print(decoded_text)
    print('-' * 10)
    


        
attempts = 3
print("hello there !")
while attempts != 0 :
    actual_password = "noIdea"
    print("Enter your password please")
    password = input("> ")
    if password == actual_password:
        print("welcome !")
        print("woul you like to encode or decode ?")
        print("E / D")
        action = input("> ")
        if action == "E":
            text()
            break
        if action == "D":
            print("sure")
            decode()
            break
    else:
        print("oops try again")
        attempts -= 1



    



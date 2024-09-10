import string
import os

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['-', '|', 'V', 'b', 'x', 'P', ']', '%', '.', 'R', 'u', 'j', '<', 'g', 't', '6', '&', '>', '^', "'", '#', '?', 'y', '1', 'c', 'l', 'v', 'N', 'd', '5', '!', '+', '3', ';', 'w', 'h', 'm', '[', '_', '@', 'o', 'e', '*', 'B', 'z', '7', 'A', 'J', 'X', ' ', 'a', '(', 'k', 'Y', 'F', 'H', 'O', '`', 'Z', 's', '4', '\\', 'K', 'q', 'I', 'n', 'M', '$', 'Q', 'r', ',', '=', '8', '{', 'C', '~', '0', 'E', 'p', 'L', 'T', '/', 'W', ':', 'i', 'S', ')', '}', 'G', 'f', '2', '9', 'U', 'D', '"']

function = input("Select a function: 1- Encrypt Message 0-Decrypt Message 2-Encrypt File -1-Decrypt File\n")



def encryptMessgae():
    text = input("Enter a message\n")
    cipher = ""

    for letter in text: 
        index = chars.index(letter)
        cipher += key[index]
        
    print(f"encrypted: {cipher}\n")

def decryptMessage():
    encrypted = input("Enter the encrypted message\n")
    text = ""

    for letter in encrypted: 
        index = key.index(letter)
        text += chars[index]

    print(f"decrypted: {text}")

def encryptFile(file, output):
    try: 
        # reads input file and encyrpts
        current_dir = os.getcwd() 
        file_path = os.path.join(current_dir, file)
        with open(file_path, 'r') as f:  #this opens and automatically closes file after
            text=f.read()
            
        cipher = ""
        
        for letter in text: 
            if letter in chars:
              index = chars.index(letter)
              cipher += key[index]  
            else:
                cipher += letter #handles new lines
        
        #adds to new file
        with open(output, "w") as f:
            f.write(cipher)
        
        print(f"file encyrypted. new file {output}")
    
    except FileNotFoundError:
        print(f"Error: {file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
            
def DecryptFile(file, output):
    try: 
        # reads input file and decrypts
        current_dir = os.getcwd() 
        file_path = os.path.join(current_dir, file)
        with open(file_path, 'r') as f:  #this opens and automatically closes file after
            cipher=f.read()
            
        text = ""
        
        for letter in cipher: 
            if letter in key:
              index = key.index(letter)
              text += chars[index]  
            else:
                text += letter #handles new lines
        
        #adds to new file
        with open(output, "w") as f:
            f.write(text)
        
        print(f"file encyrypted. new file {output}")
    
    except FileNotFoundError:
        print(f"Error: {file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if function == "1":
    encryptMessgae()
elif function == "0": 
    decryptMessage()
elif function == "2":
    file = input("Enter the path of file to encrypt: ")
    output = input("\nEnter output file: ")
    encryptFile(file, output)
elif function == "-1":
    file = input("Enter the path of file to decrypt: ")
    output = input("\nEnter output file: ")
    DecryptFile(file, output)
else:
    print("incorrect selection")

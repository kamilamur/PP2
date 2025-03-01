import string
import os

def generate_alphabet_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for letter in string.ascii_uppercase:  
        file_name = f"{letter}.txt"
        file_path = os.path.join(directory, file_name)
        
        with open(file_path, 'w') as file:
            file.write(f"This is {file_name}\n")
        
        print(f"Created file: {file_path}")

def main():
    directory = input("Enter the directory to save the files: ").strip()
    generate_alphabet_files(directory)

if __name__ == "_main_":
    main()
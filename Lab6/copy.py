def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"File '{source_file}' successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print("The source file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_file = input("Enter the source file path: ").strip()
    destination_file = input("Enter the destination file path: ").strip()
    
    copy_file(source_file, destination_file)

if __name__ == "_main_":
    main()
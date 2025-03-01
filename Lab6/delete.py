import os
def delete_file(file_path):
    if not os.path.exists(file_path):
        print("The specified path does not exist.")
        return
    
    if not os.path.isfile(file_path):
        print("The specified path is not a file.")
        return
    
    if not os.access(file_path, os.W_OK):
        print("No permission to delete the file.")
        return
    
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

def main():
    file_path = input("Enter the file path to delete: ").strip()
    delete_file(file_path)

if __name__ == "_main_":
    main()


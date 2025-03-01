import os

def list_only_directories(path):
    print("\nOnly directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_only_files(path):
    print("\nOnly files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_directories_and_files(path):
    print("\nAll directories and files:")
    for root, dirs, files in os.walk(path):
        print(f"\nDirectory: {root}")
        for d in dirs:
            print(f"  Sub-directory: {d}")
        for f in files:
            print(f"  File: {f}")

def main():
    path = input("Enter the directory path: ").strip()

    if os.path.exists(path) and os.path.isdir(path):  
        list_only_directories(path)
        list_only_files(path)
        list_all_directories_and_files(path)
    else:
        print("The specified path does not exist or is not a directory.")

if __name__ == "_main_":
    main()
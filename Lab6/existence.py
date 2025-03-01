import os

def check_path_access(path):
    print(f"\nChecking access for path: {path}")
    if os.path.exists(path):
        print("✅ Path exists.")
    else:
        print("❌ Path does not exist.")
        return
    
    
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")

def main():
    path = input("Enter the path to check: ")
    check_path_access(path)

if __name__== "main_":
    main()
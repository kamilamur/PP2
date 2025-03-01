def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    count_lines_in_file(file_path)

if __name__ == "_main_":
    main()
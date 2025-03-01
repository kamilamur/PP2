def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List successfully written to file: {file_path}")
    except Exception as e:
        print(f" An error occurred: {e}")

def main():
    file_path = input("Enter the file path to save the list (e.g., output.txt): ").strip()
    print("Enter list items one by one (type 'done' to finish):")
    data_list = []
    while True:
        item = input("> ").strip()
        if item.lower() == 'done':
            break
        data_list.append(item)

    
    write_list_to_file(file_path, data_list)

if __name__ == "_main_":
    main()
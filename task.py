def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found.")

def write_to_file(filename):
    user_input = input("Please enter some text: ")
    with open(filename, 'w') as file:
        file.write(user_input)
    print(f"Text saved to {filename}.")

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def append_to_file(filename):
    new_sentence = input("Please enter a new sentence: ")
    with open(filename, 'a') as file:
        file.write(new_sentence + "\n")
    print(f"Sentence appended to {filename}.")

def copy_file_contents(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            with open(destination_filename, 'w') as destination_file:
                destination_file.write(source_file.read())
        print(f"Contents copied from {source_filename} to {destination_filename}.")
    except FileNotFoundError:
        print(f"File {source_filename} not found.")

def main():
    while True:
        print("\nFile Operations Menu:")
        print("1. Read a file line by line")
        print("2. Write to a file")
        print("3. Count words in a file")
        print("4. Append to a file")
        print("5. Copy contents of one file to another")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename: ")
            read_file_line_by_line(filename)
        elif choice == "2":
            filename = input("Enter the filename: ")
            write_to_file(filename)
        elif choice == "3":
            filename = input("Enter the filename: ")
            count_words_in_file(filename)
        elif choice == "4":
            filename = input("Enter the filename: ")
            append_to_file(filename)
        elif choice == "5":
            source_filename = input("Enter the source filename: ")
            destination_filename = input("Enter the destination filename: ")
            copy_file_contents(source_filename, destination_filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
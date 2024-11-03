# Aim: Implement Python programs to explore files and directories.
# a. Python program to count number of lines, words, and characters in a file.
# b. Python program to display files available in the current directory

def count_lines_words_chars(file_name):

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            words = file.read().split()
            characters = file.read()
            print(f"Number of lines: {len(lines)}")
            print(f"Number of words: {len(words)}")
            print(f"Number of characters: {len(characters)}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def display_files_in_directory():
    import os
    try:
        files = os.listdir()
        print(f"Files in the current directory: {files}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def main():
    file_name = input("Enter the file name: ")
    count_lines_words_chars(file_name)
    display_files_in_directory()
    
main()
import sys
import os 

def count_bytes(file_path):
    '''
    Counts the file size

    Parameters:
    - file_path: path to the file to be scanned

    Output:
    - returns the size of the file or either raises error if file is not found
    '''
    return os.path.getsize(file_path)

def count_lines(file_path):
    '''
    Counts the number of lines in specified file

    Parameters:
    - file_path: path to the file to be scanned

    Output:
    - returns the line count in a text file
    '''
    lines = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines += 1
            return lines
    except FileNotFoundError:
        print('File not found.')
        return None

def count_words(file_path):
    '''
    Counts the number of words in a text file

    Parameters: 
    -file_path: path of the file to be scanned

    Output:
    - returns word count in a text file 
    '''
    words = 0
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            for line in file:
                words += len(line.split())
            return words
    except FileNotFoundError:
        print('File not found')
        return None
    
def count_chars(file_path):
    '''
    Counts the number of characters in a character file

    Parameters:
    -file_path: path of the file to be scanned

    Output:
    - returns the character count of a text file
    '''
    characters = 0
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            for line in file:
                characters += len(line)
            return characters
    except FileNotFoundError:
        print("File not found")
        return None


def main():
    if len(sys.argv) == 2:
        def_file_path = sys.argv[1]
        bytes_count = count_bytes(def_file_path)
        line_count = count_lines(def_file_path)
        word_count = count_words(def_file_path)
        print(f'{line_count} {word_count} {bytes_count} {def_file_path}')
    
    elif len(sys.argv) == 3:
        option = sys.argv[1]
        file_path = sys.argv[2]

        if option == '-c':
            bytes_count = count_bytes(file_path)
            print(f'{bytes_count} {file_path}')
        elif option == '-l':
            line_count = count_lines(file_path)
            print(f'{line_count} {file_path}')
        elif option == '-w':
            word_count = count_words(file_path)
            print(f'{word_count} {file_path}')
        elif option == '-m':
            char_count = count_chars(file_path)
            print(f'{char_count} {file_path}')
    
    else:
        print('Usage: python ccwc.py -c <filename>')
        return


if __name__ == '__main__':
    main()



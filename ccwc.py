import sys
import os 

def count_bytes(file_path):
    return os.path.getsize(file_path)

def count_lines(file_path):
    lines = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines += 1
            return lines
    except FileNotFoundError:
        print('File not found.')
        return None

def main():
    if  len(sys.argv) != 3:
        print('Usage: python ccwc.py -c <filename>')
        return
    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == '-c':
        bytes_count = count_bytes(file_path)
        print(f'{bytes_count} {file_path}')
    elif option == '-l':
        lines_count = count_lines(file_path)
        print(f'{lines_count} {file_path}')

if __name__ == '__main__':
    main()



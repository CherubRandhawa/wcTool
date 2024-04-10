Unix wc Command Line Tool Clone
This project is a clone of the Unix wc command line tool, built as a coding challenge. The wc tool, short for "word count", is a command-line utility that outputs the number of lines, words, and bytes in a file. It's a classic example of a simple yet powerful Unix tool, following the Unix philosophy of doing one thing well.

Unix Philosophy
The Unix command line tools embody several key principles:

Writing simple parts connected by clean interfaces: Each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
Design programs to be connected to other programs: Each tool can be easily connected to other tools to create incredibly powerful compositions.
Following these philosophies has made Unix command line tools some of the most widely used software engineering tools, allowing the creation of complex text data processing pipelines from simple command line tools.

Usage
To use the ccwc (coding challenge word counter) tool:

Download the provided test.txt file.
Run the script ccwc.py with the appropriate options and filename.
Example usage:

python ccwc.py -l test.txt

This command will output the number of lines in the test.txt file.

Similarly other commands can be used as well.

This also supports the default command when no option is provided and it ouputs the default result with value of all three parameters.

python ccwc.py test.txt
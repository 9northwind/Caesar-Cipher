class Encryption:
    def __init__(self, filepath, key: int):
        self.filepath = filepath
        self.key = key
        self.cipher = ''

    def encrypt(self):
        symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
                   '{', '[', '}', ']', '\\', '|', ':', ';', '"', "'", ',', '<', '.', '>', '?',
                   '/']
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        try:
            with open(self.filepath, 'r') as f:
                data = f.read()
            for char in data:
                if char.isupper():
                    char_index = ord(char) - ord('A') + 1  # Finding the position of character in alphabet
                    new_char_index = (char_index + self.key) % 26
                    new_char = chr(new_char_index + ord('A') - 1)  # Finding the character at new index
                    self.cipher += new_char
                elif char.islower():
                    char_index = ord(char) - ord('a') + 1
                    new_char_index = (char_index + self.key) % 26
                    new_char = chr(new_char_index + ord('a') - 1)
                    self.cipher += new_char
                elif char in symbols:
                    char_index = symbols.index(char)
                    new_char_index = (char_index + self.key) % 31
                    new_char = symbols[new_char_index]
                    self.cipher += new_char
                elif char.isdigit():
                    char_index = numbers.index(char)
                    new_char_index = (char_index + self.key) % 10
                    new_char = numbers[new_char_index]
                    self.cipher += new_char
                elif char == ' ':
                    self.cipher += '`'
            with open(self.filepath, 'w') as f:
                f.write(self.cipher)
        except FileNotFoundError:
            print("File not found.")

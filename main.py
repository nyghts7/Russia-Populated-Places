from transliterate import translit

def transliterate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    transliterated_text = translit(text, 'ru', reversed=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(transliterated_text)

def main():
    input_file = input("Enter the input file path: ")
    output_file = input("Enter the output file path: ")

    transliterate_file(input_file, output_file)
    print("Transliteration completed.")

if __name__ == '__main__':
    main()
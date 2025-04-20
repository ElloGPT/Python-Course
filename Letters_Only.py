import string

def is_letter_only(text: str) -> None:
    if len(text.strip()) <= 0:
        raise ValueError("Please enter a non-empty text!")

    alphabet: str = string.ascii_letters + " "

    for char in text:
        if char not in alphabet:
            raise ValueError("The text can only contain English letters and spaces!")

    print(f"\"{text}\" is only in letters. Nice!")

def main() -> None:
    while True:
        try:
            user_input: str = input("Check Text: ")
            is_letter_only(user_input)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Encountered an unknown exception: {type(e)} - {e}")

if __name__ == "__main__":
    main()

#This program checks if the text has only letters
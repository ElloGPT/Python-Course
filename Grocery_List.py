import time as t

def welcome() -> None:
    print("Welcome to Groceries!\n----------------\n[1] Add an item\n[2] Remove an item\n[3] List all Items\n[0] Exit program\n----------------")


def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f"{item} has been added!")


def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f"{item} has been removed!")
    except ValueError:
        print(f"{item} is not in {groceries}")


def display_list(groceries: list[str]) -> None:
    try:
        print("____List____")
        for i, item in enumerate(groceries, 1):
            print(f"{i}: {item.capitalize()}")
    except Exception:
        print("You dont have a list yet!")
        t.sleep(1)

    print("_"*10)


def is_an_option(text: str) -> bool:
    return text in ["1","2","3","0"]


def main() -> None:
    groceries: list[str] = []

    welcome()
    while True:
        user_input: str = input("Option: ").lower()

        if not is_an_option(user_input):
            print("Please pick a valid option..")
            continue
        if user_input == "1":
            new_item: str = input("What do you want to add? - ").lower()
            add_item(new_item, groceries)
        elif user_input == "2":
            del_item: str = input("What item do you want to remove? - ").lower()
            remove_item(del_item, groceries)
        elif user_input == "3":
            display_list(groceries)
        elif user_input == "0":
            print("Exiting program..")
            t.sleep(1.5)
            break


if __name__ == "__main__":
    main()
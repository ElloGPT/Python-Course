from datetime import datetime
import time as t

def get_response(text: str) -> str:
    lowered: str = text.lower()

    if lowered in ["hello", "hi", "hey"]:
        return "Hey there!"
    elif "how are you" in lowered:
        return "I`m good thanks!"
    elif "your name" in lowered:
        return "My name is ElloGPT :D"
    elif "time" in lowered:
        current_time: datetime = datetime.now()
        return f"The time is: {current_time.strftime('%H:%M')}"
    elif lowered in ["bye", "see you", "goodbye"]:
        return "It was nice talking to you!"
    else:
        return f"Sorry i do not understand \"{text}\"."
    
def main(): 
    while True:
        user_input: str = input("You: ")

        if user_input == "exit":
            print("ElloGPT: It was a pleasure to meet you!")
            t.sleep(1.5)
            break

        bot_response: str = get_response(user_input)
        print(f"ElloGPT: {bot_response}")

if __name__ == "__main__":
    main()

#This is a very simplified version of a chatbot.
#More responses and features need to be added and further expanded.

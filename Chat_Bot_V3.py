from difflib import get_close_matches

def find_close_matches(user_question: str, knowledge: dict) -> str | None:
    question: list[str] = [question for question in knowledge]
    matches: list[str] = get_close_matches(user_question, question, n=1, cutoff=0.6)

    if matches:
        return matches[0]
    

def run_ElloGPT(knowledge: dict) ->  None:
    while True:
        user_input: str = input("You: ")

        best_match: str | None = find_close_matches(user_input, knowledge)
        response: str = knowledge.get(best_match)

        if response == "break":
            break

        elif response:
            print(f"ElloGPT: {response}")
        
        else:
            print(f"ElloGPT: I do not understand..")

def main() -> None:

    brain: dict[str, str] = {"hello": "Hey there!",
                             "how are you?": "I am good, thx",
                             "what is the time?":"No clue!",
                             "what can you do": "I can answer your questions",
                             "ok": "great!"}
    
    run_ElloGPT(knowledge=brain)
    
if __name__ == "__main__":
    main()
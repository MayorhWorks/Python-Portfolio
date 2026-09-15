import random
import json
import os

def load_questions(filepath):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filepath)
    try:

        with open(full_path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Could not find {filepath}. Make sure it's in the same folder.")
        return [] 
def run_layer():
    questions = load_questions("questions.json")
    if not questions:
        return

    play_again = True
    while play_again:
        play_again = play_round(questions)

    print("Thanks for playing!")


def ask_to_replay(message):
    print(message)
    answer = input("Wanna try again? (yes/no): ")
    return answer.strip().lower() == "yes"


def play_round(questions):
    re_questions = questions.copy()
    random.shuffle(re_questions)
    score = 0
    total = len(re_questions)

    for item in re_questions:
        print(item["question"])
        user_answer = input("Your Answer (or press Enter to skip)")

        if user_answer.strip() == "":
            print("Skipped")
            continue

        correct_answer = item["answer"].strip().lower()
        given = user_answer.strip().lower()

        if correct_answer == given:
            print("Correct!")
            score += 1
        else:
            print(f"The correct answer was {item['answer']}")
    final_score = score/total
    print(f"\nFinal score: {score}/{total}")

    if final_score < 0.5:
        return ask_to_replay("Oops! Not good enough 😢")

    elif final_score < 0.8:
        return ask_to_replay("Decent effort, but there's room to improve.")
        
    else:
        return ask_to_replay("Great job! 🥳")
        

if __name__ == "__main__":
        run_layer() 
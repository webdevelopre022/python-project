#YouTube channel 5starcoder
#subscribe my channel 
#project_06

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")
    print(f"\n🎉 You got {score}/{len(questions)} correct.")

def main():
    questions = [
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
            "answer": "A"
        },
        {
            "question": "How many bones are there in the adult human body?",
            "options": ["A. 198", "B. 206", "C. 210", "D. 230"],
            "answer": "B"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Carbon Dioxide"],
            "answer": "D"
        }
    ]

    print("🧠 Welcome to the Science Quiz!")
    run_quiz(questions)

if __name__ == "__main__":
    main()

import random
from Body.Speak import Speak

# Periodic table dictionary
periodic_table = {
    1: {'symbol': 'H', 'name': 'Hydrogen'},
    2: {'symbol': 'He', 'name': 'Helium'},
    3: {'symbol': 'Li', 'name': 'Lithium'},
    4: {'symbol': 'Be', 'name': 'Beryllium'},
    5: {'symbol': 'B', 'name': 'Boron'},
    6: {'symbol': 'C', 'name': 'Carbon'},
    7: {'symbol': 'N', 'name': 'Nitrogen'},
    8: {'symbol': 'O', 'name': 'Oxygen'},
    9: {'symbol': 'F', 'name': 'Fluorine'},
    10: {'symbol': 'Ne', 'name': 'Neon'},
    11: {'symbol': 'Na', 'name': 'Sodium'},
    12: {'symbol': 'Mg', 'name': 'Magnesium'},
    # Add more elements as needed...
}
# Main program loop
while True:
    Speak("Let's learn the periodic table!")
    Speak("Type 'quit' to exit the program.")
    Speak("Type 'random' to generate a random element.")
    Speak("Type 'quiz' to start a quiz.")

    Speak("Enter an element symbol or a command: ")
    user_input = input("Enter an element symbol or a command: ")

    if user_input == 'quit':
        break

    if user_input == 'random':
        atomic_number = random.choice(list(periodic_table.keys()))
        element = periodic_table[atomic_number]
        Speak("Random element: {element['symbol']} ({atomic_number}) - {element['name']}")
        print(f"Random element: {element['symbol']} ({atomic_number}) - {element['name']}")
        continue

    if user_input == 'quiz':
        score = 0
        Speak("Enter the number of questions for the quiz: ")
        num_questions = int(input("Enter the number of questions for the quiz: "))
        quiz_elements = random.sample(list(periodic_table.keys()), num_questions)

        Speak("Quiz starting...\n")
        print("Quiz starting...\n")

        for atomic_number in quiz_elements:
            element = periodic_table[atomic_number]
            symbol_question = f"What is the symbol for {element['name']}?"
            Speak(symbol_question)
            atomic_number_question = f"What is the atomic number of {element['name']}?"
            Speak(atomic_number_question)
            symbol_answer = element['symbol']
            atomic_number_answer = atomic_number

            user_symbol_answer = input(symbol_question + " ")
            user_atomic_number_answer = input(atomic_number_question + " ")

            if user_symbol_answer == symbol_answer and user_atomic_number_answer == str(atomic_number_answer):
                print("Correct!")
                Speak("Coreect!")
                score += 1
            else:
                print(f"Wrong! The correct answers are: {symbol_answer} ({atomic_number_answer}).")
                Speak("Wrong!")

        percentage = (score / num_questions) * 100
        print(f"\nQuiz finished! Your score: {score}/{num_questions} ({percentage}%)\n")
        Speak(f"\nQuiz finished! Your score: {score}/{num_questions} ({percentage}%)\n")

        continue

    found_element = False

    for atomic_number, element in periodic_table.items():
        if element['symbol'] == user_input:
            print(f"Element: {element['symbol']} ({atomic_number}) - {element['name']}")
            found_element = True
            break

    if not found_element:
        print("Invalid input. Please enter a valid element symbol or command.")
        Speak("Invalid input. Please enter a valid element symbol or command.")

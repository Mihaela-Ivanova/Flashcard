import random


class Flashcard:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Q: {self.question} | A: {self.answer}"


class FlashcardManager:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, question: str, answer: str):
        self.flashcards[question] = Flashcard(question, answer)
        print("Flashcard added successfully!")

    def edit_flashcard(self, old_question: str, new_question: str, new_answer: str):
        if old_question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != old_question:
                del self.flashcards[old_question]
            print("Flashcard updated successfully!")
        else:
            print("Flashcard not found.")

    def delete_flashcard(self, question: str):
        if question in self.flashcards:
            del self.flashcards[question]
            print("Flashcard deleted successfully!")
        else:
            print("Flashcard not found.")

    def list_flashcards(self):
        if self.flashcards:
            print("\nAvailable Flashcards:")
            for flashcard in self.flashcards.values():
                print(flashcard)
        else:
            print("No flashcards available.")

    def review_flashcard(self):
        if self.flashcards:
            flashcard = random.choice(list(self.flashcards.values()))
            print(f"\nQuestion: {flashcard.question}")
            input("Press Enter to reveal the answer...")
            print(f"Answer: {flashcard.answer}\n")
        else:
            print("No flashcards to review!")


def main():
    manager = FlashcardManager()

    while True:
        print("\nPlease choose an option:")
        print("1. Create a new flashcard")
        print("2. Edit a flashcard")
        print("3. Delete a flashcard")
        print("4. List all flashcards")
        print("5. Review flashcards")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            manager.add_flashcard(question, answer)

        elif choice == 2:
            old_question = input("Enter the question to edit: ")
            new_question = input("Enter the new question: ")
            new_answer = input("Enter the new answer: ")
            manager.edit_flashcard(old_question, new_question, new_answer)

        elif choice == 3:
            question = input("Enter the question to delete: ")
            manager.delete_flashcard(question)

        elif choice == 4:
            manager.list_flashcards()

        elif choice == 5:
            manager.review_flashcard()

        elif choice == 6:
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
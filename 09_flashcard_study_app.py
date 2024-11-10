import random


class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_question(self):
        return f"Question: {self.question}"

    def display_answer(self):
        return f"Answer: {self.answer}"


class FlashcardManager:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, question, answer):
        self.flashcards[question] = Flashcard(question, answer)

    def edit_flashcard(self, question, new_question, new_answer):
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]

    def delete_flashcard(self, question):
        if question in self.flashcards:
            del self.flashcards[question]

    def list_flashcards(self):
        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())

    def review_flashcard(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")


flash = FlashcardManager()

while True:
    print("Please pick one of the following options: "
          "\n1. Create a new flashcard."
          "\n2. Edit a flashcard."
          "\n3. Delete a flashcard."
          "\n4. Print the questions."
          "\n5. View Workout Plans"
          "\n6. Exit"
          )

    command = int(input())

    if command == 6:
        print("Goodbye! 👋")
        break

    if command == 1:
        question = input("What question do you want to add: ")
        answer = input("What is the answer: ")
        flash.add_flashcard(question, answer)

    elif command == 2:
        old_question = input("What question do you want to edit: ")
        new_question = input("What is the new question: ")
        new_answer = input("What is the answer: ")
        flash.edit_flashcard(old_question, new_question, new_answer)

    elif command == 3:
        delete_question = input("What question do you want to delete: ")
        flash.delete_flashcard(delete_question)

    elif command == 4:
        flash.list_flashcards()

    elif command == 5:
        flash.review_flashcard()














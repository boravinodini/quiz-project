
# from quiz import Quiz

# quiz1 = Quiz(1, "Python Basics", "Python")

# quiz1.add_question(
#     "What is Python?",
#     ["Programming Language", "Database", "Browser", "OS"],
#     "Programming Language"
# )

# quiz1.display_quiz()

# from quiz import Quiz
# from user import User

# # Create Quiz
# quiz1 = Quiz(1, "Python Basics", "Python")

# quiz1.add_question(
#     "What is Python?",
#     ["Programming Language", "Database", "Browser", "OS"],
#     "Programming Language"
# )

# quiz1.display_quiz()

# print("-------------------------")

# # Create User
# user1 = User(101, "Vinodini")

# user1.attempt_quiz("Python Basics", 10)

# user1.display_user()


# from utils import save_data, load_data

# # Sample quiz data
# quiz_data = [
#     {
#         "quiz_id": 1,
#         "title": "Python Basics",
#         "topic": "Python"
#     }
# ]

# # Save data
# save_data("quizzes.json", quiz_data)

# # Load data
# result = load_data("quizzes.json")

# print("Loaded Quiz Data:")
# print(result)


from quiz import Quiz
from utils import save_data, load_data
from user import register_user, login_user


def create_quiz():

    quizzes = load_data("quizzes.json")

    quiz_id = len(quizzes) + 1

    title = input("Enter Quiz Title: ")
    topic = input("Enter Quiz Topic: ")

    quiz = Quiz(quiz_id, title, topic)

    total = int(input("How many questions do you want to add? "))

    for i in range(total):

        print("\nQuestion", i + 1)

        question = input("Enter Question: ")

        options = []

        for j in range(4):
            option = input(f"Enter Option {chr(65+j)}: ")
            options.append(option)

        answer = input("Enter Correct Answer (A/B/C/D): ").upper()

        if answer not in ["A", "B", "C", "D"]:
            print("Invalid answer! Please enter A, B, C or D.")
            return

        quiz.add_question(question, options, answer)

    quiz_data = {
        "quiz_id": quiz.quiz_id,
        "title": quiz.title,
        "topic": quiz.topic,
        "questions": quiz.questions
    }

    quizzes.append(quiz_data)

    save_data("quizzes.json", quizzes)

    print("\nQuiz created successfully!")


def take_quiz():

    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    print("\nAvailable Quizzes:")

    for quiz in quizzes:
        print(quiz["quiz_id"], "-", quiz["title"])

    quiz_id = int(input("Enter Quiz ID: "))

    selected_quiz = None

    for quiz in quizzes:
        if quiz["quiz_id"] == quiz_id:
            selected_quiz = quiz
            break

    if selected_quiz is None:
        print("Quiz not found!")
        return

    score = 0

    for i, question in enumerate(selected_quiz["questions"], 1):

        print("\nQuestion", i, ":", question["question"])

        for j, option in enumerate(question["options"]):
            print(chr(65+j), ".", option)

        answer = input("Enter answer (A/B/C/D): ").upper()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\n========== RESULT ==========")
    print("Total Questions:", len(selected_quiz["questions"]))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(selected_quiz["questions"]) - score)
    print("Final Score:", score, "/", len(selected_quiz["questions"]))



def rate_quiz():

    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    print("\n========== AVAILABLE QUIZZES ==========")

    for quiz in quizzes:
        print(quiz["quiz_id"], "-", quiz["title"])

    try:
        quiz_id = int(input("\nEnter Quiz ID: "))
    except ValueError:
        print("Please enter a valid Quiz ID!")
        return

    selected_quiz = None

    for quiz in quizzes:
        if quiz["quiz_id"] == quiz_id:
            selected_quiz = quiz
            break

    if selected_quiz is None:
        print("Quiz not found!")
        return

    try:
        rating = int(input("Give rating (1 to 5): "))

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    comment = input("Enter your comment: ").strip()

    if not comment:
        print("Comment cannot be empty!")
        return

    review = {
        "rating": rating,
        "comment": comment
    }

    if "reviews" not in selected_quiz:
        selected_quiz["reviews"] = []

    selected_quiz["reviews"].append(review)

    save_data("quizzes.json", quizzes)

    print("\nThank you for your feedback!")
    print("Rating:", rating, "/5")
    print("Comment:", comment)



def view_reviews():

    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    print("\n========== QUIZ REVIEWS ==========")

    for quiz in quizzes:

        print("\nQuiz Title:", quiz["title"])

        reviews = quiz.get("reviews", [])

        if not reviews:
            print("No reviews available!")
            continue

        total_rating = 0

        for review in reviews:
            print("Rating:", review["rating"], "/5")
            print("Comment:", review["comment"])

            total_rating += review["rating"]

        average = total_rating / len(reviews)

        print("Average Rating:", round(average, 2), "/5")


def view_reviews():
    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    print("\n========== QUIZ REVIEWS ==========")

    for quiz in quizzes:
        print("\nQuiz Title:", quiz["title"])

        reviews = quiz.get("reviews", [])

        if not reviews:
            print("No reviews available!")
            continue

        total_rating = 0

        for review in reviews:
            print("Rating:", review["rating"], "/5")
            print("Comment:", review["comment"])
            total_rating += review["rating"]

        average = total_rating / len(reviews)
        print("Average Rating:", round(average, 2), "/5")






def main():

    while True:

        print("\n========== QUIZ APPLICATION ==========")
        print("\n========== QUIZ APPLICATION ==========")
        print("1. Create Quiz")
        print("2. View All Quizzes")
        print("3. Take Quiz")
        print("4. Search Quiz")
        print("5. Rate Quiz")
        print("6. View Ratings and Comments")
        print("7. Register User")
        print("8. Login User")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_quiz()

        elif choice == "2":
            view_all_quizzes()

        elif choice == "3":
            take_quiz()

        elif choice == "4":
            search_quiz()

        elif choice == "5":
            rate_quiz()
        elif choice == "6":
            view_reviews()
        elif choice == "7":
            register_user()

        elif choice == "8":
            login_user()

        elif choice == "9":
            print("Thank you for using Quiz Application!")
            break


def view_all_quizzes():

    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    print("\n========== AVAILABLE QUIZZES ==========")

    for quiz in quizzes:

        print("\nQuiz ID:", quiz["quiz_id"])
        print("Title:", quiz["title"])
        print("Topic:", quiz["topic"])

        questions = quiz.get("questions", [])

        print("Total Questions:", len(questions))


def search_quiz():

    quizzes = load_data("quizzes.json")

    if not quizzes:
        print("No quizzes available!")
        return

    keyword = input("Enter quiz title or topic to search: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for quiz in quizzes:

        title = quiz.get("title", "").lower()
        topic = quiz.get("topic", "").lower()

        if keyword in title or keyword in topic:

            print("\nQuiz ID:", quiz["quiz_id"])
            print("Title:", quiz["title"])
            print("Topic:", quiz["topic"])
            print("Total Questions:", len(quiz.get("questions", [])))

            found = True

    if not found:
        print("No matching quiz found!")



if __name__ == "__main__":
    main()


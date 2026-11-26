
class Quiz:
    def __init__(self, quiz_id, title, topic):
        self.quiz_id = quiz_id
        self.title = title
        self.topic = topic
        self.questions = []

    def add_question(self, question, options, answer):
        question_data = {
            "question": question,
            "options": options,
            "answer": answer
        }

        self.questions.append(question_data)

    def display_quiz(self):
        print("Quiz ID:", self.quiz_id)
        print("Quiz Title:", self.title)
        print("Topic:", self.topic)
        print("Total Questions:", len(self.questions))
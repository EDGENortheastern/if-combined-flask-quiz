from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

def load_question():
    with open("questions.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)
        return row["question"], row["answer"]

@app.route("/", methods=["GET", "POST"])
def quiz():
    question, correct_answer = load_question()

    if request.method == "POST":
        name = request.form.get("name")
        user_answer = request.form.get("answer")

        save_result(name, question, user_answer, correct_answer)

        return render_template(
            "result.html",
            name=name,
            question=question,
            user_answer=user_answer,
            correct_answer=correct_answer,
            correct=(user_answer.strip().lower() == correct_answer.lower())
        )

    return render_template("quiz.html", question=question)

def save_result(name, question, answer, correct):
    file_exists = os.path.exists("results.csv")
    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["name", "question", "user_answer", "correct_answer"])
        writer.writerow([name, question, answer, correct])

if __name__ == "__main__":
    app.run(debug=True)

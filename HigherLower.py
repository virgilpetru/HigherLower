from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def title():
    return "<h1 style='font-size: 20pt'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/guess/<int:number>')
def check_number(number):
    if number < random_number:
        return "<h1 style='color: red'>Number Too Low, Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemdieHlwb3J2MmozdXFsczhyZTBmdnV5em0ybnFoejJxbHJod2pvOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gKHGnB1ml0moQdjhEJ/giphy.gif' width=500>"
    elif number > random_number:
        return "<h1 style='color: blue'>Number Too High, Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb20xNDZnMm9zMXRjaTlyMjlpbTJsbWVhdjAzNjhtM3F0d2htYTgzOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fpXxIjftmkk9y/giphy.gif' width=500>"
    else:
        return "<h1 style='color: green'>You guessed right!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG9jamR0dXF3dzl5NjB2Y2JmMDRhemR2MmN5cHF1bThnajZhNHQwcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ynaCWB9soHk1a/giphy.gif' width=500>"

if __name__ == "__main__":
    app.run(debug=True)
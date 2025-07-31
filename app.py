from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps World!"
    return "Lets Discuss, Devops"

if __name__ == '__main__':
    app.run(debug=True)

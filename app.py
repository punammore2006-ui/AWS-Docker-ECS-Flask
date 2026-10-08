from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Containerized Flask Application</h1>
    <p>Deployed using Python Flask, Docker, Amazon ECR, and Amazon ECS.</p>
    <p>Created by Punam More</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
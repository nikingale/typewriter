from flask import Flask
from flask import request, render_template
from processor import process

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/score', methods=['GET', 'POST'])
def score():
    data = request.json
    scores = process(data["text"])
    return buildResponse(scores)


def buildResponse(scores):
    easy = list()
    medium = list()
    hard = list()

    for word in scores:
        if scores[word] > 5.0 and scores[word] <= 10.0:
            easy.append(word)
        if scores[word] > 10.0 and scores[word] <= 30.0:
            medium.append(word)
        if scores[word] > 30.0:
            hard.append(word)

    words = dict()
    words["easy"] = easy
    words["medium"] = medium
    words["hard"] = hard

    if len(scores) == 0:
        score = 0
    else: 
        score = round((len(medium) + len(hard)) / len(scores) * 100 , 2)

    response = dict()
    response["score"] = score
    response["words"] = words

    return response
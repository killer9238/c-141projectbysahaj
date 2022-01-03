from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv', "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    article = all_articles[0]
    return jsonify({
        "data": article,
        "status": "success"
    })
    
@app.route("/liked-article", methods=["POST"])
def liked_article():
    all_article = all_articles[1:]
    article = all_article[0]
    
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    all_article = all_articles[1:]
    article = all_article[0]
    
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()
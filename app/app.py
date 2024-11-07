from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("tweet_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    tweet_text = data.get("text")
    if not tweet_text:
        return jsonify({"error": "No input provided"}), 400

    # Preprocess and predict sentiment
    transformed_text = vectorizer.transform([tweet_text])
    sentiment = model.predict(transformed_text)[0]
    sentiment_text = "Positive" if sentiment == 1 else "Negative"

    return jsonify({"sentiment": sentiment_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080 ,debug=True)

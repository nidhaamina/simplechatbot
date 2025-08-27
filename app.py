from flask import Flask, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, render_template


load_dotenv()
print("Loaded API Key:", os.getenv("GROQ_API_KEY"))


app = Flask(__name__)


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        response = client.chat.completions.create(
            model="llama3-8b-8192",  
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message},
            ],
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)


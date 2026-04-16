from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Initialize Groq client
from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an educational assistant. Explain clearly with examples."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        answer = response.choices[0].message.content

    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"response": answer})


# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

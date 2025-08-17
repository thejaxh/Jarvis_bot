from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi, I am Jarvis 👋 — always online!"

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json or {}
    user = data.get("user", "friend")
    mood = data.get("mood", "normal")
    
    if mood == "sad":
        return {"reply": f"Don't worry {user}, ellam sheriyakum 🙌"}
    elif mood == "happy":
        return {"reply": f"Wow {user}! Ninte santhosham kandittu enikkum joy aaayi 😃"}
    elif mood == "hungry":
        return {"reply": f"{user}, time to eat something! 🍲"}
    else:
        return {"reply": f"Hi {user}, Jarvis here — ethokke venam paroo 😊"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

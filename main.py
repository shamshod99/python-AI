from flask import Flask, request, jsonify
import yfinance as yf
import pandas_ta as ta

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Ustoz ishlayapti!"

# Foydalanuvchi bilan chat qilish API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # JSON ma'lumotni olish
    user_message = data.get("message", "")

    # Hozircha oddiy javob
    response = {"reply": f"Siz yozdingiz: {user_message}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

# Tesla (TSLA) aksiyalarini yuklaymiz
df = yf.download("TSLA", period="1mo", interval="1d")

# RSI va MACD hisoblash
df["RSI"] = ta.rsi(df["Close"])
df["MACD"] = ta.macd(df["Close"])["MACD_12_26_9"]

# Natijani chiqaramiz
print(df.tail())

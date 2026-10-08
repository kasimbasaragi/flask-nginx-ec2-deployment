from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LoveConnect</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 150px;
                background: linear-gradient(135deg, #ff758c, #ff7eb3);
                color: white;
            }

            h1 {
                font-size: 50px;
            }

            p {
                font-size: 22px;
            }

            button {
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 25px;
                background: white;
                color: #ff4f81;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <h1>❤️ Welcome to LoveConnect</h1>
        <p>Find someone special and start a beautiful connection.</p>
        <button>Get Started</button>
    </body>
    </html>
    """
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

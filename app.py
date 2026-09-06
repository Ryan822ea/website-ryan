from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Website Ryan</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
                font-family: Arial;
                min-height: 100vh;
                padding-top: 70px;
                overflow: hidden;
            }

            /* Animasi cahaya di background */
            body::before {
                content: "";
                position: fixed;
                width: 300px;
                height: 300px;
                background: rgba(0, 200, 255, 0.15);
                border-radius: 50%;
                filter: blur(60px);
                top: 10%;
                left: 10%;
                animation: bergerak 5s infinite alternate;
            }

            body::after {
                content: "";
                position: fixed;
                width: 300px;
                height: 300px;
                background: rgba(100, 255, 200, 0.12);
                border-radius: 50%;
                filter: blur(60px);
                bottom: 10%;
                right: 10%;
                animation: bergerak2 6s infinite alternate;
            }

            @keyframes bergerak {
                from {
                    transform: translate(0, 0);
                }
                to {
                    transform: translate(150px, 100px);
                }
            }

            @keyframes bergerak2 {
                from {
                    transform: translate(0, 0);
                }
                to {
                    transform: translate(-150px, -100px);
                }
            }

            h1 {
                font-size: 40px;
                animation: muncul 1.5s ease;
            }

            p {
                font-size: 18px;
                animation: muncul 2s ease;
            }

            img {
                width: 250px;
                height: 250px;
                object-fit: cover;
                border-radius: 50%;
                margin: 20px;
                border: 5px solid white;
                box-shadow: 0 0 30px rgba(255,255,255,0.4);
                animation: melayang 3s ease-in-out infinite;
            }

            button {
                background: white;
                color: #111;
                border: none;
                padding: 15px 30px;
                border-radius: 10px;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                transform: scale(1.1);
                box-shadow: 0 0 20px white;
            }

            @keyframes melayang {
                0%, 100% {
                    transform: translateY(0);
                }

                50% {
                    transform: translateY(-15px);
                }
            }

            @keyframes muncul {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }

                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>

    <body>

        <h1>Halo semua aku RYAN 👋</h1>

        <p>Selamat datang di website pertamaku!</p>

        <img src="/static/foto.jpg">

        <br>

        <button onclick="sapa()">
            Klik bos 🚀
        </button>

        <script>
            function sapa() {
                alert("Halo rekk! Terima kasih sudah mengunjungi website ku 😎");
            }
        </script>

    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)

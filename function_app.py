import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="ClockPage", auth_level=func.AuthLevel.ANONYMOUS)
def ClockPage(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Clock page requested.')

    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>デジタル時計</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #1a1a2e;
                font-family: 'Courier New', monospace;
            }
            #clock {
                font-size: 6vw;
                color: #00ffcc;
                letter-spacing: 0.05em;
                text-shadow: 0 0 20px rgba(0, 255, 204, 0.6);
            }
            #date {
                text-align: center;
                color: #888;
                font-size: 1.2vw;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div>
            <div id="clock">--:--:--</div>
            <div id="date">----</div>
        </div>
        <script>
            function updateClock() {
                const now = new Date();
                const h = String(now.getHours()).padStart(2, '0');
                const m = String(now.getMinutes()).padStart(2, '0');
                const s = String(now.getSeconds()).padStart(2, '0');
                document.getElementById('clock').textContent = `${h}:${m}:${s}`;

                const days = ['日', '月', '火', '水', '木', '金', '土'];
                const dateStr = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日 (${days[now.getDay()]})`;
                document.getElementById('date').textContent = dateStr;
            }
            updateClock();
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """

    return func.HttpResponse(html_content, mimetype="text/html")
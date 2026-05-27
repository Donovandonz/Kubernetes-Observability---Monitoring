from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # HTML page with an image and the environment message
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Portfolio App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f0f2f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            img {{
                max-width: 400px;
                margin: 20px 0;
                border-radius: 8px;
            }}
            .env {{
                color: #2c3e50;
                font-size: 1.2em;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello from my DevOps Project!</h1>
            <img src="https://raw.githubusercontent.com/Donovandonz/Cloud-Devops-Engineer-Portfolio-Project/main/images/devops-logo.png?raw=true" 
                 alt="DevOps Logo" 
                 onerror="this.src='https://via.placeholder.com/400x200?text=DevOps+in+Action'">
            <div class="env">
                <strong>Environment:</strong> {os.getenv('ENV', 'production')}<br>
                <strong>Status:</strong> Running
            </div>
            <p>✅ Deployed with Kubernetes + Prometheus + Grafana</p>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask
import requests
import schedule
import time
from threading import Thread
from waitress import serve

# Initialize Flask app
app = Flask(__name__)

# List of URLs to monitor
urls = [
    "https://sellstreams1.onrender.com/",
    "https://quiz-application-vzaz.onrender.com/",
    "https://sellstreams1.onrender.com/doc/",
    "https://pet-adoption-bd.onrender.com/"
]

# Monitor function to hit the URLs
def monitor_urls():
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            print(f"Hit URL: {url} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to fetch {url} - {e}")

# Schedule the monitoring every 5 minutes
schedule.every(1).minutes.do(monitor_urls)

# Route for Flask (to bind the service to a port)
@app.route('/')
def index():
    return "Monitoring URLs... Check the logs for status."

# Start monitoring in the background using a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Start the background scheduler in a separate thread
    thread = Thread(target=run_schedule)
    thread.daemon = True
    thread.start()

    # Use Waitress to serve the Flask app
    serve(app, host='0.0.0.0', port=5000)

import requests
import schedule
import time

# List of URLs to monitor
urls = [
    # "https://sellstreams1.onrender.com/",
    "https://quiz-application-vzaz.onrender.com/",
    "https://sellstreams1.onrender.com/doc/",
    "https://pet-adoption-bd.onrender.com/"
]

# Monitor function
def monitor_urls():
    for url in urls:
        try:
            # Just make the GET request without checking the status
            response = requests.get(url, timeout=10)
            print(f"Hit URL: {url} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to fetch {url} - {e}")

# Schedule the monitoring every 5 minutes
schedule.every(1).minutes.do(monitor_urls)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)

import requests
import threading

def fetch_url(url):
    response = requests.get(url)
    # Process the response data

# List of URLs to crawl
urls = ['https://site1.com', 'https://site2.com', 'https://site3.com']

# Create threads for concurrent crawling
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Process the collected data

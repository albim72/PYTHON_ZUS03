import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import requests

# Funkcja blokująca (I/O-bound), np. pobieranie pliku
def download_url(url):
    response = requests.get(url)
    return f"{url}: {len(response.content)} bajtów"

# Opakowanie funkcji sync do użycia w asyncio
async def async_download(executor, url):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, download_url, url)
    return result

async def main():
    urls = [
        "https://www.foxnews.com/",
    "https://edition.cnn.com/",
    "https://www.bbc.com/",
    "https://www.wp.pl/",
    "https://www.gov.pl/web/obrona-narodowa",
    "https://mil.ru/"
    ]
    
    # Pool wątków dla operacji I/O
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [async_download(executor, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

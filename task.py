from celery import Celery
import aiohttp
import asyncio
import pandas as pd

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

@app.task
def fetch_data_task(url):
    async def main(url):
        async with aiohttp.ClientSession() as session:
            return await fetch_data(session, url)
    
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(url))
    
    # Convert data to DataFrame
    df = pd.DataFrame(result)
    
    # Create a filename based on the URL or its index
    filename = f"output_{url.split('/')[-1]}.xlsx"
    
    # Save DataFrame to an Excel file
    df.to_excel(filename, index=False)
    
    return f"Data from {url} saved to {filename}."

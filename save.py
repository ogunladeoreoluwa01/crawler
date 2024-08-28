from task import fetch_data_task

if __name__ == "__main__":
    # Example URLs
    urls = [
        "https://fakestoreapi.com/products/category/jewelery",
        "https://fakestoreapi.com/products/category/electronics",
        "https://fakestoreapi.com/products/category/men's clothing",
        "https://fakestoreapi.com/products/category/women's clothing",
      
    ]
    
    # Submit each URL as a task to Celery
    for url in urls:
        result = fetch_data_task.delay(url)
        print(f"Task ID for {url}: {result.id}")

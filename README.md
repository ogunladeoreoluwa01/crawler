

# **How to Set Up and Run the Asynchronous API Crawler on Windows**

## **Requirements**

Before you start, ensure you have the following installed:

- Python 3.7 or higher
- The following Python libraries:
  - `celery`
  - `redis`
  - `aiohttp`
  - `pandas`
  - `openpyxl`

## **Step 1: Install Dependencies**
 **Install Python Libraries**:  
   Use `pip` to install the required libraries by running the following command in the project directory:

   ```bash
   pip install celery redis aiohttp pandas openpyxl
   ```

## **Step 2: Install and Run Redis**

1. **Download Redis for Windows**:  
   Download Redis from the [Microsoft Archive](https://github.com/MicrosoftArchive/redis/releases) and follow the installation instructions.

2. **Start the Redis Server**:
   - Open a terminal (Command Prompt or PowerShell).
   - Navigate to the folder where Redis is installed by running in a terminal:
  ```bash
  cd C:\Program Files\Redis
  ```
   - Start the Redis server by running:
     ```bash
     redis-server
     ```

## **Step 3: Set Up and Run Celery Workers**

1. **Set Environment Variable** :
   - Open another terminal and run:
     ```bash
     set FORKED_BY_MULTIPROCESSING=1
     ```

2. **Start Celery Workers**:
   - next run this to create your workers (if needed you can run the same command on multiple terminals ,aslo the comand should be done in the file directory so celey can find the module task).:
   - In each terminal, navigate to the project directory and start a Celery worker by running:
     ```bash
     python -m celery -A tasks worker --loglevel=info --concurrency=4
     ```
   - The `concurrency=4` option controls the number of worker processes. Adjust it based on your system's capabilities.

## **Step 4: Submit Tasks**

1. **Run the Task Submission Script**:
   - In the project directory, run the script to submit tasks to Celery:
     ```bash
     python save_to_excel.py
     ```
   - This script will enqueue the task, and the workers will process it, fetching data from the specified URLs and saving it as Excel files.

## **Step 5: Check the Results**

After the tasks are completed, you’ll find Excel files (e.g., `output_0.xlsx`, `output_1.xlsx`) in the project directory, each containing the data fetched from the respective URLs.(note the numbers or index can be the task name sometimes or the index of the url in the urls for example in my example api urls when outputing you will get `output_Electronics.xlsx` just as an example)



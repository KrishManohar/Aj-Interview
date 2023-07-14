## For Aj Interview (FastAPI with PyTest) For AWS Lambda

### Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required dependencies:

   ```shell
    pip install -r requirements.txt
   ```

### Running the Application

1. To run the FastAPI application locally, use the following command:

   ```shell
    uvicorn main:app --reload
   ```

You can access the application at http://localhost:8000/. It provides the following endpoints:

````
/ - Renders the index.html template.
/python - Retrieves a random Python response from a predefined list.
/reverse/{name} - Reverses the provided name and returns the letter count along with the reversed name.
````

### Running Unit Tests

1. To run the unit tests using PyTest, execute the following command:

```shell
pytest
```
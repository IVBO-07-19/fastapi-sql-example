# Fast API / SQLite example

## How to run

1. Create venv
    ```bash
        python -m venv venv
    ```
2. Activate venv
    ### Windows
    ```powershell
    .\venv\Scripts\activate 
    ```
    ### Linux/MacOS
    ```bash
    source venv/bin/activate
    ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Run app
    ```bash
    uvicorn main:app --reload
    ```
    Open docs on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
# crypto-currency-price-fastapi
Example of eventsourcing with FastAPI

## Getting Started

Clone repo for quickstart:
```zsh
git clone https://github.com/aymogo/crypto_currency
cd crypto_currency
```

Create virtual environment (optional)
```zsh
python3 -m venv venv
```


<details markdown="1">
<summary>Activate virtual environment if you created ...</summary>

Linux
```zsh
source cenc/bin/activate
```
Windows
```zsh
./venv/Scripts/activate
```

</details>


Install all backend requirements:
```zsh
pip install -r requirements.txt
```


Run the FastAPI server with:

<div class="termy">

```console
$ uvicorn src.main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>


Open local API docs [http://localhost:8000/docs](http://localhost:5000/docs)


Our server ready to work
Let's run the frontend:
```zsh
npm run dev
```

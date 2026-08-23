import requests

def ask(prompt, model="orca-mini"):
    session = requests.Session()
    session.proxies = {"http": None, "https": None}
    response = session.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
    )
    return response.json()["message"]["content"]

print(ask("Привет! Кто ты?"))
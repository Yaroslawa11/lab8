import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        return joke_data
    except requests.RequestException as e:
        print("\n" + "=" * 40)
        print("ПОМИЛКА".center(40))
        print("=" * 40)
        print(f"Не вдалося отримати анекдот.\nДеталі: {e}")
        print("=" * 40)
        return None

def main():
    joke = get_joke()
    if not joke:
        return
    print("\n" + "=" * 40)
    print(" ВИПАДКОВИЙ АНЕКДОТ".center(40))
    print("=" * 40)
    print(f" Питання: {joke['setup']}")
    print(f" Відповідь: {joke['punchline']}")
    print("=" * 40)

if __name__ == "__main__":
    main()

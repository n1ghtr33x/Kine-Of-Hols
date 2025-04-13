import requests

# URL вашего API (замените на актуальный, если сервер запущен не локально)
BASE_URL = "http://172.20.10.3:8001"

def test_version():
    try:
        response = requests.get(f"{BASE_URL}/version")
        response.raise_for_status()
        print("Version:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error fetching version:", e)

def test_register(player_name: str, password: str):
    try:
        data = {
            "player_name": player_name,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/register", json=data)
        response.raise_for_status()
        print("Register response:", response.json())
    except requests.exceptions.HTTPError as e:
        print("Registration error:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def test_login(player_name: str, password: str):
    try:
        data = {
            "name": player_name,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/login", json=data)
        print("Status code:", response.status_code)
        print("Raw response:", response.text)  # Печатаем сырой текст ответа
        response.raise_for_status()
        print("Login response:", response.json())
    except requests.exceptions.HTTPError as e:
        print("Login error:", response.text)  # Печатаем текст ошибки
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def test_update_data(data):
    try:
        data = {
            "name": data["name"],
            "password": data["password"],
            "elixir": data["elixir"],
            "gold": data["gold"],
            "gems": data["gems"]
        }
        response = requests.post(f"{BASE_URL}/update_user", json=data)
        print("Status code:", response.status_code)
        response.raise_for_status()
        print("Login response:", response.json())
    except requests.exceptions.HTTPError as e:
        print("Login error:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    # Тестовые данные
    test_player_name = "TestPlayer"
    test_password = "TestPassword123"

    # Проверка версии
    print("=== Testing version ===")
    test_version()

    # Тест регистрации
    print("\n=== Testing registration ===")
    test_register(test_player_name, test_password)

    # Тест логина с правильными данными
    print("\n=== Testing login (correct credentials) ===")
    test_login(test_player_name, test_password)

    # Тест логина с неправильным паролем
    print("\n=== Testing login (wrong password) ===")
    test_login(test_player_name, "WrongPassword")

    # Тест логина с неправильным именем
    print("\n=== Testing login (wrong username) ===")
    test_login("NonExistentPlayer", test_password)

    # Тест обновления данных
    print("\n=== Testing update data ===")
    data = {
        "name": test_player_name,
        "password": test_password,
        "elixir": 1,
        "gold": 2,
        "gems": 1
    }
    test_update_data(data)
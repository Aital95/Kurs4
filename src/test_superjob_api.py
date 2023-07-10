import requests

def test_superjob_api():
    headers = {"X-Api-App-Id": "SJAPI"}
    params = {"keyword": "python"}

    response = requests.get("https://api.superjob.ru/2.0/vacancies", headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Ошибка доступа к SuperJob API")


if __name__ == "__main__":
    test_superjob_api()

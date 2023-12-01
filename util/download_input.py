import requests
from pathlib import Path

BASE_URL = "https://adventofcode.com"
YEAR = "2023"


for day in range(1, 31):
    with open('./util/session.txt', 'r', encoding='utf-8') as fp:
        cookies = {"session": fp.read()}
    response = requests.get(
        f"{BASE_URL}/{YEAR}/day/{day}/input",
        timeout=2,
        cookies=cookies
    )
    if response.status_code != 200:
        print(f"Fetch input for day {day} resulted in {response.status_code}: {response.text}")
        break
    path = f"./{YEAR}/day{day}/input"
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f"{path}/input.txt", "w+", encoding="utf-8") as fp:
        fp.write(response.text)

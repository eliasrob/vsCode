import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

textFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(10000):
    print(chunk)

    
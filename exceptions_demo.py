import requests

url = 'https://www.crunchbase.com/'

try:
    page = requests.get(url)
    if page.status_code == 403:
        raise Exception('You are not allowed')

except Exception as e:
    print(e)
else:
    print('Worked till here')
finally:
    print('stopping the execution')
import requests

res= requests.get('https://www.wikipedia.org/') 

try:
    resultado = res.raise_for_status()
    print(res)
except Exception as exc:
    print("There was a problem: %s" % (exc))



 
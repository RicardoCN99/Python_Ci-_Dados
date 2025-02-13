import requests

url="https://pt.wikipedia.org/wiki/Wiki" 

r=requests.get(url) #pedido get ao servidor

print(r.status_code)

print(r.request.headers)

print(r.request.body)

print(r.url)

#print(r.text) # resposta do servidor

headers=r.headers
print(headers["date"])
print(headers["Content-type"])



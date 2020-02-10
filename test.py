import requests

# Let's test getting the oauth 
#etsy = OAuth1Session('client_key',
#                     client_secret=client_secret,
#                     resource_owner_key=resource_owner_key,
#                     resource_owner_secret=resource_owner_secret)

etsy = OAuth1Session('', '')

payload = {'api_key': ''}


r = requests.get("https://openapi.etsy.com/v2/listings/active",  params=payload)

print(r.status_code)

print(r.status_code == requests.codes.ok)


print(requests.codes["temporary_redirect"])


print(requests.codes.teapot)


print(requests.codes["o/"])
print(r.text)

msg = "Hello World"
print(msg)
msg = msg.lower()
print(msg)




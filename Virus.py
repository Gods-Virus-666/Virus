
import requests

print("Format must be https://github.com/ or http://github.com/")

website = input("Enter website to crawl: ")

r = requests.get(website)

print(r.text)

f = open('source_code.txt', 'w')
f.write(print(f"{r.text}"))
f.close()

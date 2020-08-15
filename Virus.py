import requests

print("Format must be https://github.com/ or http://github.com/")

website = input("Enter website to crawl: ")

r = requests.get(website)

f = open('source_code.txt', 'w')
f.write(f"{r.text}")
f.close()

source_code = open('source_code.txt', 'r')

print(source_code)

print("Complete")

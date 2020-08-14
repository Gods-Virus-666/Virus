#Virus
import requests

print("Format must be https://github.com/ or http://github.com/")
website = input("Enter website to crawl: ")

r = requests.get(website)

print(r.text)

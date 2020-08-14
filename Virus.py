#Virus
import requests

print("Format must be https://github.com/ or http://github.com/")
website = input("Enter website to crawl: ")

source_code = requests.get(website)

print(source_code.txt)

import requests

print("Format must be https://github.com/ or http://github.com/")

website = input("Enter website to crawl: ")

r = requests.get(website)

f = open('source_code.txt', 'w')
f.write(f"{r.text}")
f.close()

f = open('source_code.txt', 'r')

if f.mode == 'r':
 contents = f.read()

contents_split = contents.split()

f = open('contents_list.txt', 'w')
f.write(f"{contents_split}")
f.close()

sam = contents_split.sorted()

print(sam)

print("Complete")

import requests

print("Format must be https://github.com/ or http://github.com/")

website = input("Enter website to crawl: ")

r = requests.get(website)

with open('source_code.txt', 'w') as f:
 f.write(f"{r.text}")

with open('source_code.txt', 'r') as f:
 if f.mode == 'r':
  contents = f.read()

contents_split = contents.split("'src=")
f = open('contents_list.txt', 'w')
f.write(f"{contents_split}")
f.close()

contents_split.sort()

print(contents_split)

print("Complete")

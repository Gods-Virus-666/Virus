import requests

print("Format must be https://github.com/ or http://github.com/")

website = input("Enter website to crawl: ")

r = requests.get(website)

f = open('source_code.txt', 'w')
f.write(f"{r.text}")
f.close()

f = open('source_code.txt', 'r')

if f.mode == 'r':
 contents = f.read

contents_list = contents.spilt()

f = open('contents_list.txt', 'w')
f.write(f"{contents.split()}")
f.close()

print(contents_list)
print("Complete")

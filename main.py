import requests
from bs4 import BeautifulSoup
import time

print('Scraping data....')
x = 1
while x <= 28950:
    with open('test.txt', 'a') as outfile:
        result = requests.get(f"https://website.com/page={x}") # Website name goes here
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        stop = soup.find(class_="page-item disabled")
        for h2_tag in soup.find_all('h2'):
            strong_tag = h2_tag.find('strong')
            line = f'{strong_tag}'.replace('<strong>', '')
            string = line.replace('</strong>', '')
            if "<a class=" not in string:
                outfile.write(f'{string}\n')
        print(f'  Page: {x}', end="\r")
        time.sleep(1)
        if x > 1 and stop != None:
          print('\nEnd is reached')
          break
        x+=1


# The code below removes any duplicated lines
import hashlib

completed_lines_hash = set()
output_file = open('dups.txt', "w")
for line in open('test.txt', "r"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
print('\nThe data have been scraped')
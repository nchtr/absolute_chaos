#1
import re
fword="Python is simple programming language(no.)"
pattern = re.compile(r'\w+')
print(pattern.findall(fword)[0])


#2
import datetime
st = 'Result: Timestamp;Value;Quality;Annotation26.10.2020 17:29:15.854;123;0;26.10.2020 17:29:20.556;321;0;; Error: None'  
st.split(';')[3][10:]

print(datetime.datetime.strptime(st.split(';')[3][10:-4], '%d.%m.%Y %H:%M:%S'))


#3
print(re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7(\1)\2-\3-\4', input()))


#4 незнаю работает ли, модулей нету
import requests
from bs4 import BeautifulSoup


r=requests.get('https://translate.google.com/')
html=BS(r.content, 'html.parser')
print(html)
    
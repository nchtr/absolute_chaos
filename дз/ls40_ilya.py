import os
#1
# os.mkdir('C:\\Users\\kaloglot\\Desktop\\дз\\mp3')
# os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\audio.mp3', 'C:\\Users\\kaloglot\\Desktop\\дз\\mp3\\audio.mp3')
# os.mkdir('C:\\Users\\kaloglot\\Desktop\\дз\\flac')
# os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\audio.flac', 'C:\\Users\\kaloglot\\Desktop\\дз\\flac\\audio.flac')
# os.mkdir('C:\\Users\\kaloglot\\Desktop\\дз\\oga')
# os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\audio.oga', 'C:\\Users\\kaloglot\\Desktop\\дз\\oga\\audio.oga')
#2
# os.rename('C:\\Users\\kaloglot\\Desktop\\дз\\vasya\\kursovaya.doc', 'C:\\Users\\kaloglot\\Desktop\\дз\\vasya\\vasya_kursovaya.doc')
# os.rename('C:\\Users\\kaloglot\\Desktop\\дз\\mila\\kursovaya.doc', 'C:\\Users\\kaloglot\\Desktop\\дз\\mila\\mila_test.pdf')
# os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\vasya\\vasya_kursovaya.doc', 'C:\\Users\\kaloglot\\Desktop\\дз\\vasya_kursovaya.doc')
# os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\mila\\mila_test.pdf', 'C:\\Users\\kaloglot\\Desktop\\дз\\mila_test.pdf')
# os.rmdir('C:\\Users\\kaloglot\\Desktop\\дз\\vasya')
# os.rmdir('C:\\Users\\kaloglot\\Desktop\\дз\\mila')
#3
# alldirs=os.listdir('C:\\Users\\kaloglot\\Desktop\\дз')
# os.mkdir('C:\\Users\\kaloglot\\Desktop\\дз\\S01')
# os.mkdir('C:\\Users\\kaloglot\\Desktop\\дз\\S02')
# for need in alldirs:
#     if "S01" in need:
#         os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\'+str(need), 'C:\\Users\\kaloglot\\Desktop\\дз\\S01\\'+str(need))
#     elif "S02" in need:
#         os.replace('C:\\Users\\kaloglot\\Desktop\\дз\\'+str(need), 'C:\\Users\\kaloglot\\Desktop\\дз\\S02\\'+str(need))    
#4
# allf=os.listdir('C:\\Users\\kaloglot\\Desktop\\дз\\Pictures')
# allf.sort()
# for i in range(len(allf)):
#     os.rename('C:\\Users\\kaloglot\\Desktop\\дз\\Pictures\\'+allf[i], 'C:\\Users\\kaloglot\\Desktop\\дз\\Pictures\\'+str(i)+os.path.splitext('C:\\Users\\kaloglot\\Desktop\\дз\\Pictures\\'+allf[i])[1])
#5
import re
import csv
 
with open('C:\\Users\\kaloglot\\Desktop\\дз\\in.csv', 'r') as f_in, open('C:\\Users\\kaloglot\\Desktop\\дз\\out.csv', 'w') as f_out:
    text = f_in.read()
    all_symbols = len(text)
    all_lines = text.count('\n') + 1
    all_vowels = len(re.findall(r'(?i)[aeiouy]', text))
    all_consonats = len(re.findall(r'(?i)(?![aeiouy])[a-z]', text))
    all_digits = len(re.findall(r'\d', text))
    result = [{'str':'Всего символов: ','value':str(all_symbols)},{'str':'Всего строк: ','value':str(all_lines)},{'str':'Всего гласных: ','value':str(all_vowels)},{'str':'Всего согласных: ','value':str(all_consonats)}, {'str':'Всего чисел: ','value':str(all_digits)}]
    print(result)   
    write=csv.DictWriter(f_out, fieldnames=['str', 'value'])
    write.writeheader()
    write.writerows(result)
    
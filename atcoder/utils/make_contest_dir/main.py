import datetime
import os


str_genre = input('Please input genre. ex.)abc, arc, agc, etc. : ')
if str_genre == '':
    str_genre = 'abc'
os.makedirs(os.path.join('../../', str_genre), exist_ok=True)

str_name = ''
while str_name == '':
    str_name = input('Please input contest\'s name. ex.)abc001 : ')
os.makedirs(os.path.join('../../', str_genre, str_name), exist_ok=True)

list_suffix = list(input('Please input suffix list, default=abcd ex.) abcd, 1234, abcdef : '))
if list_suffix == []:
    list_suffix = list('abcd')

# Make blank.py
for suffix in list_suffix:
    abspath = os.path.join('../../', str_genre, str_name, '%s_%s.py' % (str_name, suffix))
    if os.path.exists(abspath) == False:
        fp_blank = open(abspath, 'w', encoding='utf-8')
        fp_blank.close()

# Make blank.md
abspath = os.path.join('../../', str_genre, str_name, '%s.md' % str_name)
if os.path.exists(abspath) == False:
    fp_blank = open(abspath, 'w', encoding='utf-8')
    fp_blank.write('# %s\n\n' % str_name)
    for suffix in list_suffix:
        fp_blank.write('## %s（%s）\n\n' % (suffix, datetime.date.today().strftime('%Y/%m/%d')))
    fp_blank.close()

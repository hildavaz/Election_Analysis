from multiprocessing import Condition
from sqlite3.dbapi2 import _Statement


print("Hello World")



counties = ['Arapahoe','Denver','Jefferson']
if counties[1] == 'Denver':
 print(counties[1])

if counties[3] != "Jefferson":
 print(counties[2])

def new_func():

temperature = int(input('What is the temperature outside?'))

if temperature > 80:
    print('Turn on the AC')

else:
    print('Open the windows')


from zipfile import ZipFile

zip_ = ZipFile('Архив.zip')
print(zip_.namelist())
text = zip_.read('example2.txt')
print(text)
zip_.close()

with ZipFile('Архив.zip') as myzip:
    myzip.extract('example2.txt')
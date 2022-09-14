with open('example.txt', 'w') as f:
    f.write('Hello world\nNew row')


# Закрывать файл вручную - антипаттерн, нужно стараться использовать контекстный менеджер
# f = open('example2.txt', 'w')
# f.write('Hello2')
# f.close()

with open('example.txt', 'r') as f:
    file = f.read()
    print(file)
    assert file == 'Hello world\nNew row'
    assert 'New' in file

def test_rows():
    with open('example2.txt', 'r') as file:
        for i in file:

            assert i == 'Hello1'
            print(i)

with open('example4_x.txt', 'x') as file:
    file.write('Hello\n')

with open('example5_x.txt', 'x') as file:
    file.write('Hello\n')
with open('example5_x.txt', 'a') as file:
    file.write('NewHello')

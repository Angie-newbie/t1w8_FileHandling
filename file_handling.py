# open a file

# file.write('This is a new file~\n')
# file.write('See ya\n')

# file.close()

with open('new_file.txt') as file:
    for line in file:
        print(line.strip())

# content = file.readline().strip()
# print(repr(content))
# content = file.readline().strip()
# print(content)

# content = file.read(10)
# print(content)
# content = file.read(5)
# print(content)


# file.close()
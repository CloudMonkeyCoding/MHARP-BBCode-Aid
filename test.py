line = 'hello Kong Panda test'
index = line.find('Panda')
output_line = 'fu' + line[:index] + 'Fu ' + line[index:] + 'end'
print(output_line)
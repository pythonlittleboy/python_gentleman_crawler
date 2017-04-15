print('Hello World!')
file_object = open('thefile.txt')
try:
    list_of_all_the_lines = file_object.readlines()
    for line in list_of_all_the_lines:
        print(">>>>>" + line);
finally:
     file_object.close()

output = open('output.txt', 'w')
output.write("h1\n")
output.write("h2\n")
output.close()
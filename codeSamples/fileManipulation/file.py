import os
print(os.getcwd())
os.chdir('JustCreated') #changing to the JustCreated directory

opener = open('my_file.txt', 'r+') #opening the file
#reader = opener.read() #reading the file content at once
for the_data in range(8):
	reader = opener.readline() #reading the file line by line
	#reader = reader.rstrip('\n') removing '\n' characters if needed
	print(reader,end = '')

opener.close()
#using the tell() function to control the pointer within the file

new_file = open('my_file.txt', 'r+')
print("\n")
print(new_file.tell())

for the_data in range(2):
    file_reader = new_file.readline()
    print(file_reader, end='')
    print(new_file.tell())
    print(new_file.seek(new_file.tell()))

new_file.close()

#----writing to a file----
print("-----------------------\n")
file1 = open('my_file.txt', 'a+')
print(file1.tell())
new_content = "This line was added from a script"
file1.write("\n" + new_content)
#adding content to the top
file1.seek(0)
print(file1.tell())


# the book.txt file that contain each book and it title,
# book.txt was open with python  open() buit-in function ,
# (with) precede (open) was used to closed the book.txt after reading it
# (as)  assign  already opened book.txt to reader

with open("Book.txt", "r") as reader:

# readline() function was used to read each line of Book.txt 
	book1_title = reader.readline()
	book1 = reader.readline()
	print(book1_title)
	print(book1)
	print("----"*5)

#readline() function was used to read each line of Book.txt 
	book2_title = reader.readline()
	book2 = reader.readline()
	print(book2_title)
	print(book2)
	print("----"*5)

#readline() function was used to read each line of Book.txt 
	book3_title = reader.readline()
	book3 = reader.readline()
	print(book3_title)
	print(book3)
	print("----"*5)

# len() function find the length of each book character with white space
	len_book1 = len(book1) - 1
	len_book2 = len(book2) - 1
	len_book3 = len(book3) - 1

# book[0], book2[0], book[0] correspond to the first character in each book
# note length of each book is an integers ,and need to cast to string before you can concantenate it with
#  each book was concantenate with it correspond number of character

	code1 = book1[0] + str(len_book1)
	code2 = book2[0] + str(len_book2)
	code3 = book3[0] + str(len_book3)

	print(f"Book1 code: {code1}\n")
	print(f'Book2 code: {code2}\n')
	print(f'Book3 code: {code3}\n')

	
	


	
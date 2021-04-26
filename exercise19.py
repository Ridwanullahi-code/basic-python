import re 
def text_match(text):
	patterns = re.compile(r'\Bz\B')
	if patterns.search(text):
		return "Found a match"
	else:
		return "Not found"
print(text_match("The quick brown for jumps over the lazy dog."))
print(text_match("the ptryt hojmgh"))

def email_match(email):
	pattern = re.compile(r'\w+\@\w+\.\w+')
	if pattern.search(email):
		return "You input valid email address"

	else:
		return "invalid email address"
print(email_match("ajayiridwanullahi01@gmail.com"))
print(email_match("ajayiridwanullahi.com"))

def match(string):
	pattern = re.compile(r'ab{3}')
	if pattern.search(string):
		return"the string is found"
	else:
		return "not found"
print(match("abbb"))
print(match("abbbb"))
print(match("abbbbbb"))

def match2(string2):
	pattern = re.compile(r"^ab{2,3}")
	if pattern.search(string2):
		return "correct"
	else:
		return "incorrect"
print(match2("abbbbbb "))

def match3(string3):
	pattern = re.compile(r"^[a-z]+_[a-z]+$")
	if pattern.search(string3):
		return "found"
	else:
		return "not found"
print(match3("aaa_bbbcd"))
print(match3("abgd_hhhbjs"))

def text_match(text):
	pattern = re.compile(r"[A-Z][a-z]+")
	if pattern.search(text):
		return  "valid"
	else:
		return "not found"
print(text_match("Aabbb"))




	 	

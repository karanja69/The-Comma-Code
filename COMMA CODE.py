spam = ['apples','bananas','tofu','cats']
def things(list):
	newspam = ','.join(list).rsplit(',',1)
	newspam = ' and '.join(newspam)
	return newspam
print(things(spam))

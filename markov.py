from os import listdir
from shutil import copyfileobj
import markovify


a = 0  # Number of total lines in all files
b = -1  # Number of files

path = 'C:/Users/Will Bennett/Documents/Code/web-crawler/saved/'
# path = 'files/'

with open('text.txt', 'w+') as f:
	results = listdir(path)
	for file in results:
		if file.endswith('.html'):
			b += 1
			try:
				with open(path + file, encoding="utf-8") as open_file:
					try:
						print('Digesting "{0}"'.format(file))
						copyfileobj(open_file, f)
					except UnicodeError:
						print('Unknown encoding on file.')
			except FileNotFoundError:
				print('Invalid file name "{0}"'.format(file))

print('Reading huge_text.txt')
with open('huge_text.txt', 'r') as f:
	model = markovify.Text(f, retain_original=False)

print('Saving model to model.json')
with open('model.json', 'w+') as f:
	f.write(model.to_json())

print('Writing to markov1_nl.html')
with open('markov1_nl.html', 'w+') as f:
	for i in range(600):
		f.write(model.make_sentence(tries=100))

with open('words.txt', 'r') as fin:
	words = fin.readline().strip()

words_lst = words.split()

words_dict = {}

count = 0
for idx, word in enumerate(words_lst):
	if word not in words_dict:
		words_dict[word] = (1, count)
		count += 1
	else:
		words_dict[word] = (words_dict[word][0]+1, words_dict[word][1])

count = 0
with open('Q1.txt', 'w') as fout:
	for key, value in words_dict.items():
		if count == len(words_dict):
			fout.write(key + ' ' + str(value[1]) + ' ' + str(value[0]))
		else:
			fout.write(key + ' ' + str(value[1]) + ' ' + str(value[0]) + '\n')
		count += 1
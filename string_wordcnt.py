import re

def parse(text,word_cnt):
	text = text.lower()
	word_list = re.findall(r'\w+',text)
	for word in word_list:
		word_cnt[word] = word_cnt.get(word,0)+1
		print(word_cnt.get(word,0))
	return word_cnt

if __name__ == '__main__':
	word_cnt = {}
	with open('in.txt','r') as fin:
		for text in fin.readlines():
			word_fre = parse(text,word_cnt)
		print(word_fre)
	sorted_word_list = sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)

	with open('out.txt','w') as fout:
		for word,fre in sorted_word_list:
			fout.write('{} {}\n'.format(word,fre))
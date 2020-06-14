import re

class String_NLP(object):
	def parse(self,text):
		#使用正则表达式去除标点符号和换行
		text = re.sub(r'[\W]',' ',text)
		#转换成小写
		text = text.lower()
		#生产所有单词的列表
		word_list = text.split(' ')
		#去除空白单词
		word_list = filter(None,word_list)
		#生成单词和出现频率的字典
		word_cnt = {}
		for word in word_list:
			if word not in word_cnt:
				word_cnt[word] = 0
			else:
				word_cnt[word] += 1

		#按照词频排序
		sorted_word_list = sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)
		return sorted_word_list



if __name__ == '__main__':
	nlpobj = String_NLP()
	with open('in.txt', 'r') as fin:
		#text = fin.read()
	#word_and_freq = nlpobj.parse(text)
		for text in fin.readlines():
			word_and_freq = nlpobj.parse(text)
		print(word_and_freq)

	with open('out.txt', 'w') as fout:
		for word, freq in word_and_freq:
			fout.write('{} {}\n'.format(word, freq))
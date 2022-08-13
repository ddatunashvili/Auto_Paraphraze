# -*- coding: utf-8 -*-

# import filter as flt

import random
import pprint

import re
# filtered_text = flt.filter()


# 												პარაგრაფების შექმნა
def structurize(filtered_text):
	# 1162 წინადადება დაიყო 2-2 წინადადებად (გავაერთიანეთ)
	# print(len(filtered_text))

	paragraphs = []
	sentence = []
	counter = 0
	for i in filtered_text:
		counter += 1
		if counter  <= 2:
			sentence.append(i)
		else:
			paragraphs.append(sentence)
			counter = 0
			sentence = []
		

	print("----------")
	# 2-2 წინადადება
	# print(len(paragraphs))


	# 										პარაგრაფების დამუშავება


	perafrasis = {}
	p_number = 0
	for paragraph in paragraphs:
		# პირველი წინადადება 
		coma_words = paragraph[0].split(",")

		# მეორე წინადადება დავშალე
		coma_words_2 = paragraph[1].split(",")

		# მეორე წინადადება 
		coma_words2 = paragraph[1].split(",")

		# წინადადების სტრუქტურა
		try:
			# მარტივი 2 მძიმიანი
			first_sentence = coma_words[0] + coma_words[1]
			second_sentence = coma_words2[0] + coma_words2[1]

			# რთული
			try:
				# სამ მძიმიანი
				first_sentence +=  coma_words[2]
				second_sentence +=  coma_words2[2]
			except:
				pass

		except:
			first_sentence = paragraph[0]
			second_sentence = paragraph[1]

		# პირველი წინადადება
		# perafrasis[p_number] = first_sentence

		first_sentence = re.sub('\W+\n',"", first_sentence)
		second_sentence = re.sub('\W+\n',"", second_sentence)


		# wordlists
		wordlist = coma_words[-2:] + coma_words_2[:2]
		
		wordlist = "".join(wordlist).split()


		# keywords gen and gramar words filter 
		keywords = []
		for i in wordlist:
			if len(i) > 5:
				i = re.sub('\W+','', i)
				if "რატომ" not in i and "იმიტომ" not in i and "როგორ" not in i and " და " not in i and "პირველი" not in i and "საჭირო" not in i and "საქმე" not in i and "ერთნაირ" not in i and "შესახე" not in i and "განვი" not in i and "ვიტყ" not in i and "ვამბ" not in i and "რადგ" not in i and "მხოლო" not in i and "რაკი" not in i:
					

					keywords.append(i)

		# randomize keywords
		try:
			keywords = random.sample(keywords,2 )
		except:
			keywords = random.choice(keywords)


		perafrasis[p_number] = {
			"first_sentence":first_sentence,
			"keywords":keywords,
			"second_sentence":second_sentence
		} 
		p_number += 1

	pprint.pprint(perafrasis)

		











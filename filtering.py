'''
ტექსტი txt
	- ზედმეტი სიმბოლოების მოშორება
	- სარჩევების და .. რაღაცების მოჭრა
	- კონკრეტული თემის ამოღება
    
'''
import re  # regex - regular expresion for finding filtering text

def filter():
    with open("pages.txt", "r", encoding="utf-8") as f:
        txt = f.read()
        # 38 დან რადგან სარჩევია მანამდე
        sentences = txt.split(". ")[38:]
        # print(paragraphs[102]) sentence 102

    #  text from title
    topic_text = []
    coping = False
    for sentence in sentences:


        # სადამდე # მხოლოდ მაშინ ეძებოს როცა კოპირება დაწყებულია
        if """განმარტებები""" in sentence and coping == True:
            break
        # საიდან # ტექსტი დაგვჭირდა
        if """ტრადიციულად მეცამეტე მოციქულად""" in sentence:
            coping = True
            print("ok")
        # კოპურ
        if coping == True:
            topic_text.append(sentence)

    # print(topic_text)

    clean_text = [i.replace("/[^.,a-zA-Z0-9]/g", '') for i in topic_text]
    print(clean_text)

    return clean_text
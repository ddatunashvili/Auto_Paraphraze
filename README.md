### Auto Paraphraze 
                **ავტომატური კონსპექტის შემქმნელი**

#### სტრუქტურა
----------
	აბზაცი
	keywords უნიკალური
	აბზაცის დასკვნა
--------
`ნოუთები პარაგრაფის ნომერის მიხედვით`
```python
perafrasis[p_number] = {
			"first_sentence":first_sentence,
			"keywords":keywords,
			"second_sentence":second_sentence
		} 
```
-----

#### requirements 
* უნდა დავაყენოთ [პითონი](python.org)
* PyPDF2 მოდული ( pip install pypdfd2 )
* pprint მოდული ( pip install pprint )

#### ინსტრუქცია
```bash
python main.py
python3 main.py
```

`! თუ მოდულების დაყენების შემდეგ არ გაეშვა`
```bash
pip install -r requirements.txt
```
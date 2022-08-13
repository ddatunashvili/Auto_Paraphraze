

# pip freeze > requrements.txt    or pip3 freeze > requrements.txt 
# pip install -r requirements.txt


import pdf_txt as pt

import filtering as flt

import structurize as structure




pt.pdf_txt()

filtered_text = flt.filter()

structure.structurize(filtered_text)
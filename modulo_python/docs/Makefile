all: html

html:
	jupyter nbconvert  *.ipynb --to slides --output-dir=html
pdf:
	jupyter nbconvert  *.ipynb --to pdf --output-dir=pdf
view:
	jupyter nbconvert *.ipynb --to slides --output-dir=slides --post serve


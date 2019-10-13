all: slides

slides:
	jupyter nbconvert *.ipynb --to slides --post serve

pdf:
	jupyter nbconvert  *.ipynb --to pdf

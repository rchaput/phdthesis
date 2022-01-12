pdf:
	R -q -e 'library(bookdown); bookdown::render_book("index.Rmd", "thesisdown::thesis_pdf", output_dir = "_book/pdf")'

gitbook:
	R -q -e 'library(bookdown); bookdown::render_book("index.Rmd", "thesisdown::gitbook", output_dir = "_book/gitbook")'

serve:
	R -q -e 'library(bookdown); bookdown::serve_book(output_dir = "_book/serve")'

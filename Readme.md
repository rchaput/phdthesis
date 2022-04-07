# Remy Chaput's PhD Thesis

This repository holds the source files (RMarkdown + Bookdown) for the thesis.

## Compiling

`make pdf` produces the PDF file (single file) at `_book/thesis.pdf`

`make gitbook` produces a HTML book (multiple files) at `_book/gitbook/index.html`

`make serve` can be used to live preview the modifications. The thesis will be
built at `_book/serve/` (similar to the `gitbook` format), and re-built each
time a file is modified. The book can be previewed using either the RStudio
Viewer, or any Web browser (the URL of the server is displayed in the console).

## Requirements

A Python virtual environment must be installed in a `.venv` folder, at this
project's root.
The virtualenv must contain the libraries listed in `python-requirements.txt`, 
e.g., by using `pip install -r python-requirements.txt`.
To avoid using a virtual env, comment the line 
`reticulate::use_virtualenv(file.path(getwd(), ".venv"))` in the `setup`
chunk of `index.Rmd`. However, the `reticulate` library **must** find a
Python version with the required libraries, otherwise the book cannot be
produced.

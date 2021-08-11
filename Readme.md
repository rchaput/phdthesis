# Remy Chaput's PhD Thesis

This repository holds the source files (RMarkdown + Bookdown) for the thesis.

## Compiling

`make pdf` produces the PDF file (single file) at `_book/thesis.pdf`

`make gitbook` produces a HTML book (multiple files) at `_book/gitbook/index.html`

`make serve` can be used to live preview the modifications. The thesis will be
built at `_book/serve/` (similar to the `gitbook` format), and re-built each
time a file is modified. The book can be previewed using either the RStudio
Viewer, or any Web browser (the URL of the server is displayed in the console).

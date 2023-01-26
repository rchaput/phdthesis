PREVIEW ?= FALSE              ## Whether to avoid compiling the whole book in `serve`.
OUTPUT_PDF ?= _book/pdf       ## Output directory when compiling the PDF book.
OUTPUT_HTML ?= _book/gitbook  ## Output directory when compiling the HTML book.
OUTPUT_ALL ?= _book/all       ## Output directory when compiling both PDF and HTML.


## ┌───────────────────────────────────────────────────────────────────┐
## │                      Building the manuscript                      │
## │ ───────────────────────────────────────────────────────────────── │
## │ Important commands: "make pdf", "make gitbook", "make all"        │
## └───────────────────────────────────────────────────────────────────┘


help: ## Show this help.
# regex for general help
	@sed -ne "s/^##\(.*\)/\1/p" $(MAKEFILE_LIST)
# regex for makefile commands (targets)
	@printf "────────────────────────`tput bold``tput setaf 2` Make Commands `tput sgr0`────────────────────────────────\n"
	@sed -ne "/@sed/!s/\(^[^#?=]*:\).*##\(.*\)/`tput setaf 2``tput bold`\1`tput sgr0`\2/p" $(MAKEFILE_LIST)
# regex for makefile variables
	@printf "────────────────────────`tput bold``tput setaf 4` Make Variables `tput sgr0`───────────────────────────────\n"
	@sed -ne "/@sed/!s/\(.*\)?=\(.*\)##\(.*\)/`tput setaf 4``tput bold`\1:`tput setaf 5`\2`tput sgr0`\3/p" $(MAKEFILE_LIST)


pdf:  ## Build the PDF manuscript only.
	R -q -e 'bookdown::render_book("index.Rmd", "thesisdown::thesis_pdf", output_dir = "$(strip $(OUTPUT_PDF))")'


gitbook:  ## Build the HTML manuscript only.
	R -q -e 'bookdown::render_book("index.Rmd", "thesisdown::thesis_gitbook", output_dir = "$(strip $(OUTPUT_HTML))")'


# Using the same folder allows the HTML version to link to the PDF for downloading.
all:  ## Build both PDF and HTML manuscripts (in the same folder).
	R -q -e 'bookdown::render_book("index.Rmd", c("thesisdown::thesis_pdf", "thesisdown::thesis_gitbook"), output_dir = "$(strip $(OUTPUT_ALL))"); warnings()'


# `preview=FALSE` forces to recompile the whole book, which avoids some bugs,
# but costs more time. This is fine during the first steps of writing, because
# the book is still small, but should be disabled in later steps.
# Use `make serve PREVIEW=TRUE` to disable it.
serve:  ## Live preview (with auto-reload) of the HTML book.
	R -q -e 'bookdown::serve_book(output_dir = "_book/serve", preview = $(PREVIEW))'


clean:  ## Remove compiled files (intermediate files are kept).
# `_book` contains the produced files; `thesis.log/lol` are produced by LaTeX.
	rm -rf _book/ thesis.log thesis.lol


purge: clean  ## Remove all produced files, including intermediate caches and figures.
	rm -rf _bookdown_files/

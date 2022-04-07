# By default, compile the whole book in `serve`.
PREVIEW=FALSE


# Build only the PDF in its specific folder.
pdf:
	R -q -e 'library(bookdown); bookdown::render_book("index.Rmd", "thesisdown::thesis_pdf", output_dir = "_book/pdf")'

# Build only the book (HTML) in its specific folder.
gitbook:
	R -q -e 'library(bookdown); bookdown::render_book("index.Rmd", "thesisdown::thesis_gitbook", output_dir = "_book/gitbook")'

# Build both PDF and HTML, in the same folder. Thus, the HTML version links to the PDF for downloading.
all:
	R -q -e 'library(bookdown); bookdown::render_book("index.Rmd", c("thesisdown::thesis_pdf", "thesisdown::thesis_gitbook"), output_dir = "_book/all"); warnings()'

# Note: we set `preview=FALSE` to try and avoid some bugs when the recompiled file has not the same name as the original (???)
# e.g., "02-positioning.Rmd" is compiled as "03-positioning.html", which means that the updated website shows no difference...
# We must manually navigate to "03-positioning.html" to discover the updated changes.
# `preview=FALSE` forces to recompile the *whole* website each time a change is detected.
# This is fine during the first steps of writing, because the book is still small. Maybe we will have to disable it later.
# Use `make serve PREVIEW=TRUE` to disable it.
serve:
	R -q -e 'library(bookdown); bookdown::serve_book(output_dir = "_book/serve", preview = $(PREVIEW))'

# Deploy the whole website (HTML+PDF, see `all`) to a remote server.
# `make all` should be called before (not set as a prerequisite here to avoid forcing recompilation each time).
# Variables $USER, $HOST, $PORT, $DIR should be set.
deploy:
	[ "$(REMOTE_USER)" != "" ]
	[ "$(REMOTE_HOST)" != "" ]
	[ "$(REMOTE_DIR)" != "" ]
	rsync --delete --recursive _book/all/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_DIR)

# Remove compiled files. `_book` contains the produced files, `thesis.log/lol` are produced by LaTeX.
# Intermediate files (cache, figures) in `_bookdown_files` are not removed.
clean:
	rm -rf _book/ thesis.log thesis.lol

# Remove all produced files, including intermediate caches and figures.
purge: clean
	rm -rf _bookdown_files/

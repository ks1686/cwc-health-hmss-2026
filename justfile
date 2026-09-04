# Paper repo task runner. CI runs the same compile check.
#
#   just build   compile main.tex → main.pdf
#   just check   what CI enforces before merge
#   just clean   remove LaTeX aux files
#   just ship    check, then open the local pre-push review gate

set shell := ["bash", "-uc"]

export PATH := "/Library/TeX/texbin:" + env_var("PATH")

_default:
    @just --list --unsorted

# Compile the IEEE manuscript (pdfLaTeX + BibTeX via latexmk).
build:
    latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
    @test -f main.pdf
    @ls -lh main.pdf

# Same compile CI runs. Use this before push.
check: build
    @echo "✓ latexmk ok"

# Record a passed review so the genv pre-push gate opens.
ship: check
    @~/.config/genv/git/review-record.sh -- just check

# Remove aux / PDF build products (PDF is gitignored).
clean:
    latexmk -C
    @echo "✓ cleaned"

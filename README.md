# PHYSICS BOOK

This is an open-source project to all Physics TA at UBC Okanagan. This book manages the files and questions related to the PHYS122 Lab. Another development for PHYS112 labs will be in progress in September 2021.

## Usage

### Building the book

If you'd like to develop on and continue to build the phys-book book, you should:

- Clone this repository.
- Please use conda as the package manger. Install miniconda as instructed on their website [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
- After isntallation, run `conda env create -f environment.yml`
- (Recommended) Remove the existing `phys-book/_build/` directory
- Run `jupyter-book build phys-book/`

A fully-rendered HTML version of the book will be built in `phys-book/_build/html/`.

### Hosting the book

The html version of the book is hosted on the `gh-pages` branch of this repo. A GitHub actions workflow has been created that automatically builds and pushes the book to this branch on a push or pull request to main.

If you wish to disable this automation, you may remove the GitHub actions workflow and build the book manually by:

- Navigating to your local build (projet root); and running,
- `ghp-import -n -p -f phys-book/_build/html`

This will automatically push your build to the `gh-pages` branch. More information on this hosting process can be found [here](https://jupyterbook.org/publish/gh-pages.html#manually-host-your-book-with-github-pages).

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/thuanGIT/phys_book/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

# phys-book

This book manages the files and questions related to the labs

## Usage

### Building the book

If you'd like to develop on and build the phys-book book, you should:

- Clone this repository and run
- Run `pip install -r requirements.txt` if you are using venv to create virtual environment.
- If you are using Conda as package manager, run `conda env create -f environment. yml`
- (Recommended) Remove the existing `phys-book/_build/` directory
- Run `jupyter-book build phys-book/`

A fully-rendered HTML version of the book will be built in `phys-book/_build/html/`.

### Hosting the book

The html version of the book is hosted on the `gh-pages` branch of this repo. A GitHub actions workflow has been created that automatically builds and pushes the book to this branch on a push or pull request to main.

If you wish to disable this automation, you may remove the GitHub actions workflow and build the book manually by:

- Navigating to your local build; and running,
- `ghp-import -n -p -f phys-book/_build/html`

This will automatically push your build to the `gh-pages` branch. More information on this hosting process can be found [here](https://jupyterbook.org/publish/gh-pages.html#manually-host-your-book-with-github-pages).

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/thuanGIT/phys_book/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

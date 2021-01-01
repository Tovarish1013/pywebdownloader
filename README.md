# PYWEBDOWNLOADER (PWL)

PWL is a program for simplifying the process of downloading webpages and their corresponding assets.  You can use it to look "under the hood" of the websites who's features you would like to learn from.

PWL downloads HTML, CSS & JS assets and stores them on your local drive.

## Installation

You need to have python (and pip) installed to use this program.

Navigate (cd) to the directory where you want install PWL.  Open terminal window and type:

```bash
pip install git+https://github.com/Tovarish1013/pywebdownloader.git
```

## Usage
Navigate to the installation directory.  NOTE: Running the program from another directory will create a 'Downloads' folder at that location.

Open terminal window and type:
```bash
pywebcopy
```

Copy & Paste the webpage URL.

## Exceptions
Some website do not allow scraping of their data with robots.txt.
Exact URL is required and re-directs will not work with this program.  For best results navigate to the webpage with your browser and copy/paste the URL from the address bar.

## pywebcopy
This program is powered by a 3rd party python library: pywebcopy
https://pypi.org/project/pywebcopy/


## License
[MIT](https://choosealicense.com/licenses/mit/)
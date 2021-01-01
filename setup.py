from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

# https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup(
    name = 'pywebdownloader',
    description = 'Simple CLI app for downloading website assets',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = install_requires,
    python_requires = '>=3.6',
    entry_points = {
        'console_scripts': [
            'pywebdownloader = webdownloader.__main__:main'
        ]},
    author = 'Nikolai Chkhenkeli',
    long_description=README,
    long_description_content_type="text/markdown"  
    )
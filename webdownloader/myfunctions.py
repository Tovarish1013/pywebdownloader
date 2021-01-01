from pywebcopy import exceptions, save_webpage  # https://pypi.org/project/pywebcopy/
import validators # https://validators.readthedocs.io/en/latest/
from urllib.request import Request, urlopen
import urllib.error

# pywebcopy module that saves & zips webpages
def save_page(url):
    # TEST VERSION 2
    try:
        save_webpage(url, project_folder='downloads')
    except exceptions.AccessError as e:
        print(e)
        return False
    except:
        print('Sorry, something went wrong :(')
        return False
    else:
        return True

# Function to validate URL.  Returns true OR message
def validate_url(url):
    if not validators.url(url):
        return 'Invalid URL.'
    # https://stackoverflow.com/questions/11983049/python-read-and-validate-input-url
    req = Request(url)
    try:
        urlopen(req)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            return 'Failed to reach server. Please check URL. Reason: ' + str(e.reason)
        else:
            return '1 - There was a problem. Please check URL and try again.'
    except:
        return '2 - There was a problem. Please check URL and try again.'
    else:
        return True
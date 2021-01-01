# source env/bin/activate

from .myfunctions import save_page, validate_url

# MAIN FUNCTION
def main():
    # get url from user
    url = input('Enter webpage URL: ')
    print('URL: ', url)
    # validate url
    url_message = validate_url(url)
    if not url_message == True:
        print(url_message)
        return main()
    
    # download page
    saved = save_page(url)
    if saved == False:
        return main()
    else:
        pass

if __name__ == '__main__':
    main()
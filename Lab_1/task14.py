
def non_empty(func):
    def wrapper():
        pages = func()
        for page in pages:
            if page == '' or page == None:
                pages.remove(page)
        return pages
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())
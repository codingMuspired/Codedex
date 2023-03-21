#wiki_search.py

#searches through wikipedia using a module

import wikipedia

search_phrase = input('Please enter a phrase to search: \n')

print(wikipedia.search(search_phrase))
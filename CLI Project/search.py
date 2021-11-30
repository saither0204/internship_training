import click
import urllib, json

url = 'http://openlibrary.org/search.json?'
click.echo('\n******************* Open Library Search Portal on a CLI *******************\n')
book_name = click.prompt('Please enter the book name you want to search:- ')
click.echo("\nYou have entered the book name:- "'\n'+book_name+'\n')

string_div = book_name.replace(" ","+")

import urllib.request, json 
with urllib.request.urlopen(url+'q='+string_div) as url:
    data = json.loads(url.read().decode())
for i in range(8):
    print(data['docs'][i]['title'])


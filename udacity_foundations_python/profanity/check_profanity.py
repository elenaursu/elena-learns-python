from urllib import request, parse

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    return contents_of_file

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + parse.quote(text_to_check)
    connection = request.urlopen(url)
    output = connection.read()
    #print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert!")
    elif b"false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

contents_of_file = read_text()
check_profanity(contents_of_file)

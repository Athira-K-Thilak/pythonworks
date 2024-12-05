

from json import load

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\books.json")

data=load(f)

# for book in data:

    # print(book)

all_titles=[book.get("title") for book in data]

# print(all_titles)

#print book with pages < 250

page_filter=[book.get("title") for book in data if book.get("pages")<250]

# print(page_filter)

#print all genres

all_genres=[book.get("genre") for book in data ]

# print(set(all_genres))

genre_count={genre:all_genres.count(genre) for genre in all_genres}

# print(genre_count)

#print costly book

costly_book=max(data,key=lambda d:d.get("price"))

# print(costly_book)

#author with more than one book
    
all_authors=[author.get("author") for author in data]

author_count={author:all_authors.count(author) for author in all_authors}

# author_with_more_book=[author for author in author_count if all_authors.count(author)>1]

# print(author_with_more_book)

print([k for k,v in author_count.items() if v>1])
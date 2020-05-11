import json
import re
import random

testFile = open("isbndb-data.json")
data = json.load(testFile)


l = []
with open("data.txt", "w") as file:
    for i in range(len(data['data'])):
        # print i
        isbn13 = data['data'][i]['isbn13']
        isbn10 = data['data'][i]['isbn10']
        title = data['data'][i]['title']
        
        try:
            author = data['data'][i]['author_data'][0]['name']
        except:
            author = 'John Doe'
        publisher = data['data'][i]['publisher_text']
        try:
            year = int(re.search(r'\d+', data['data'][i]['edition_info']).group())

        except:
            try:
                year = int(re.search(r'\d+', data['data'][i]['publisher_text']).group())
            except:
                year = random.randint(1970,2014)
        num_copies = 1
        price = round(random.uniform(20.0, 80.0), 2)
        try:
            book_format = re.search(r'Hardcover', data['data'][i]['edition_info']).group()
        except:
            book_format = 'Paperback'
        keyword = (data['data'][i]['summary'][:250] + '...') if len(data['data'][i]['summary'])> 250 else data['data'][i]['summary']
        try:
            book_subject = data['data'][i]['subject_ids'][0]
        except:
            book_subject = 'General'

        statement = "INSERT INTO book VALUES ('" + str(isbn13)+ "','" +str(isbn10) + "','" + title + "','" + author + "','" + publisher + "'," + str(year) + "," + str(num_copies) + "," +  str(price) + ",'" +  keyword + "','" + book_subject + "','" +  book_format + "');"
        # print(statement)
        file.write(statement)
        file.write("\n")
    

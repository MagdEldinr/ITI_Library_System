import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from faker import Faker
from Book.models import Book, Topic
from Author.models import Author

fakegen = Faker()

topics=['literature', 'History', 'Religion', 'Education', 'Comedy', 'SiFi', 'Digital Design', 'Engineering', 'Drama', 'Romance', 'Marketing', 'Computer Science', 'Economy']
STATUS_FIELDS = ['P', 'W', 'D']
def add_topic():
    return Topic.objects.get_or_create(name=random.choice(topics))[0]

def populate(N=10):
    for i in range(N):

        # Create fake data for that entry

        # Topic data
        new_topic = add_topic()

        # Book data
        book_publish_date = fakegen.date()
        book_title = fakegen.catch_phrase()
        book_number_of_pages = fakegen.random_int(min=0, max=5000, step=1)
        book_status = fakegen.random_elements(elements=('P', 'W', 'D'), unique=False, length=1)[0]

        # Author Data
        author_name = fakegen.name()
        author_email = fakegen.ascii_email()
        author_nationallity = fakegen.country()

        # Create the new Author
        new_author = Author.objects.get_or_create(name=author_name, email=author_email, nationallity=author_nationallity)[0]

        # Create fake access record for that Topic
        new_book = Book.objects.get_or_create(title=book_title, publish_date=book_publish_date,
         number_of_pages=book_number_of_pages, status=book_status, author=new_author, topic=new_topic)[0]

if __name__ == "__main__":
    print("Populating..")
    populate(25)
    print("Done")            
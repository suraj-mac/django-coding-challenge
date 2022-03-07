# Django Coding Challenge
You can complete this coding challenge by creating a python virtual environment or by creating a Dockerfile and docker-compose.yml file to run the environment.

The application is a work in progress that houses authors, articles, and associated data. Currently, a user can navigate to the following URLS to access information.
- `http://localhost:8000/articles/` --> list of first 50 published articles
- `http://localhost:8000/articles/<year>/` --> articles published in corresponding year
- `http://localhost:8000/articles/<year>/<month>/` --> articles published in the corresponding year/month
- `http://localhost:8000/articles/<pk>/` --> single view of article based on the pk (primary key)

There are open GitHub issues with user reports and feature requests that need to be addressed. Please create a pull request that addresses these issues.

Along with the open GitHub issues, some files you interact with are in dire need of refactoring because they do not adhere to the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) or good desgin in general. Using class inheritance is a good approach and is strongly encouraged during this refactoring.

We have included a sqlite (`db.sqlite3`) database that has been prepopulated with random data. The library and code to generate this test data is provided below.

## Test Data Generation Process

```python

from faker import Faker
from authors.models import Author
from articles.models import Genre, Article

fake = Faker()

for _ in range(10000):
    Author.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        pseudonym=fake.name(),
    )

Genre.objects.create(name='Advocacy')
Genre.objects.create(name='Ambush')
Genre.objects.create(name='Online')
Genre.objects.create(name='Trade')
Genre.objects.create(name='Political')
Genre.objects.create(name='Environmental')
Genre.objects.create(name='Fashion')
Genre.objects.create(name='Society')
Genre.objects.create(name='Community')

for _ in range(100000):
    Article.objects.create(
        title=fake.color_name() + ' ' + fake.company(),
        sub_title=fake.color(),
        genre=Genre.objects.order_by('?').first(),
        content=fake.text(),
        author=Author.objects.order_by('?').first(),
        published=fake.date_time_this_decade(),
    )

for _ in range(25000):
    article = Article.objects.order_by('?').first()
    article.published = None
    article.save()

```

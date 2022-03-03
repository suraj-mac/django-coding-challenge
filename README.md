# Test Data Generated With

```python

from faker import Faker
from authors.models import Author
from articles.models import Genre, Article

fake = Faker()

for i in range(10000):
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
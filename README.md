Random article getter
=====
Lymarenko Lev - lymarenko.lev@gmail.com

----

### Get random article from main page of sites:
+ https://tv.rbc.ru/
+ https://meduza.io


### How to use?
```python
from random_article import get_random_article
my_artcile = get_random_article(<function that returns list of articles>)
```

#### For example:

```python
from random_article import get_random_article, get_rbc_articles
my_article = get_random_article(get_rbc_articles)
```

```python
from random_article import get_random_article, get_meduza_articles
my_article = get_random_article(get_meduza_articles)
```
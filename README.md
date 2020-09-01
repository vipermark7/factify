# factify
A simple Django app that returns a quote from the Fact Sphere when you refresh the page

I added quotes from the Fact Sphere from a bit of parsed HTML from the Portal wiki, and I saved them as Quotes from the manage.py shell (python3 manage,py shell from the root directory, similar to how it was done in [Part 2 of the official Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

# Main steps to recreating this app 
* Run ```django-admin startproject factify```, switch directories into factify/, and then do ```django-admin startapp info```. This will create a directory called factify/, which contains the important files settings.py and urls.py, and info/, which has views.py and models.py
* Make sure that you have the appropriate content in urls.py (importing the views from your app and having a root view, for example) 
* Put the name of your app in settings.py under INSTALLED_APPS
* For our simple app, we just have a Quote model with a field called text, which has the actual text of the quote
* Run makemigrations and migrate with manage.py 
* Open the Django shell (```python manage.py shell```),


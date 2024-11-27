ECOMMERCE PROJECT

To create a virtual environment , we use this code:
  pyhton  -m venv .venv

  We then activate the virtual environment:
    .\.venv\Scripts\Activate.ps1

Then we install django using :
  pip install django

Once django is intalled we start the ecommerce project:
  django-admin startproject ecommerce

in the ecommerce folder we start the models for customer and order as required in the question
      django-admin startapp customer
      django-admin startapp order
we can then run the surver to ensure proper installation of django

**Project repo**
https://github.com/MikeTarkington/cake_portal

**Brainstorming GDoc**
https://docs.google.com/document/d/1axuk8QQitvpOLjTeMMwoYbZ2OQzFjd9aauF7Bd4417I/edit

**command to run server with tracing and port forwarding (from project dir with manage.py file in it):**
- `ddtrace-run python3 manage.py runserver 0.0.0.0:8000`

**django2 cheat sheet (from udemy course)**
file:///Users/michael.tarkington/Downloads/Django2-Cheat-Sheet.pdf


**add app within project (logical seperation of functionality within site which has its own views and models etc but can be shared via import):**
- `python3 manage.py startapp name` # keep name in lower case w/single term ideally
- navigate to *apps.py* file for new app directory and note that `class <Name>Config(AppConfig):` has been created, add the `<Name>Config` portion to the `INSTALLED_APPS` section of the project *settings.py* file ie `'name.apps.NameConfig',`

**Model Creation:**
1. create blog model
- in *models.py* for the app:
    ```python
    from django.db import models

    class ModelName(models.Model):
        # attributes = https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types
        first_name = model.CharField(max_length=30)
        last_name = model.CharField(max_length=30)
        start_date = model.DateTimeField()
        demo_cert = model.BooleanField()
    ```
- for common associations: https://docs.djangoproject.com/en/3.0/topics/db/examples/
- some postgres unique docs: https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/
- general re models and databases: https://docs.djangoproject.com/en/3.0/topics/db/

2. create migration
- `python3 manage.py makemigrations`
- output should show it has detected new model and created a migration

3. migrate
- `python3 manage.py migrate`
- output should reflect having added the migration created from prev command

4. add to admin
- in *admin.py* of app directory:
    ```python
    from .models import Name

    admin.site.register(Name)
    ```
- rerun server
- check admin area for new model construct
- access shell with via django `python3 -m django dbshell --settings=cake_portal.settings` or via bash `psql -d db_name`


**Access Model Data in Views:**
- in `views.py` import the model:
    ```python
    from .models import Model

    def allobjects(request):
        objects = Model.objects
        return render(request, 'app_path/allobjects.html)', {'objects':objects})
    ```
- in corresponding view:
    ```html
    {% for object in objects.all %} 
        {{ object.attribute }}
        <br />
    {% endfor %}
    ```

**Reset Migrations**
https://www.techiediaries.com/resetting-django-migrations/
https://stackoverflow.com/questions/49645351/how-to-drop-app-table-with-django-and-postgres
https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-and-manage-py


**Django usage of Google API Refs**
https://github.com/googleapis/google-api-python-client
https://stackoverflow.com/questions/37754999/google-calendar-integration-with-django
https://pypi.org/project/python-google-calendar-api/
https://github.com/garethr/django-googlecalendar
https://code.google.com/archive/p/django-google/
http://gummadjango.blogspot.com/2017/02/google-calendar-api-with-django.html

**Google API Refs**
https://developers.google.com/calendar/quickstart/python
https://developers.google.com/calendar/v3/reference
https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md
http://googleapis.github.io/google-api-python-client/docs/dyn/calendar_v3.freebusy.html
https://developers.google.com/calendar/v3/reference/events/list
https://developers.google.com/calendar/v3/reference/freebusy/query
https://support.google.com/cloud/answer/7454865
https://gist.github.com/cwurld/9b4e10dbeecab28345a3
https://stackoverflow.com/questions/45821138/use-freebusy-to-other-calendar-than-primary

**Django Logging**
https://docs.djangoproject.com/en/3.0/topics/logging/#topic-logging-parts-loggers

**Django Making Models**
https://docs.djangoproject.com/en/3.0/topics/db/models/#meta-options
https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types
https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model

**Django Sessions**
https://docs.djangoproject.com/en/3.0/topics/http/sessions/

**Django Admin**
https://docs.djangoproject.com/en/3.0/ref/django-admin/

**Django DB Query/Interraction**
https://docs.djangoproject.com/en/3.0/topics/db/queries/
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.filter
https://tutorial.djangogirls.org/en/django_orm/











**comman to run server with tracing and port forwarding (from project dir with manage.py file in it):**
- `ddtrace-run python3 manage.py runserver 0.0.0.0:8000`

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



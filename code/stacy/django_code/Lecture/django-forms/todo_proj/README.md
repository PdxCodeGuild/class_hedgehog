https://github.com/PdxCodeGuild/class_hedgehog/blob/main/3%20Django/docs/Django%20Quickstart.md


# Create virtual environment
    virtualenv venv

# open new window in that folder
    code .

# activate virtual environment
    venv/scripts/activate

# install django
    pip install django

# freeze requirements
    pip freeze > requirements.txt

# start project
    django-admin startproject {name}_proj .

# start app
    py manage.py startapp {name} 

# add app to urls in project settings
    from {whatever} import path, include
    INSTALLED-APPS = [
        {app name here}
    ]

# add paths to project folder urls.py
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('todo/', include('todotu.urls'))
    ]

# add urls.py in app folder
    from django.urls import path
    from . import views
###### when we go to this path, run views.index function        
    urlpatterns = [
        path("", views.index) 
    ]
###### all POST request require a / at end of path

# Create templates
    todotu/templates/todotu
        index.html

# in views, import stuffs
    from django.shortcuts import render, HttpResponse
###### create index function
    def index(request):
        return HttpResponse('Hellow world!')
###### refine index function
    def index(request):
        context = {}
        return render(request, '{path}', context)
###### path here is todotu/index.html

# start server
    py manage.py runserver

# Work on index.html
    <form action="/" method="POST" name="todo_item">
###### csrf token is needed for django to allow access for the request
        {% csrf_token %}
        <input type="text">
        <select name="priority" id="">
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
        </select>
        <button>Submit</button>
    </form>

# Add some logic to views.py
    


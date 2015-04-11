#WnCC
##Python | Web frameworks | Flask

###Logistics

This session can be held at around mid Spring semester. Prior to this, WnCC is expected to have completed the following sessions in the Web section:
* basics of web, frontend and backend, PHP(so that Python backend can be appreciated :p), SQL, etc.
* Python, basic syntax and usage.
* LAMP installation which can be carried out along with Linux installation.

####Why **flask**?
Flask is a microframework for Python and is easy to get a hang of. To quote the developers

>It's intended for getting started very quickly and was developed with best intentions in mind.<br/>

Freshers will find this powerful at the same time not going overhead too.

####Place
Hands on session. As per the turnout expected, NSL or OSL will be chosen accordingly. 

####Time
Two to three hour session hands-on session at end of which participants will have a simple Python server running which will also have extended database support with SQLite.

**Note**: A more engaging and detailed presentation needs to be made. The below just gives an overview of details.

###Tutorial
#####Web framework?
A web application framework (WAF) is a software framework that is designed to support the development of dynamic websites, web applications, web services and web resources. The framework aims to alleviate the overhead associated with common activities performed in web development.

#####Why 'micro' in flask, a microframework?
“Micro” does not mean that Flask is lacking in functionality nor does it mean that your whole web application has to fit into a single Python file, although it certainly can. The “micro” in microframework means Flask aims to keep the core simple but extensible. Though a framework it does not force decisions.

Not suitable for constantly expanding and **very** large projects, because as your project grows in complexity, you may find that you outgrow the micro framework, and may prefer something that promotes better code organization in a large project. But if this is a side project, don't let the fear of outgrowing it prevent you from starting with a micro framework that you're comfortable with.

#####Setup and execution
```
$ pip install Flask
$ python hello.py
 * Running on http://localhost:5000/
```
#####hello, world!
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
Save this as `hello.py` and execute as shown above.

####Routing
#####Explanation
**@app.route** gives the content for a specific route. For example, `@app.route('/url')` gives content for `website/url`.<br/>
#####Example
```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```
Here the `localhost:5000` has `Index page` and `localhost:5000/hello` has `Hello World`.

#####Rendering template
Flask configures the Jinja2 template engine for you automatically. You will need to use `render_template()` method.
```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
Flask will look for templates in the templates folder.  Hence, the file structure should be like
```
/application.py
/templates
    /hello.html
```
where `hello.html` is a template and will look this
```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```
Now using the concept of routing and rendering when this app is executed `localhost:5000/foo` will have `Hello foo`.

**Note**: A couple of new symbols are noticed here
 
* **@** : Decorators may/may not be covered in the `Python` session. If the decorators are not covered, then `@app-route` is a syntactical thing which gives the route url, the real meaning can be ignored in terms of implementation.
* **{% block %}**: Part of Jinga templating.<br/>
Example: 
```
{% block body %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
```
Though Jinga can be a session on it's own, it is unnecessary. It is intuitive and can be sinked after a couple of examples.

#####Debug mode
Running the app in `debug` mode has some advantages.

**How?**

Either this
```
app.debug = True
app.run()
```
or `app.run(debug=True)`, both have the same effect.

**Advantages**

Everytime you change the code, you have to restart the server to see the changes but this is not the case in `debug mode`. Also it provides a helpful debugger if things go wrong.

**Why can't you always do this?**

To quote a sentence in the documentation
>There is a major security risk.

(These technical details might not be necessary, though a satisfactory reply should be given if doubts raised)

#####Exercise
Use **flask** as structural framework for any website/webapp that you made. Rendering a template will be a big plus.

####Building the server
Participants should have an idea of GET, POST requests and should have used them in the past.<br/>
Basic idea of queries is necessary. Atleast should know where to look up for prepared query statements.<br/>
Actual example and explanation is not added here so as to not bloat this document. One such example is the [EasyFill](https://github.com/Sumith1896/EasyFill) project.<br/>

####Concluding remarks
The structure that **Flask** gets to web apps is amazing. Flask is great for developers working on small projects that need a fast way to make a simple, Python-powered web site.<br/>
* Their github [repo](https://github.com/mitsuhiko/flask) is open to suggestions and contributions.<br/>
* Flask's [documentation](http://flask.pocoo.org/docs/0.10/) is also very well organised and is exhaustive.<br/>
* Some `flask` projects for inspiration can be found at [http://flask.pocoo.org/community/poweredby](http://flask.pocoo.org/community/poweredby/).<br/>
* My flask project can be found [here](https://github.com/Sumith1896/EasyFill) but to complete the app you'll need the Android half which can be found in [Meet](https://github.com/udiboy1209)'s profile [here](https://github.com/udiboy1209/EasyFill).
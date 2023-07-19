# Flask

Flask - набор инструментов для создания веб-приложений

![Flask image](../images/flask.png "Flask image")


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Добро пожаловать!</h1>'

app.run()
```

Стандартная (типовая) структура Flask проекта:

```
/flask_project
    /app
        /static
            /css
            /js
            /images
        /templates
            home.html
            login.html
            base.html
            ...
    config.py
    run.py
    requirements.txt
```


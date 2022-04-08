```
$env:FLASK_APP = "app.py"
```
```
$env:FLASK_ENV = "development"
```
```
flask run
```

These steps are required to run a Python Flask development server though most
likely that will not be useful if trying to test the project bewteen devices.
Though it can be used if the macro is directed to locahost and the
primary device you use has a webcam.

This server will serve the web application allowing models to be uploaded and
viewed. Though this can still be done using the hosted server at https://2316615a.pythonanywhere.com/ (End date 8th July 2022)
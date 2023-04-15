# CipSurf_Email_Collection
API to collect email of the user and send automated custom emails.

### Testing on Local System

In order to test the API on local system, clone the repositorty and run the following commands:

(1) Activating the environment
```
./test/Scripts/activate.ps1 
```

(2) Running the Flask deployment server
```
Flask run 
```
or
```
py app.py
```

### Requirements

The library requirements for the project is mentioned in [requirements.txt](./requirements.txt)

The requirements include:

```
aniso8601==9.0.1
click==8.1.3
colorama==0.4.6
dnspython==2.3.0
Flask==2.2.3
Flask-RESTful==0.3.9
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
pymongo==4.3.3
python-dotenv
pytz==2023.3
six==1.16.0
Werkzeug==2.2.3
gunicorn==20.0.4
```

### Accessing the API remotely

The base url of the API is : [ClipSurf](https://clipsurf.onrender.com)

The endpoints is dynamically created based on the email and the name of the user.
The final endpoinnts looks like :
```
https://clipsurf.onrender.com/youremail@example.com&firstname
```

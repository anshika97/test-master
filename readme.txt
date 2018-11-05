# use python 3.7.1
# cd to project directory before executing below commands

# install dependencies
$ sudo pip install -r requirements.txt

# make migrations
$ python3 manage.py makemigrations

# apply migrations
$ python3 manage.py migrate

# run server
$ python3 manage.py runserver

# view in browser
# navigate to localhost:8000
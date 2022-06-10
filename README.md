# StringReverseApi
An endpoint that reverses phrases

## How to run the application
### Clone the project from github
- git clone git@github.com:joseph-njogu/StringReverseApi.git

### Install the requirements
- pip install -r requirements.txt

### Makemigrations
- python3 manage.py makemigrations && python3 manage.py migrate

### Runserver
- python3 manage.py runserver
- Head to the browser on th provided localhost link

# Dockerization
- Run the application as a docker image
- docker run njogu487/reverseapi:0.0.1 then
- docker up

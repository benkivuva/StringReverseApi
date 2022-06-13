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
- Head to the browser on http://127.0.0.1:8000/reverse

# Dockerization
- Run the application as a docker image
- docker run njogu487/reverseapi:latest then
- docker up
- You should be able to access the api endpoint on http://127.0.0.1:8000/reverse

## Build and publish image to docker hub
Using circleci as the CICD platform, automate the bukiding and publishing
the docker image to dockerhub.

## Build and publish the docker image to an AWS FARGATE
## Requirements for this

```
ansible
awscli
boto
botocore
boto3
docker
docker-py
docker-compose
```
# Using ansible playbooks to:
1. Create a VPC with public routes and security groups.
1. Creates relevant IAM Roles for ECS/FARGATE.
1. Push docker image to AWS ECR.
1. Create an AWS ECS cluster and service and task.
1. Start ECS cluster task based on the container.
1. Attach the ECS FARGATE cluster to an AWS ELB for dynamic scaling.
1. You can scale number of nodes you want to run by changing `size_of_cluster: 3` in `./vars/everything.yml`
1. This also puts logs in to AWS Cloudwatch.

Ensure that you have the correct profile as your default profile in `~/.aws/credentials` .
You also want to export your keys to the current shell environment like this:

```
echo export AWS_ACCESS_KEY_ID="your access id"
echo export AWS_SECRET_ACCESS_KEY="your access key"
```

# docker-kubernetes-demo with GKE

The purpose of this repo is to establish connection between two pods

Pod 1: contains the container of flask application

pod 2: contains the container of mysql


# Image creation
# run this command where the dockerfile exist
cd app

docker build -t image-name:tag .

# run this command to run the container
docker run -d -p 5000:5000 image-name


# Uploading image to the container registry steps

docker tag tag_image gcr.io/project-id/image-name


docker push gcr.io/project-d/image-name


# Configure environment for kubernetes cluster

# Check the configuration 
gcloud config list

gcloud config set project $PROJECT_ID

gcloud config set compute/zone [COMPUTE_ENGINE_ZONE]


# Create the new cluster
gcloud container clusters create cluster-name --num-nodes=2

ex:

gcloud container clusters create demo --num-nodes=2


# kubernetes
cd DEMO

# deploy the containers
kubectl apply -f flask-deployment.yml

kubectl apply -f db-deployment.yml

# check the deployment
kubectl get deployment

kubectl apply -f flask-service.yml

kubectl apply -f db-service.yml

# check services are running 
kubectl get services

# check its working
externalIP:port


# config the pod network/communication
# sql
kubectl exec -it pod-name bash

mysql -u root -p root

then run the content from db.sql file in that mysql


# Remove the created cluster

gcloud container clusters delete cluster-name

ex:

gcloud container clusters delete flask-mysql-cluster

gcloud container clusters delete demo

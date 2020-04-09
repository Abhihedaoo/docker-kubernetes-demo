First create three namespace

nginx: having nginx to control traffic amongst the services
tenant1: having all the resources belong to tenant1
tenant2: having all the resources belong to tenant1


We will be using the helm for this scenario

Install helm 
command:

```console
wget https://get.helm.sh/helm-v3.0.1-linux-amd64.tar.gz
tar -zxvf helm-v3.0.1-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm3
```

check

```console 
helm3 version
```

add the repo to helm

Nginx Setup

Create a namespace nginx

command:
```console
kubectl create ns nginx
```

Deploy and expose nginx 

```console
helm3 install nginx stable/nginx-ingress --namespace nginx --set rbac.create=true --set controller.publishService.enabled=true
```

See the running services and external IP of the nginx

```console
kubect get services -n nginx
```

Tenant1 setup

create namespace tenant1

command:
```console
kubectl create ns tenant1
```

Deploy the hello-world app on tenant1

```console
kubectl create deployment hello-app-tenant1 --image=gcr.io/google-samples/hello-app:1.0 --namespace=tenant1
```

Expose the hello-world app on tenant1

```console
kubectl expose deployment hello-app-tenant1 --port 8080 --target-port 8080 --namespace=tenant1
```

To check the service running and deployed properly 

```console
kubectl get pods -n tenant1
kubectl get services -n tenant1
```


Tenant2 Setup

Create namespace tenant2

```console
kubectl create ns tenant2
```

Deploy the hello-world app on tenant2

```console
kubectl create deployment hello-app-tenant2 --image=gcr.io/google-samples/hello-app:1.0 --namespace=tenant2
```

Expose the hello-world app on tenant2

```console
kubectl expose deployment hello-app-tenant2 --port 8080 --target-port 8080 --namespace=tenant2
```

To check the service running and deployed properly

```console
kubectl get pods -n tenant2
kubectl get services -n tenant2
```

deploy the ingress controller name ingress.yaml

```console
kubectl apply -f ingress-tenant1.yaml
kubectl apply -f ingress-tenant1.yaml
```


Now go to GCP > kubernetes engine >services and ingress
there under ingress tab you can see all the paths through nginx


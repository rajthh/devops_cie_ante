\# DevOps CIE 2026



\## Exercise 1: Hello Pod



\### Objective

Deploy an Nginx application on Kubernetes using Minikube.



\### Tools Used

\- Docker Desktop

\- Minikube

\- Kubernetes

\- kubectl

\- Nginx



\### Commands Used



```bash

minikube start --driver=docker

kubectl run hello-k8s --image=nginx --port=80

kubectl get pods

kubectl expose pod hello-k8s --type=NodePort --port=80

kubectl get services

minikube service hello-k8s


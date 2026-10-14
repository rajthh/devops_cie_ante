\# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and Replicasets



\## Objective



To deploy multiple applications on a multi-node Kubernetes cluster using Minikube, Deployments, ReplicaSets, Pod Anti-Affinity, and NodePort Services.



The exercise consists of two applications:



\- \*\*Product Catalog\*\*: Provides product information.

\- \*\*Shopping Cart\*\*: Manages items added to the shopping cart.



The Product Catalog runs with \*\*2 replicas\*\*, while the Shopping Cart runs with \*\*3 replicas\*\*. Pod Anti-Affinity is used to distribute replicas across different Kubernetes nodes for fault tolerance.



\---



\## Technologies Used



\- Kubernetes

\- Minikube

\- Docker

\- Python

\- Flask

\- YAML

\- PowerShell



\---



\## Cluster Configuration



A 3-node Minikube cluster was created:



```powershell

minikube start --nodes 3 -p devops-multinode --force


\# Exercise 7 - Introduction to Continuous Integration (CI) and Jenkins



\## Objective



To understand Continuous Integration (CI), Jenkins, CI workflow, Jenkins concepts, and demonstrate a basic CI pipeline using Jenkins.



\## What is Continuous Integration?



Continuous Integration is a development practice where developers frequently integrate their code changes into a shared repository.



\### Key Features



\- Frequent Code Integration

\- Automated Builds

\- Automated Testing

\- Immediate Feedback



\### Benefits



\- Early Bug Detection

\- Improved Collaboration

\- Faster Development Cycles

\- High-Quality Code



\## CI Workflow



1\. Developer pushes code to Git.

2\. CI server detects the change.

3\. Build process is triggered.

4\. Automated tests are executed.

5\. Results are reported to the developer.



\## Jenkins



Jenkins is an open-source automation server used to build, test, and deploy software.



\### Jenkins Concepts



\- Job/Project: A task executed by Jenkins.

\- Build: Execution of a build process.

\- Pipeline: A sequence of build, test and deployment steps.

\- Plugins: Extend Jenkins functionality.

\- Nodes: Machines where Jenkins jobs execute.



\## Jenkins Installation



Jenkins can be run using Docker:



&#x20;   docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts



Jenkins is accessed through:



&#x20;   http://localhost:8080



\## Practical CI Demonstration



A Jenkins Pipeline named `Exercise-7-CI` was created.



Pipeline stages:



1\. Checkout

2\. Build

3\. Test

4\. CI Success



The pipeline executed successfully with Build #1.



\## Result



Successfully understood Continuous Integration and Jenkins and demonstrated a basic CI pipeline using Jenkins.


# Student Project – Multi-App Django Application

## Overview
This is a Django-based multi-app project with CI/CD automation.

- **Framework**: Django
- **Containerization**: Docker
- **Automation**: Jenkins
- **Deployment**: Docker Hub

## Project Structure
```
StudentProject/    - Main Django project folder
  app1/           - Contains the homepage
  app2/           - Contains a sample page
  templates/      - Global templates for UI
  static/         - Contains CSS for styling
Dockerfile        - Defines how the project runs inside a container
Jenkinsfile       - Automates the CI/CD pipeline
```

## How to Run the Project Locally
### 1. Clone the Repository
```bash
git clone https://github.com/SRCEM-AIML/C1_09_MeghaKirpan_assignment2.git
cd C1_09_MeghaKirpan_assignment2
```

### 2. Run Using Docker
If you want to run the project inside a Docker container, use:
```bash
docker build -t meghakirpan/studentproject .
docker run -p 8000:8000 meghakirpan/studentproject
```
Now, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### 3. Pull from Docker Hub
Instead of building manually, you can pull the prebuilt image:
```bash
docker pull meghakirpan/studentproject:latest
docker run -p 8000:8000 meghakirpan/studentproject
```
Now your project will be live on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Jenkins CI/CD Pipeline
The Jenkins pipeline automates:
- Pulling code from GitHub
- Building a Docker image
- Pushing it to Docker Hub

To trigger the pipeline, push any changes to GitHub, and Jenkins will do the rest!

## Important Links
- **GitHub Repository**: [C1_09_MeghaKirpan_assignment2](https://github.com/SRCEM-AIML/C1_09_MeghaKirpan_assignment2)
- **Docker Hub Image**: meghakirpan/studentproject

## Conclusion
This project demonstrates a full CI/CD pipeline with Django, Docker, and Jenkins. It ensures that every code change is automatically built, tested, and deployed using best DevOps practices.


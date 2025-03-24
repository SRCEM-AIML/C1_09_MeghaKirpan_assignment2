# A-32-ASSIGNMENT2
##  Student Project – Multi-App Django Application**  
### ** Overview**  
This is a **Django-based multi-app project**  
- **Framework:** Django  
- **Containerization:** Docker  
- **Automation:** Jenkins  
- **Deployment:** Docker Hub  
---
###  Project Structure**  
- `StudentProject/` – Main Django project folder  
- `app1/` – Contains the homepage  
- `app2/` – Contains a sample page  
- `templates/` – Global templates for UI  
- `static/` – Contains CSS for styling  
- `Dockerfile` – Defines how the project runs inside a container  
- `Jenkinsfile` – Automates the CI/CD pipeline  
---
### ** How to Run the Project Locally**  
#### **1 Clone the Repository**  
```bash
git clone https://github.com/SRCEM-AIM-Class-A/A-32-ASSIGNMENT2.git
cd A-32-ASSIGNMENT2
#### **2️ Run Using Docker**  
If you want to run the project inside a Docker container, use:  
```bash
docker build -t studentproject .
docker run -p 8000:8000 studentproject
```
Now, open **`http://127.0.0.1:8000/`** in your browser.

---
### ** Pull from Docker Hub**  
Instead of building manually, you can **pull the prebuilt image**:  
```bash
docker pull chhavipancholi/chhavipancholi-assignment2:latest
docker run -p 8000:8000 chhavipancholi/chhavipancholi-assignment2
```
Now your project will be live on `http://127.0.0.1:8000/`  
---
### **Jenkins CI/CD Pipeline**  
The Jenkins pipeline automates:  
1 pulling code from GitHub**  
2.Building a Docker image**  
3.Pushing it to Docker Hub**  
To trigger the pipeline, **push any changes to GitHub**, and Jenkins will do the rest!
### ** Important Links**
- **GitHub Repository:** [A-32-ASSIGNMENT2](https://github.com/SRCEM-AIM-Class-A/A-32-ASSIGNMENT2)  
- **Docker Hub Image:** [chhavipancholi-assignment2](https://hub.docker.com/repository/docker/chhavipancholi/chhavipancholi-assignment2/general)  
### ** Conclusion**  
This project demonstrates **a full CI/CD pipeline with Django, Docker, and Jenkins**. It ensures that every code change is automatically built, tested, and deployed using best DevOps practices.  


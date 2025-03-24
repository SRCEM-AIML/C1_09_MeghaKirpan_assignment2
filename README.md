## 📌 Project Overview<br>
This project demonstrates the containerization of a multi-app Django web application using Docker. The setup ensures a consistent runtime environment, making the application portable, scalable, and easy to deploy.

##✅ Why Use Docker?<br>
🛠 Isolation: The Django application runs inside its own container, avoiding conflicts with other services or dependencies.
-Consistency: The environment remains the same across development, testing, and production.
-Portability: Easily deploy the containerized application on any system or cloud platform.
-Scalability: Docker allows horizontal scaling by running multiple containers simultaneously.

##🔧 How It Works<br>
📄 Dockerfile: Sets up a lightweight Python environment, installs dependencies, and copies the Django project files into the container.

🤖 Jenkinsfile (CI/CD Pipeline): Automates the process by:
+Pulling the latest code from the GitHub repository.
+Building the Docker image.
+Pushing the built image to Docker Hub.

Running the Application: Once the Docker image is built and pushed, the Django app can be run as a container, accessible via the configured port.

##Technologies Used<br>
Python 3<br>
Django<br>
Docker<br>
Jenkins (for CI/CD pipeline)<br>

##Contact for Support<br>
Name: Megha Kirpan<br>
Email: kirpanmk@rknec.edu

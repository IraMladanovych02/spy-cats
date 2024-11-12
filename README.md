# spy-cats
# Library

Description
---
A project for efficient management of spying work processes

# Installation

### How to Set Up the Project

1. **Clone the Repository**  
   Fork the repository and clone it to your local machine:
   ```bash
   https://github.com/<YOU_NAME>/spy-cats.git
   ```

2. **Set Up a Virtual Environment**  
   Create a virtual environment and activate it. Then, install the required dependencies:
   
   - On **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     pip install -r requirements.txt
     ```
   
   - On **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

3. **Create a Superuser**  
   To manage the project through the admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. **Run the Development Server**  
   Start the server to check if the website is running:
   ```bash
   python manage.py runserver
   ```

---

# CREATED SUPERUSER

- For efficient management of the project, the User model was added and the superuser was created. lease, use provided credenyials to login:
---
- **email: user@user.com**
- ---
- **password: user123456789**

# Documantation

Due to time constraints, I was unable to add all the endpoints to Postman. But I`ve implemented Swagger to create documentation automatically.
To check the documentation please run server and enter the following url: http://127.0.0.1:8000/api/doc/swagger/
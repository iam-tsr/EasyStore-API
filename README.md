# EasyStore API

## Overview
The EasyStore API provides a simple and efficient backend storage solution for small websites or projects that lack a backend storage system. This API allows users to generate API keys, store files, manage access, monitor usage, and ensure security. The service utilizes a local system drive for storage and includes features such as API key generation and file upload automation.

## Project Structure
The project consists of the following main files and directories:

- `.env` - Environment variables configuration file.
- `.env.example` - Example environment variables file.
- `.gitignore` - Specifies which files and directories to ignore in git.
- `app.py` - Main application script.
- `db.sqlite` - SQLite database file.
- `requirements.txt` - Python dependencies required for the project.
- `migrations/` - Directory containing database migration scripts.
- `static/` - Directory for static files like CSS.
- `templates/` - Directory for HTML template files.
- `uploads/` - Directory where uploaded files are stored.
- `tests/` - Directory containing test scripts.

## Setup and Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- PostgreSQL (for database)

### Installation Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/iam-tsr/EasyStore-API.git
   cd EasyStore-API
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv\Scripts\activate  # On Windows use `venv/bin/activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file based on the `.env.example` file.
   - Configure the necessary environment variables.

5. **Create PostgreSQL Database**
   - Log in to PostgreSQL:
     ```sh
     psql -U postgres
     ```
   - Create a new database and user:
     ```sql
     CREATE DATABASE store;
     CREATE USER api WITH PASSWORD 'key';
     ```
   - Grant all privileges on the database to the user:
     ```sql
     GRANT ALL PRIVILEGES ON DATABASE store TO api;
     ```
      ```
      \c store
      GRANT ALL PRIVILEGES ON DATABASE store TO api;
      GRANT USAGE ON SCHEMA public TO api;
      GRANT CREATE ON SCHEMA public TO api;
      ```
      ```
      ALTER USER api WITH SUPERUSER;
      ALTER USER api WITH NOSUPERUSER;
      ```

6. **Configure Environment Variables (Only if you have made changes while creating PostgreSQL Database)**

   - Update your `.env` file with the following variables :

     ```
     DATABASE_URL=postgresql://easystore_user:your_password@localhost/easystore_db
     SECRET_KEY=your_secret_key
     UPLOAD_FOLDER=uploads
     ```

<!-- 7. **Run Migrations**
   ```sh
   alembic upgrade head
   ``` -->

7. **Start the Application**
   ```sh
   python app.py
   ```

## Usage

### API Endpoints
- **Authentication**
  - `POST /register`: Register a new user.
  - `POST /login`: Log in an existing user to receive an authentication token.

- **File Management**
  - `POST /upload`: Upload a file.
  - `GET /files`: Retrieve a list of uploaded files.
  - `GET /files/<file_id>`: Download a specific file.

### Example Requests
- **Register**
  ```sh
  curl -X POST http://localhost:5000/register -d '{"username": "testuser", "password": "testpass"}' -H "Content-Type: application/json"
  ```

- **Login**
  ```sh
  curl -X POST http://localhost:5000/login -d '{"username": "testuser", "password": "testpass"}' -H "Content-Type: application/json"
  ```

- **Upload File**
  ```sh
  curl -X POST http://localhost:5000/upload -F 'file=@path/to/your/file.txt' -H "Authorization: Bearer <your_token>"
  ```

- **Get Files**
  ```sh
  curl -X GET http://localhost:5000/files -H "Authorization: Bearer <your_token>"
  ```

- **Download File**
  ```sh
  curl -X GET http://localhost:5000/files/<file_id> -H "Authorization: Bearer <your_token>" -o downloaded_file.txt
  ```

## Configuration
- **Environment Variables**
  - `SECRET_KEY`: Secret key for session management.
  - `DATABASE_URL`: Database connection string.
  - `UPLOAD_FOLDER`: Directory for storing uploaded files.

## Testing
To run the tests, use the following command:
```sh
pytest
```
This will execute the tests defined in `test_authentication.py` and `test_query.py`.

## File Descriptions
- **app.py**: Main application script handling routing and logic.
- **db.sqlite**: SQLite database file storing user and file information.
- **requirements.txt**: Lists the dependencies required by the project.
- **migrations/**: Contains scripts for database migrations.
- **static/**: Stores static assets like CSS files.
- **templates/**: Contains HTML templates for rendering web pages.
- **uploads/**: Directory for storing uploaded files.
- **tests/**: Directory containing test scripts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing
Feel free to contribute by submitting issues or pull requests. Please ensure your contributions align with the project's goals and standards.

## Contact
For any inquiries or support, please contact Tushar Rajput (@iam-tsr) or Ansh Chauhan (@Anshchauhanhub).
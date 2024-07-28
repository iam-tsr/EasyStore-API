
# EasyStore API

## Overview

This project provides a simple and efficient backend storage solution for small websites or projects that lack their own backend storage. It allows developers to generate API keys, store files, manage access, monitor usage, and ensure security. The storage service uses the local system drive.

## Features

- **API Key Generation**: Create unique API keys for users.
- **File Storage**: Store and manage files using the generated API keys.
- **Access Management**: Control access to stored files based on API keys.
- **Usage Monitoring**: Track the usage of storage and API key activity.
- **Security**: Ensure secure storage and access of files.

## Project Structure
```
.
├── app.py                 # Main application file
├── gitignore.txt          # Git ignore file
├── project_directory.txt  # Project directory description
├── project_structure.txt  # Project structure information
├── requirements.txt       # List of dependencies
├── storage.json           # Storage configuration file
├── storage_client.py      # Client interface for storage operations
├── storage_system.py      # Core storage system logic
├── templates/             # Directory for HTML templates
└── upload/                # Directory for file uploads
```
## Getting Started

### Prerequisites
```
- Python 3.x
- Required dependencies (listed in `requirements.txt`)
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iam-tsr/EasyStore-API.git
   cd EasyStore-API
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the main application:

   ```bash
   python app.py
   ```

2. The application will start and provide endpoints for API key generation, file storage, and management.

### Configuration

Modify `storage.json` to configure the storage settings, such as storage path and limits.

### API Endpoints

- **Generate API Key**: `POST /generate-api-key`
- **Upload File**: `POST /upload-file`
- **Access File**: `GET /file/<api_key>/<file_id>`
- **Monitor Usage**: `GET /usage/<api_key>`

### File Upload Script

A script is available to automate the process of uploading files using the API key. You can find it in the `upload/` directory.

### Security

Ensure secure storage and access by configuring appropriate permissions in `storage.json`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing

Feel free to contribute by submitting issues or pull requests. Please ensure your contributions align with the project's goals and standards.

## Contact

For any inquiries or support, please contact Tushar Rajput (@iam-tsr) or Ansh Chauhan (@Anshchauhanhub)..
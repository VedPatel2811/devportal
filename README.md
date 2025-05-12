
# Developer Portal for API Management

## Project Overview

This project is a Developer Portal built using Django that enables users to manage API keys, view API documentation, 
and track API usage statistics. The portal provides features like user authentication, role-based access control, 
and a dashboard for monitoring API usage.

### Features

- User Registration and Authentication (Admin, Developer, Viewer roles)
- API Key Generation and Management
- Auto-Generated API Documentation using Swagger
- Interactive API Testing Tool
- Usage Analytics with Graphical Visualization
- Admin Panel for User and API Key Management

## Tech Stack

- Backend: Python, Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (can be switched to PostgreSQL)
- Deployment: Docker, AWS (optional)
- Version Control: Git, GitHub

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VedPatel2811/devportal.git
   cd devportal
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`
- API Documentation: `http://127.0.0.1:8000/api/docs/`

## API Endpoints

- User Registration: `POST /api/users/`
- API Key Generation: `POST /api/apikeys/`
- View API Keys: `GET /api/apikeys/`
- Interactive API Testing: via Swagger Docs

## Contributing

1. Fork the project
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request

## License

This project is licensed under the MIT License.

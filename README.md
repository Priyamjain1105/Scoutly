# Scoutly

A Flask + MySQL platform that connects students with employers. Students can create profiles, browse/apply for jobs, and connect with hiring managers. Employers can post jobs and reach out to candidates. Hosted on AWS.

## Description
Helps to connect Students/Working professionals to hiring managers

## Tech Stack
- Backend: Flask
- ORM/DB: SQLAlchemy + MySQL
- Hosting/Storage: AWS (EC2/S3/RDS)
- Authentication: Flask-Login / JWT (your choice)

## Getting Started

### Prerequisites
- Python 3.x
- MySQL server (or AWS RDS)
- Virtual environment support

### Installation
```bash
# 1. Create and activate virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
```

### Configuration
Create a .env file or set environment variables:
- FLASK_APP=your_app
- FLASK_ENV=development or production
- SECRET_KEY=your-secret-key
- SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@host/dbname
- AWS_ACCESS_KEY_ID=...
- AWS_SECRET_ACCESS_KEY=...
- S3_BUCKET_NAME=...
- MAIL_SERVER/MAIL_USERNAME/MAIL_PASSWORD (optional)

### Run Locally
```bash
flask run
# App available at http://localhost:5000
```

### Run in Docker (optional)
```bash
docker-compose up -d
```

## API Endpoints (optional)
- Auth: POST /auth/register, POST /auth/login
- Profiles: GET /students/{id}, GET /employers/{id}
- Jobs: GET /jobs, POST /jobs, GET /jobs/{id}
- Applications: POST /jobs/{id}/apply
- Messages: GET /conversations/{id}, POST /conversations/{id}/messages

## Database Schema (high level)
- users(id, email, password_hash, role, name, created_at)
- student_profiles(id, user_id, resume_url, major, graduation_year)
- employer_profiles(id, user_id, company_name)
- jobs(id, employer_id, title, description, location, type, salary, posted_at)
- applications(id, student_id, job_id, resume_url, status, applied_at)
- messages(id, sender_id, recipient_id, content, sent_at)

## Security & Best Practices
- Passwords hashed with bcrypt/argon2
- Use HTTPS in production
- CSRF protection for forms
- Input validation and sanitization
- Principle of least privilege for IAM roles

## Testing
- Unit tests location: tests/
- How to run: pytest

## Deployment
- AWS: EC2 (or Elastic Beanstalk), RDS for MySQL, S3 for storage, SES for email
- WSGI: Gunicorn behind Nginx
- Domain + TLS via ACM

## Contributing
- Fork the repo
- Create a feature branch
- Run tests
- Submit a PR

## License
MIT 



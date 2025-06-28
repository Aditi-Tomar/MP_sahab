# Deployment Guide for Voter Management System

## Deploying to Render

### 1. Prerequisites
- GitHub repository with your code
- Render account
- AWS RDS MySQL database (already configured)

### 2. Environment Variables
Set these in your Render dashboard using your AWS RDS credentials:

```
DEBUG=False
SECRET_KEY=your-secret-key-here
DB_NAME=testnew
DB_USER=admin
DB_PASSWORD=Target321h
DB_HOST=mpsahab.c52ygcs8ia06.eu-north-1.rds.amazonaws.com
DB_PORT=3306
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Note**: Replace the database credentials above with your actual AWS RDS credentials if they're different from the ones in your local settings.

### 3. Build Commands
In Render, set these build commands:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

### 4. Start Command
```bash
gunicorn core.wsgi:application
```

### 5. Static Files
- Whitenoise is configured to serve static files
- Run `python manage.py collectstatic` during build
- Static files will be served from `/static/`

### 6. Media Files (Render Persistent Disk)
- Media files are stored on Render's persistent disk
- Path: `/opt/render/project/src/media`
- Media files are included in Git for initial deployment
- New uploads will be saved to Render's persistent storage
- Media files persist between deployments

### 7. Database (AWS RDS)
- Your app is already configured to use AWS RDS MySQL
- Ensure your AWS RDS security group allows connections from Render's IP ranges
- Database endpoint: `mpsahab.c52ygcs8ia06.eu-north-1.rds.amazonaws.com`
- Database name: `testnew`
- User: `admin`

### 8. Security
- Set `DEBUG=False` in production
- Use strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS` properly
- Ensure AWS RDS security group is properly configured

### 9. HTTPS (Optional)
Uncomment HTTPS settings in `settings.py` if using custom domain with SSL.

## Local Development
```bash
python manage.py runserver
```

## Production Checklist
- [ ] DEBUG=False
- [ ] Strong SECRET_KEY
- [ ] AWS RDS database accessible from Render
- [ ] Static files collected
- [ ] Migrations applied
- [ ] Environment variables set
- [ ] Media files included in Git
- [ ] AWS RDS security group allows Render connections 
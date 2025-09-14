# Permissions and Groups Setup Guide

## Overview
This Django application implements a comprehensive permission system using Django's built-in authentication system with custom permissions and groups.

## Custom Permissions
The Book model has been extended with four custom permissions:
- `can_view` - View books
- `can_create` - Create new books
- `can_edit` - Edit existing books
- `can_delete` - Delete books

## Groups Configuration
Three groups have been created with the following permissions:

### 1. Viewers Group
- Permissions: `can_view`
- Description: Users can only view books but cannot modify them.

### 2. Editors Group
- Permissions: `can_view`, `can_create`, `can_edit`
- Description: Users can view, create, and edit books but cannot delete them.

### 3. Admins Group
- Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
- Description: Users have full access to all book operations.

## Setup Instructions

1. **Create Groups and Assign Permissions:**
   - Go to Django Admin → Groups
   - Create the three groups: Viewers, Editors, Admins
   - Assign the appropriate permissions to each group

2. **Assign Users to Groups:**
   - Go to Django Admin → Users
   - Select a user and assign them to the appropriate group

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate



   # Security Implementation Documentation

## Security Measures Implemented

### 1. Secure Settings Configuration
- **DEBUG**: Configured to use environment variable (set DEBUG=False in production)
- **Security Headers**: Enabled XSS filter, clickjacking protection, and MIME type sniffing prevention
- **HTTPS Enforcement**: Session and CSRF cookies set to secure-only for HTTPS
- **Content Security Policy**: Implemented CSP to restrict resource loading

### 2. CSRF Protection
- All forms include `{% csrf_token %}` template tags
- CSRF middleware enabled in settings
- CSRF cookies are HTTPOnly and Secure

### 3. SQL Injection Prevention
- Used Django ORM with parameterized queries
- Input validation in search functionality
- Form validation for all user inputs

### 4. XSS Prevention
- Content Security Policy headers implemented
- Safe template rendering
- Input validation and sanitization

### 5. Secure Password Handling
- Minimum password length enforced (8 characters)
- Common password prevention
- Numeric password prevention

## Environment Variables for Production

Set these environment variables in production:

```bash
DEBUG=False
SECRET_KEY=your-very-secure-random-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
# DevTest

DevTest is a Django web app for uploading Excel/CSV files, generating a summary, and sending email reports with attached Excel and image files.

## Features

- Upload Excel or CSV files.
- Generate a summary for the first few rows.
- Send the summary via email with Excel and image attachments.
- Show column names and total records.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Virtual Environment](#virtual-environment)
4. [Dependencies](#dependencies)
5. [Running the Server](#running-the-server)
6. [Email Configuration](#email-configuration)
7. [License](#license)

## Requirements

- Python 3.x
- Django 4.x
- Virtualenv
- Pip

## Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/DevTest.git
cd DevTest
```

## Virtual Environment

Set up a virtual environment and activate it:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate # for macOS/Linux
venv\Scripts\activate # for Windows
```

## Dependencies

Install all project dependencies:

```
pip install -r requirements.txt
```

## Running the Server

To run the Django development server, use the following command:

```
python manage.py runserver
```

## Email Configuration

Set up email by creating a .env file with the following:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
```
# DevTest

DevTest is a Django-based web application that allows users to upload Excel/CSV files, generates a summary report from the uploaded data, and sends an email with the report as an Excel file and an image summary of the data. This README provides instructions for setting up the project, installing dependencies, running the server, and understanding the key functionalities.

## Features
- Upload Excel or CSV files
- Generates a summary of the first few rows of data
- Sends a summary report via email, including an Excel file and an image visualization of the data
- Provides key details like the number of columns and their names

## Table of Contents
1. [Requirements](#requirements)
2. [Project Setup](#project-setup)
3. [Running the Server](#running-the-server)
4. [Understanding the Code](#understanding-the-code)
   - [Views](#views)
5. [License](#license)

## Requirements

Make sure you have the following installed on your system:
- Python 3.x
- Django 4.x
- Virtualenv

## Project Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/end-9214/DevTest.git
cd DevTest

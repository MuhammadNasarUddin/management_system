# Management System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Django Version](https://img.shields.io/badge/django-5.0%2B-brightgreen.svg)](https://www.djangoproject.com/download/)

## Description

Rehan School Management System is a comprehensive web application built with Django, designed to streamline and manage various aspects of a school's operations, including interviews, faceless interactions, postings, and graphics.

## Features

- **User Authentication**: Secure user registration, login, and logout functionality.
- **Profile Management**: User profiles with statistics on interviews, faceless interactions, postings, and graphics.
- **Interviews**: Record and manage interviews, including guest name, topic, language, city, country, and URL.
- **Faceless Interactions**: Track faceless interactions with titles, numbers, and URLs.
- **Postings**: Manage postings with titles, numbers, and URLs.
- **Graphics**: Organize graphics with titles, numbers, and URLs.
- **Admin Panel**: A dedicated admin panel for administrators to manage users, interviews, faceless interactions, postings, and graphics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MuhammadNasarUddin/management_system
   
## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Apply Migrations:**
   ```bash
   python manage.py migrate  

3. **Create a superuser for the admin panel:**
   ```bash
   python manage.py createsuperuser

4. **Run the Development Server:**
   ```bash
   python manage.py runserver   



# Technical Documentation for Django Car Rental REST Framework App

## Project Overview
This project is a Car Rental application built using Django REST Framework. The app is structured into multiple Django apps: `account`, `booking`, `CarDealer`, `cars`, and `dealers`. The application provides functionalities for user account management, car bookings, car dealership management, and car inventory management.

## Table of Contents
- [Technical Documentation for Django Car Rental REST Framework App](#technical-documentation-for-django-car-rental-rest-framework-app)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Installation and Setup](#installation-and-setup)
  - [Apps Overview](#apps-overview)
    - [Account](#account)
    - [Booking](#booking)
    - [CarDealer](#cardealer)
    - [Cars](#cars)
    - [Dealers](#dealers)
  - [API Endpoints](#api-endpoints)
  - [Database Models](#database-models)
    - [Account Models:](#account-models)
    - [Booking Models:](#booking-models)
    - [Cars Models:](#cars-models)
    - [Dealers Models:](#dealers-models)
  - [Authentication and Permissions](#authentication-and-permissions)
  - [Serializers](#serializers)
  - [Views](#views)
  - [Testing](#testing)
  - [Deployment](#deployment)

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd car_rental_project
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Apps Overview

### Account

- **Purpose:** Manages user registration, authentication, and profile management.
- **Key Features:**
  - User registration and login
  - User profile management
  - JWT-based authentication

### Booking

- **Purpose:** Handles car booking functionality.
- **Key Features:**
  - Create, view, update, and cancel bookings
  - Booking history for users
  - Booking validation 

### CarDealer

- **Purpose:** Manages dealership entities.
- **Key Features:**
  - Create and manage car dealerships
  - Associate cars with dealerships
  - Dealer information management

### Cars

- **Purpose:** Manages the car inventory.
- **Key Features:**
  - Add, update, and delete car listings
  - Car details (make, model, year, features, etc.)
  - Link cars with dealerships
  - Custom Car filter

### Dealers

- **Purpose:** Manages car dealer profiles.
- **Key Features:**
  - Dealer registration and profile management
  - Assign dealers to dealerships
  - Dealer-specific car inventory management

## API Endpoints
Kindly see relevant files in each app for endpoints
## Database Models

### Account Models:
- **User:** Custom user model with fields for first name, last name, email, etc.

### Booking Models:
- **Booking:** Stores booking information, such as user, car, start date, end date, and status.

### Cars Models:
- **Car:** Represents car information, including make, model, year, VIN, and association with a dealership.

### Dealers Models:
- **Dealer:** Represents dealer profiles with fields for name, contact information, and assigned dealership.

## Authentication and Permissions
- **Authentication:** JWT-based authentication is implemented using Django REST Framework’s `rest_framework_simplejwt`.
- **Permissions:** 
  - `IsAuthenticated` for most operations.
  - Custom permissions can be defined for actions like car management (e.g., only dealers can add or update car details).

## Serializers

Serializers are defined for each app to convert complex data types (like querysets and model instances) into JSON and vice versa.

- **Account Serializers:** `UserSerializer`, `RegisterSerializer`, `LoginSerializer`
- **Booking Serializers:** `BookingSerializer`
- **CarDealer Serializers:** `CarDealerSerializer`
- **Cars Serializers:** `CarSerializer`
- **Dealers Serializers:** `DealerSerializer`

## Views

Views handle the business logic and are responsible for processing incoming requests, interacting with models, and returning responses. The project primarily uses `APIView` and `ViewSet` classes from Django REST Framework.

- **Account Views:** Handles user registration, login, and profile management.
- **Booking Views:** Manages booking creation, retrieval, update, and deletion.
- **CarDealer Views:** Manages CRUD operations for car dealerships.
- **Cars Views:** Manages car inventory operations.
- **Dealers Views:** Manages dealer profiles and their associated cars.

## Testing

- **Test Tools:** `pytest-django`, `unittest`


## Deployment

For production deployment, consider using:

- **Web Server:** Gunicorn or uWSGI
- **Database:** PostgreSQL for scalability
- **Environment:** Docker for containerization, or a traditional setup using a virtual environment.
- **CI/CD:** Use GitHub Actions, CircleCI, or Jenkins



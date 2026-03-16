# Course_management_system

A highly modular backend system built with Django and Django REST Framework (DRF) to manage Vendors, Products, Courses, Certifications, and their respective mappings. 

This project strictly adheres to the requirement of using **only `APIView`** for all endpoints to demonstrate core DRF fundamentals.

## Features
* **Strict Modularity:** Every master entity and mapping resides in its own standalone Django app.
* **APIView Architecture:** Fully manual HTTP method implementation (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
* **Comprehensive Validation:** Includes unique constraints, duplicate mapping prevention, and single primary mapping rules.
* **Query Parameter Filtering:** Custom filtering logic implemented manually for relational data.
* **Interactive Documentation:** Fully automated Swagger and ReDoc UI using `drf-yasg`.
* **Bonus Implementations:** Includes a custom database seeding script and automated unit tests.

---

## Setup Steps

### 1. Prerequisites
Ensure you have Python 3.10+ and `pip` installed.

### 2. Clone the Repository
```bash
git clone [https://github.com/RitamPal26/Course_management_system.git](https://github.com/RitamPal26/Course_management_system.git)
cd Course_management_system
```

### 3. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Migration Steps

Initialize the SQLite database by running the standard Django migration commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Seed Data

To quickly populate the database with sample Vendors, Products, Courses, Certifications, and Mappings without manual data entry, run the custom seed command:

```bash
python manage.py seed_data
```

---

## Runserver Steps

Start the local development server:

```bash
python manage.py runserver
```

The API will now be accessible at `http://127.0.0.1:8000/`.

---

## API Documentation

Interactive API documentation is generated automatically . Navigate to the following URLs while the server is running:

* **Swagger UI:** [http://127.0.0.1:8000/swagger/](https://www.google.com/search?q=http://127.0.0.1:8000/swagger/)
* **ReDoc:** [http://127.0.0.1:8000/redoc/](https://www.google.com/search?q=http://127.0.0.1:8000/redoc/)

---

## Installed Apps

The project is structured into the following isolated applications :

**Master Apps:**

* `vendor`
* `product`
* `course`
* `certification`

**Mapping Apps:**

* `vendor_product_mapping`
* `product_course_mapping`
* `course_certification_mapping`

---

## API Usage Examples

Here are examples of how to interact with the API endpoints.

### 1. List All Vendors (GET)

```bash
curl -X GET [http://127.0.0.1:8000/api/vendors/](http://127.0.0.1:8000/api/vendors/)
```

### 2. Create a Product (POST)

```bash
curl -X POST [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/) \
-H "Content-Type: application/json" \
-d '{
    "name": "Cloud Storage Enterprise",
    "code": "PROD-CSE-001",
    "description": "Enterprise cloud storage solution",
    "is_active": true
}'
```

### 3. Filter Mappings via Query Parameters (GET)

Fetch all products mapped to a specific vendor (`vendor_id=1`) :

```bash
curl -X GET "[http://127.0.0.1:8000/api/vendor-product-mappings/?vendor_id=1](http://127.0.0.1:8000/api/vendor-product-mappings/?vendor_id=1)"
```

---

# CoffeeShop

Welcome to the CoffeeShop project! This is a Django-based web application designed to manage and showcase a coffee shop's menu, orders, and customer interactions.

## Features

- Display a dynamic menu of coffee and snacks.
- Manage customer orders and payments.
- Admin dashboard for managing inventory and sales.
- User authentication for customers and staff.

## Requirements

- Python 3.x
- Django 4.x
- SQLite (default) or any other database supported by Django

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/CoffeeShop.git
    cd CoffeeShop
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and visit `http://127.0.0.1:8000`.

## Mockdata
python manage.py seed [app] --number=10

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.



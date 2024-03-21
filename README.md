"# E-Commerce-Application" 
**Overview**:
This project is an E-Commerce web application built using Django, incorporating Bootstrap for frontend styling and PayPal for handling payments and shipping. The application allows users to browse through items, add them to their cart, and proceed to checkout, where they can securely pay for their purchases using PayPal.

**Features**:
User Authentication: Users can sign up, log in, and log out securely. Only authenticated users can proceed to checkout.

Product Management: Admin users can add, edit, and delete products. Each product has details like name, description, price, and image.

Cart Functionality: Users can add items to their cart while browsing the store. They can view and manage items in their cart before proceeding to checkout.

Checkout Process: Users can securely proceed to checkout using PayPal. Shipping details are collected during checkout, and users receive confirmation emails after successful purchases.

**Technologies Used**:
Django: Python-based web framework for building the backend of the application.
Bootstrap: Frontend framework for styling and responsive design.
PayPal API: Integration for processing payments and handling shipping.
SQLite: Default database used by Django for data storage. Can be swapped out for other databases supported by Django.
HTML/CSS/JavaScript: Frontend development languages for building the user interface and enhancing user experience.
Setup:
Clone the Repository: Clone this repository to your local machine using Git.


git clone (https://github.com/denny254/E-Commerce-Application.git)
Install Dependencies: Navigate into the project directory and install the required dependencies using pip.


cd your-repository
pip install -r requirements.txt
Database Setup: Apply migrations to set up the SQLite database.


python manage.py migrate
Create Superuser (Admin): Create a superuser to access the admin interface.

python manage.py createsuperuser
Run the Application: Start the Django development server.

python manage.py runserver
Access the Application: Open a web browser and go to http://localhost:8000 to access the application. Admin interface is available at http://localhost:8000/admin.

Configuration:
Settings: Update settings.py with your specific configurations, such as database settings, static files, email configurations, and PayPal API credentials.

Admin Access: Access the Django admin interface (/admin) to manage products, users, and orders.

PayPal Integration: Configure PayPal API credentials in the settings for handling payments and shipping.

Future Enhancements:
User Reviews and Ratings: Allow users to leave reviews and ratings for products.
Advanced Search and Filtering: Implement advanced search and filtering options for products.
Multiple Payment Gateways: Integrate additional payment gateways for more payment options.
Order Tracking: Provide order tracking functionality for users to track their shipments.
Responsive Design: Ensure the application is fully responsive across various devices for a seamless user experience.
Contributors:
Denny hi, thanks to my contributor dennis ivy for tutoring me.


# Valore - Luxury Watch E-commerce

<p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/static/img/relogio_preto.svg" title="Valore Watch Store" width="150"/>
</p>

## Overview

This project is an e-commerce platform prototype built with Django, specializing in the sale of luxury watches. It was developed as part of the Backend II course during my undergraduate program in Internet Systems Technology at IFRN (Federal Institute of Education, Science and Technology of Rio Grande do Norte). The platform aims to provide a seamless and elegant shopping experience, allowing users to browse a curated selection of high-end timepieces, manage their accounts, process orders, and handle payments.

The screenshots showcase key features of the application, including product listing, user profile management, order history, and checkout processes.

## Key Features

* **Product Catalog:** Browse a wide range of luxury watches with detailed descriptions and images (as seen in the homepage screenshot).
* **User Authentication:** Secure user registration and login functionality.
* **User Profile Management:** Users can manage their personal details, including name, contact information, and profile picture (as shown in the "Dados Pessoais" screenshot).
* **Address Management:** Users can add and manage multiple shipping addresses (as shown in the "Adicionar Endereço" and "Endereços Cadastrados" screenshots).
* **Payment Management:** Securely add and manage credit card details for purchases (as shown in the "Adicionar Cartão" and "Cartões Cadastrados" screenshots).
* **Order History:** Users can view their past orders with details on status, date, payment method, and shipping information (as shown in the "Meus Pedidos" screenshot).
* **Product Listing & Addition (Admin/Seller Feature):** Functionality to add new products to the catalog, including description, price, and category (as shown in the "Adicionar Produto" screenshot).
* **Order Tracking:** (The "SEU ÚLTIMO PEDIDO" screenshot suggests order tracking with status updates).

## Technologies Used

* **Django:** A high-level Python web framework used for building the backend of the e-commerce platform.
* **Python:** The primary programming language.
* **Docker:** Containerization of the application
* **HTML, CSS, JavaScript:** For the frontend structure, styling, and interactivity.
* **Database:** Standart Django SQLite.
* **Pillow** Imagem processing.
* **Django Widget Tweaks** Customize Django Forms inputs.

## Screenshots

The following screenshots provide a visual overview of the application:

* **Homepage:** Displays a selection of luxury watches available for browsing.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_.png" title="Valore Watch Store" width="800" />
  </p>
* **Registration:** User registration form.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_auth_register_.png" title="Valore Watch Store" width="800" />
  </p>
* **Login:** User login form.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_auth_login_.png" title="Valore Watch Store" width="800" />
  </p>
  * **User index / Last order tracking:** Shows the details and status of a specific order.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user.png" title="Valore Watch Store" width="800" />
  </p>
* **Personal Data:** Section for users to manage their personal information and profile picture.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user_meusdados_.png" title="Valore Watch Store" width="800" />
  </p>
* **Add Product:** Form for adding new watch listings to the platform.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user_meusprodutos_adicionar_.png" title="Valore Watch Store" width="800" />
  </p>
* **Add Card:** Interface for users to add their credit card details for payments.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user_meuscartoes_.png" title="Valore Watch Store" width="800" />
  </p>
* **Add Address:** Form for users to input and save their shipping addresses.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user_enderecos_.png" title="Valore Watch Store" width="800" />
  </p>
* **My Orders:** Displays a history of the user's past orders with status and details.
  <p align="center">
    <img src="https://github.com/phaa/valore-watch-store/blob/main/screenshots/localhost_8000_user_pedidos_.png" title="Valore Watch Store" width="800" />
  </p>

## Get the project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/phaa/valore-watch-store.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd valore-watch-store
    ```


## Run with Docker

To run the project using a simple script, follow these steps:

3. Make sure you have Docker and Docker Compose installed.

4. From the root of the project, run the `start.sh` script:

    ```bash
    sudo chmod +x start.sh
    ./start.sh
    ```

The script will ask if you want to rebuild the Docker image. Answer `y` (yes) the first time or if you made changes to the `Dockerfile` or its dependencies. Otherwise, answer `n` (no).

5. The project will be available at `http://localhost:8000`. Migrations will be automatically done by docker-compose.

To stop the Docker containers, run the following command from the root of the project:

    ```bash
    docker-compose down
    ```

## Run without Docker

3.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Configure the database:**
    * Update the database settings in `settings.py`.
    * Run migrations:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
8.  **Access the application in your browser at `http://127.0.0.1:8000/`.**

## Potential Future Enhancements

* Advanced product filtering and search options.
* User reviews and ratings for products.
* Wishlist functionality.
* More detailed product pages with multiple images and specifications.
* Integration with more payment gateways.
* Order management and fulfillment system for administrators.
* Email notifications for order updates.

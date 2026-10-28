# 🍎 Fresh_Picked_Paradise – Fruit & Grocery Shopping Website

Frutika is a web-based fruit and grocery shopping website developed using **Python, Django, HTML, CSS, JavaScript, and Bootstrap**. The project provides a user-friendly interface for browsing products, viewing monthly deals, and exploring different sections of the website. It also includes an **AI-powered customer support chatbot** using the Google Gemini API to answer customer questions based on available website information.

## 🚀 Features

- **Home Page:** Displays products, website branding, and monthly deals.
- **Product Management:** Store and manage product names, prices, titles, and images using Django models.
- **Monthly Deals:** Display promotional offers and product information.
- **Multiple Pages:** Home, About, Shop, News, Contact, Cart, Checkout, and product and news detail pages.
- **Django Admin Panel:** Manage products, monthly deals, and logos through the admin interface.
- **AI Customer Support Chatbot:** Uses Google Gemini to answer customer questions about the website.
- **Database Integration:** Uses SQLite to store website data.
- **Responsive UI:** Built using HTML, CSS, JavaScript, and Bootstrap.
- **Media Management:** Supports uploaded product images, promotional images, and logos.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework and routing |
| HTML5 | Website structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions |
| Bootstrap | Responsive UI components |
| SQLite | Database |
| Google Gemini API | AI chatbot responses |
| Django ORM | Database operations |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
frutika/
├── frutika/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── index/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── shop.html
│   ├── contact.html
│   ├── cart.html
│   ├── checkout.html
│   ├── news.html
│   └── layouts.html
├── static/
├── assets/
├── media/
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Navigate to the project directory

```bash
cd frutika
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django pillow google-genai
```

### 5. Configure the Google Gemini API key

Set your API key as an environment variable in PowerShell:

```powershell
$env:GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

Get an API key from [Google AI Studio](https://aistudio.google.com/).

Keep your API key private. Do not commit it to GitHub.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

### 8. Run the development server

```bash
python manage.py runserver
```

Open the website in your browser:

http://127.0.0.1:8000/

Access the Django admin panel at:

http://127.0.0.1:8000/admin/

## 🤖 AI Customer Support Chatbot

The project integrates the Google Gemini API to provide AI-powered customer support.

**How it works:**

1. The customer enters a question in the chatbot.
2. The Django backend receives the question through the chatbot API endpoint.
3. Product, logo, and monthly-deal information is collected from the database.
4. The website information and customer question are sent to the Gemini model.
5. The AI generates a response and returns it to the frontend as JSON.

**Key implementation details:**
- Django endpoint: `/chatbot-api/`
- HTTP method: POST
- AI provider: Google Gemini
- Backend validation for empty and excessively long questions
- Retry handling for temporary AI server errors

The chatbot requires a valid Google Gemini API key and a working API connection.

## 🗄️ Database Models

The project includes the following Django models:

- **Product:** Stores product title, name, price, and image.
- **Monthly Deal:** Stores promotional offer details, name, description, and image.
- **Logo:** Stores website logo titles and image files.

These models can be managed through Django's admin interface.

## 🎯 Project Objectives

- Develop a dynamic website using Django.
- Understand URL routing, views, templates, and models.
- Perform database operations using Django ORM.
- Manage uploaded media and static files.
- Integrate a third-party generative AI API into a web application.
- Build practical full-stack development skills.

## 🔮 Future Enhancements

- Implement user registration and login.
- Add functional shopping cart and order management.
- Integrate a secure online payment gateway.
- Add product search, filtering, and category management.
- Improve chatbot responses with more structured product data.
- Add automated tests and deploy the application to a production server.

## 👨‍💻 Learning Outcomes

Through this project, I gained practical experience in Python and Django development, database management, frontend integration, API integration, and building an AI-powered customer support feature.

## 📌 Project Status

Developed as a learning and portfolio project. Some pages represent website interfaces, and additional backend functionality may be required for a complete production-ready e-commerce application.

---

**If you find this project useful, feel free to explore the repository!**

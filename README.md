### WebScrap

This project aims to scrape data from two websites and display it on a Django-powered web application. Follow the steps below to set up and run the project:

#### Prerequisites
- Git installed on your system
- Python 3.10 installed on your system
- Virtual environment (optional but recommended)

#### Installation and Setup
1. **Clone the Git repository:**
- git clone "https://github.com/Gopal-Singh-Cis/WebScrap.git"

2. **Navigate to the project directory:**

3. **(Optional) Create and activate a virtual environment:**
- python3.10 -m venv venv
- source venv/bin/activate


4. **Install project dependencies:**
- pip install -r requirements.txt

5. **Migrate all database migrations:**

- python manage.py makemigrations
- python manage.py migrate


6. **Start the Django local server:**
- python manage.py runserver


#### Scraping Websites
1. in the navbar you can see the link for scrap site where you get two options initially click one of them to scrap data
- myjoyonline
- The business and financial times

2. afetr successfull scrapping you see success message and a button to redirect to home page where you can see the scrapped data.

#### Additional Notes
- Ensure that your virtual environment is activated while running the project and installing dependencies.
- Make sure to run migrations before starting the Django server to set up the database schema.
- After scraping the websites, the data will be available for display on the home page.
- For any further assistance or inquiries, refer to the project documentation or contact the project maintainers.
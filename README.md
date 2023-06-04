# Chatbot with GPT-3.5 Turbo and Document Analysis

This is a chatbot that connects to the GPT chat API and uses the GPT-3.5 Turbo model to read, understand, analyze, and modify documents. It utilizes various technologies and libraries such as Google Cloud Storage for file storage, Firebase for database, Django Rest Framework for creating APIs, and Djoser for Authentication.


## Features
- Connects to the GPT chat API and uses the GPT-3.5 Turbo model to read, understand, analyze, and modify documents.
- Supports Office suite and PDF documents.
- Uses Django backend with REST API, MySQL, and Firebase.
- Incorporates TensorFlow for unsupervised learning.
- Uses React frontend with Vite and JavaScript for a seamless user experience.
- Supports two modes: light and dark mode with a complete color palette change.
- Supports responsive design for different screen sizes.

## Getting Started
To get started with the project, follow these steps:

1. Clone this repository to your local machine using `https://github.com/oardilac/ChatGPT-3.5-Django-React.git`.
2. Navigate to the project directory.
3. Create a new virtual environment: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (for macOS and Linux) or `.\env\Scripts\activate` (for Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Rename `env.template` to `.env` and fill in your OpenAI API credentials and Google Cloud Storage and Firebase credentials.
7. Apply the migrations: `python manage.py migrate`
8. Run the Django backend using `python manage.py runserver`.
9. Navigate to `http://127.0.0.1:8000/init/` in your web browser to access the chatbot.

## Usage
- To upload a file, send a `POST` request to `/init/` with the file attached in the form data.
- To input text, send a `POST` request to `/init/text/` with the `fname` (chatbot's name) and `lname` (input text) in the form data.
- You can explore the API documentation by visiting `/swagger/`.

## Technologies Used
- Django
- REST API
- MySQL
- Firebase
- TensorFlow
- React
- Vite
- JavaScript
- HTML5
- CSS3
- Sass

## Contributors
- [Oliver Ardila](https://github.com/oardilac)
- [Sebastian Escobar](https://github.com/YummySalamy)

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
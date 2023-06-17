<a name="readme-top"></a>
[![Contributors](https://shields.io/badge/Contributors-1-green)](https://github.com/oardilac/ChatGPT-3.5-Django-React/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/oardilac/ChatGPT-3.5-Django-React)](https://github.com/oardilac/ChatGPT-3.5-Django-React/network/members)
[![Stargazers](https://img.shields.io/github/stars/oardilac/ChatGPT-3.5-Django-React)](https://github.com/oardilac/ChatGPT-3.5-Django-React/stargazers)
[![Issues](https://img.shields.io/github/issues/oardilac/ChatGPT-3.5-Django-React)](https://github.com/oardilac/ChatGPT-3.5-Django-React/issues)
[![MIT License](https://img.shields.io/github/license/oardilac/ChatGPT-3.5-Django-React)](https://github.com/oardilac/ChatGPT-3.5-Django-React/blob/main/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/oardilac/)
<br />
<div align="center">
    <h3 align="center">ChatGPT Personalized: Django & React Backend</h3>

   <p align="center">
   About
AI-powered chatbot with GPT-3.5 Turbo model for document analysis, modification, and image insertion.
    <br />

  <p align="center">
    <a href="https://github.com/oardilac/ChatGPT-3.5-Django-React/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/oardilac/ChatGPT-3.5-Django-React/">View Demo</a>
    ·
    <a href="https://github.com/oardilac/ChatGPT-3.5-Django-React/issues">Report Bug</a>
    ·
    <a href="https://github.com/oardilac/ChatGPT-3.5-Django-React/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

There are many great README templates available on GitHub; however, this project deserved a custom one. This backend application is built for the personalized ChatGPT model, a powerful conversational AI model, enhanced with Django and React. The main purpose of this project is:

* To provide a robust backend for managing and interacting with a personalized instance of ChatGPT.
* To implement the principles of DRY ("Don't Repeat Yourself") to the fullest extent, allowing us to focus on creating an innovative and useful service.

Of course, the needs of every project are different. If you have any suggestions or improvements, feel free to contribute to this project by creating a pull request or opening an issue.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project's backend has been built using the following major frameworks:

* [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
* [![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-BA68C8?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
* [![OpenAI's ChatGPT](https://img.shields.io/badge/OpenAI%20ChatGPT-000000?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

1. Python3
2. Pip3
3. Django

To install Django, use pip:
```
pip install django
```
### Installation

1. Clone the repo

    ```
    git clone https://github.com/oardilac/ChatGPT-3.5-Django-React.git
    ```

2. Install required packages

    ```
    pip install -r requirements.txt
    ```

3. Make Django migrations to create your database schema:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

This Django backend provides several API endpoints for managing the personalized ChatGPT instance, including endpoints for uploading files, storing text, saving URLs, and scraping sitemaps.

In order to run the backend server, you need to:

1. Clone this repository
2. Set up a Python virtual environment and install the dependencies listed in the `requirements.txt` file.
3. Start the server by running `python manage.py runserver`.

To interact with the backend:

- To create a chatbot, make a POST request to `http://127.0.0.1:8000/chatbots/chatbots/`.
- To upload files, make a POST request to `http://127.0.0.1:8000/chatbots/uploadfiles/`.
- To save a URL, make a POST request to `http://127.0.0.1:8000/chatbots/saveurl/`.
- To scrape a sitemap, make a POST request to `http://127.0.0.1:8000/chatbots/scrapesitemap/`.

_For more examples, please refer to the [API Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Implement frontend in React.js
- [ ] Deploy the project on a server
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/oardilac/ChatGPT-3.5-Django-React/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Oliver Ardila - @oardilac - odardilacueto@gmail.com

Project Link: [https://github.com/oardilac/ChatGPT-3.5-Django-React](https://github.com/oardilac/ChatGPT-3.5-Django-React)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Firstly, I'd like to acknowledge the amazing work by the OpenAI team for creating the core engine, [ChatGPT](https://github.com/openai/gpt-3), that powers the conversational abilities of this project. The backend wouldn't have been as interactive without their expertise in the field of AI.

Next, I must credit the [Django Project](https://www.djangoproject.com/) and its numerous contributors for developing and maintaining the Django framework. The secure and scalable foundation it provides has significantly eased the development of the backend for this project.

As for the web development, this project has benefited immensely from the modern, scalable, and developer-friendly JavaScript library, [React](https://react.dev/). It has enabled us to build an interactive user interface seamlessly.

We have used [Django REST framework](https://www.django-rest-framework.org/), which is a powerful and flexible toolkit for building Web APIs in Django. Its vast range of functionalities has been instrumental in handling API requests effectively.

For handling the database models and ensuring smooth communication with the database, [Django ORM](https://docs.djangoproject.com/en/3.2/topics/db/models/) has been an invaluable tool. It has simplified data manipulation in Python by allowing the database schema to be defined as Python classes.

Finally, I would like to thank the team behind [Djoser](https://djoser.readthedocs.io/en/latest/), the Django library we used for JWT authentication. Djoser's easy-to-use API endpoints for registration and authentication have made managing user authentication in this project straightforward.

Other resources that were instrumental in the success of this project include:

* [Django](https://www.djangoproject.com/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Google Cloud Platform (GCP)](https://cloud.google.com/) - A suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products.
* [Img Shields](https://shields.io/) - For providing README badges.


<p align="right">(<a href="#readme-top">back to top</a>)</p>
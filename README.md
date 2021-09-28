<h1 align="center">URL Shortener - Back-end</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/yashranjan/URLShortener/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/yashranjan/URLShortener/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> The backend of an URL shortener website which automatically shortens the entered lengthy URL.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

This is the backend of an URL website. Go to this [link](https://github.com/yashranjan/URLShortener-React) to know further.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure that you've python>=3.6, virtualenv and pip3 installed. If not, then follow the instructions from the official documentation for your OS to install the same.

### Installing

To get the setup up and running, follow the below steps

1 Clone the repo

```
 git clone https://github.com/yashranjan/URLShortener && cd URLShortener
```

2 Create a virtual env for running the backend, so that every package dependency is local to this project only

```
virtualenv venv -p python3.x
source venv/bin/activate
```

3 Install the requirements mentioned in the requirements.txt

```
pip -r requirements.txt
```

4 Start the development server and then open localhost:8000 in the browser

```
python manage.py runserver
```

5 Though there's nothing visually appealing website in this repo, you can clone the frontend ([link](https://github.com/yashranjan/URLShortener-React)) as well to use/test all the APIs of backend.

## 🖥️ The website is hosted here <a name = "try_here"></a>

https://urlshortenert.netlify.app/

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Server Framework
- [MongoDB](https://www.mongodb.com/) - Database

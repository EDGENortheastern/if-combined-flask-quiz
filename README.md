# Flask Quiz App

A Flask web application that presents a single-question general‑knowledge quiz and stores user answer in a CSV file.

## User Guide



## 📘 Introduction to Flask

[Flask](https://flask.palletsprojects.com/en/stable/) is a lightweight web framework for Python. It provides tools to build web applications quickly while staying minimal and flexible. Unlike larger frameworks, Flask does not impose structure—you choose how your project grows.

Key concepts used in this project:

- **Routes** — URLs that run Python functions  
- **Templates** — HTML files rendered with dynamic content  
- **Static files** — CSS, images, JavaScript  
- **Request handling** — Reading form submissions  
- **Local storage** — Writing data to CSV  

To learn more about Flask, visit the official documentation:  
https://flask.palletsprojects.com/

Additional Flask resources:  
Flask Quickstart — https://flask.palletsprojects.com/en/latest/quickstart/  
Flask Tutorial — https://flask.palletsprojects.com/en/latest/tutorial/  

## 🔧 Creating a Virtual Environment (venv)

Below are instructions for macOS, Linux, and Windows.

### macOS / Linux

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

### Windows (PowerShell)

Create the virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\Activate
```

Install Flask:

```bash
pip install flask
```

## 🧠 About This Application

This project demonstrates:

- A basic Flask server  
- One‑question‑at‑a‑time quiz flow  
- HTML templates
- Input handling using forms  
- Local CSV file storage for quiz results  

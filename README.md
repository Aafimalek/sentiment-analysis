
# Sentiment Analysis Web Application

![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Flask](https://img.shields.io/badge/Flask-2.0+-red) ![Docker](https://img.shields.io/badge/Docker-20.10+-blue) ![Sklearn](https://img.shields.io/badge/Scikit--Learn-0.24+-orange) ![Joblib](https://img.shields.io/badge/Joblib-1.0+-green)

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Docker Deployment](#docker-deployment)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## About the Project

This is a **Sentiment Analysis Web Application** that allows users to analyze the sentiment of text inputs (e.g., tweets). The app uses a machine learning model built with `scikit-learn` to classify text as positive or negative. Users can interact with the model via a modern, minimalistic frontend designed for simplicity and ease of use.

This application can be deployed locally or using Docker, and it's set up to be easily accessible through Docker Hub for streamlined deployment.

--view live at:- https://sentiment-analysis-uyeg.onrender.com/
## Features

- **Sentiment Analysis:** Classify input text into positive, negative, or neutral sentiment.
- **User-Friendly Interface:** Clean, modern UI built with HTML and CSS for intuitive usage.
- **Containerized Deployment:** Easily deploy the application via Docker with minimal configuration.
- **Pre-trained Model:** Model pre-trained with sklearn and saved using Joblib for quick loading and inference.

## Technologies Used

- **Python 3.10**
- **Flask** - Web Framework
- **scikit-learn** - Machine Learning Library
- **Joblib** - For saving and loading ML models
- **Docker** - Containerization for easy deployment
- **HTML & CSS** - Frontend design

## Directory Structure

```plaintext
sentiment-analysis
│app
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration file
│
├── templates/
│   └── index.html         # Frontend HTML file
│
└── static/
    ├── css/
    │   └── style.css      # Styling for the frontend
```

## Getting Started

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aafimalek/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

To run the application locally without Docker:

1. Make sure all dependencies are installed.
2. Start the Flask app:

   ```bash
   python app.py
   ```

3. Open your browser and go to [http://localhost:8080](http://localhost:8080) to view the application.

### Docker Deployment

#### Building the Docker Image

1. Make sure Docker is installed on your machine.
2. Build the Docker image:

   ```bash
   docker build -t aafimalek2032/sentiment-analysis .
   ```

#### Running the Docker Container

Run the container using:

```bash
docker run -p 8080:8080 aafimalek2032/sentiment-analysis
```

Now, the application should be accessible at [http://localhost:8080](http://localhost:8080).

#### Pushing to Docker Hub

1. Log in to Docker Hub:

   ```bash
   docker login
   ```

2. Tag and push the image:

   ```bash
   docker tag aafimalek2032/sentiment-analysis aafimalek2032/sentiment-analysis:latest
   docker push aafimalek2032/sentiment-analysis:latest
   ```

Now, your image is available on Docker Hub at `aafimalek2032/sentiment-analysis`.

## Usage

- Enter the text you want to analyze in the input field.
- Click **Analyze** to get the sentiment classification.
- The result will show whether the sentiment is **Positive** or **Negative**.



## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

**Aafimalek**  
[GitHub](https://github.com/Aafimalek) | [DockerHub](https://hub.docker.com/u/aafimalek2032) | [Email](mailto:aafimalek2023@gmail.com)

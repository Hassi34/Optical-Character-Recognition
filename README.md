<p align="center">
    <b>
        <h1 align="center">Optical Character Recognition</h1>
    </b>
</p>
<p align="center">
<a href="https://github.com/Hassi34/Optical-Character-Recognition">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&c=g&size=18&duration=3000&pause=6000&multiline=True&center=true&width=800&height=40&lines=Vision AI service ( REST API ) for OCR ( optical character recognition );" alt="Typing SVG" />
</a>
</p>
<p align="center">
<a href="https://github.com/Hassi34/Optical-Character-Recognition">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&size=18&duration=2000&pause=1500&multiline=False&color=10D736FF&center=true&width=400&height=40&lines=AI+%7C+Computer+Vision+%7C+REST+API;Python+%7C+3.7+%7C+3.8+%7C+3.9+%7C+3.10;FastAPI+%7C+Docker;" alt="Typing SVG" />
</a>
</p>

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img alt="License" src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-g.svg">
    </a>
    <a href="https://github.com/Hassi34/Optical-Character-Recognition">
        <img alt="Last Commit" src="https://img.shields.io/github/last-commit/hassi34/Optical-Character-Recognition/main?color=g">
    </a>
    <a href="https://github.com/Hassi34/Optical-Character-Recognition">
        <img alt="Code Size" src="https://img.shields.io/github/languages/code-size/hassi34/Optical-Character-Recognition?color=g">
    </a>
    <a href="https://github.com/Hassi34/Optical-Character-Recognition">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/hassi34/Optical-Character-Recognition?color=g">
    </a>
    <a href="https://github.com/Hassi34/Optical-Character-Recognition/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/hassi34/Optical-Character-Recognition?color=g">
    </a>

## Overview
This project contains the implementation of REST API empowered by Vision AI to detect the text available in the input image. The REST API services are being distributed through the docker image. You can pull the image from [Docker Hub](https://hub.docker.com/r/hassi34/optical-character-recognition). The image comes as production-ready with unit tests and a standard algorithm implemented which can be used to expose the REST API to the web.<br>
**Following are the major contents to follow, you can jump to any section:**

>   1. [Run Locally](#run-local)
>   2. [REST API with Docker](#rest-api)<br>
>      - [Pull Image From Docker Hub](#docker-pull)<br>
>      - [Docker Container](#docker-container)<br>
>           - [Run a Docker Container](#run-docker-container)<br>
>           - [Perform Unit Tests](#unit-tests)<br>
>           - [API documentation](#api-docs)<br>
>      - [Make an API Request](#request-api)<br>

## Run Locally<a id='run-local'></a>

* Ensure you have [Python 3.7+](https://www.python.org/downloads/) installed.

* Create a new Python Conda environment:

```bash
conda create -n ocr python=3.10  # create ocr
conda activate ocr  # activate ocr
```
OR
* Create a new Python virtual environment with pip:
```bash
virtualenv ocr --python=python3.10  # create ocr
source ocr/bin/activate   # activate ocr
```
Install dependencies

```bash
  pip install -r requirements.txt
```
or
```bash
 conda env create -f environment.yaml
```

Clone the project

```bash
  git clone https://github.com/Hassi34/Optical-Character-Recognition.git
```

Go to the project directory

```bash
  cd Optical-Character-Recognition
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```
## REST API with Docker<a id='rest-api'></a>
To run the following sequence of commands, make sure you have the docker installed on your system.

### Pull Image from Docker Hub<a id='docker-pull'></a>
In case you have not already pulled the image from the Docker Hub, you can use the following command:
```bash
docker pull hassi34/optical-character-recognition
```

### Docker Container<a id='docker-container'></a>
Now once you have the docker image from the Docker Hub, you can now run the following commands to test and deploy the container to the web

* Run a Docker Container<a id='run-docker-container'></a><br>
Check all the available images:
```bash
docker images
```
Use the following command to run a docker container on your system:
```bash
docker run --name <CONTAINER NAME> -p 80:80 -d <IMAGE NAME OR ID>
```
Check if the container is running:
```bash
docker ps
```
If the container is running, then the API services will be available on all the network interfaces<br>
Type **``localhost``** in the browser and see if you get the success message from the API service.

* Perform Unit Tests<a id='#unit-tests'></a><br>
After when the API services are up and running, run the following command on the terminal to perform the unit test:
```bash
docker exec -it <CONTAINER NAME OR ID> pytest
```
* API documentation<a id='api-docs'></a><br>
The automatic API documentation will be available at http://localhost/docs

### Make an API Request<a id='request-api'></a>
Use the following script as a reference to make a REST API request:

```python
import requests
import base64

BASE64_STR = "" 
ENDPOINT = "http://127.0.0.1/predict"


def encodeImageIntoBase64(IN_IMG_PATH):
    with open(IN_IMG_PATH, "rb") as f:
        return base64.b64encode(f.read())

if __name__ == '__main__':
    response = requests.post(ENDPOINT, json={"base64_str":BASE64_STR})
    if response.status_code == 200:
        response = response.json()
        print(response)
    else :
        print(response)
```
#### **Thank you for visiting 🙏 I hope you find this project useful**<br><br>

#### **📃 License**
[MIT][license] © [Hasanain][website]

[license]: https://github.com/Hassi34/Optical-Character-Recognition/blob/main/LICENSE
[website]: https://hasanain.aicaliber.com

**Copyright &copy; 2023 Hasanain** <br>
Let's connect on **[``LinkedIn``](https://www.linkedin.com/in/hasanain-mehmood)** <br>
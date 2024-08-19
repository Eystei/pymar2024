# Cat GIF Flask App

This is a simple Flask application that displays a random cat GIF on each page load.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this application, you need to have Docker installed. Installation instructions for Docker can be found on the [official Docker website](https://docs.docker.com/get-docker/).

### Installing

Follow these steps to get your application running locally:

### Building the Docker Image

Build the Docker image using the following command:

```
docker build -t my-python-app .
```

### Running the Container
```
docker run -p 8866:5001 --name my-python-app my-python-app
```
### Viewing the Application
```
http://localhost:8866
```
### Stopping and Removing the Container
```
docker stop my-python-app
docker rm my-python-app
```

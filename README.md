# URL shortener

A service that lets you shorten a URL.

## Technology

* Python
* Flask
* SQLAlchemy

## Functionality

A Url shortening tool which does the following:

* Users should be able to enter a url into an input box on your website's front page
* If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to it

## Installation & Usage

### Installation

* Create the virtual environemnt with `pipenv shell`
* Run `pipenv install` to install packages

### Usage

* Run `pipenv shell` to start the virtual environment
* Run `pipenv run dev` to start the server at localhost:5000

## Wins & Challenges

### Wins

* Getting SQLAlchemy to work with the server
* Understanding how the redirects work

### Challenges

* Creating the model with the `__repr__` function
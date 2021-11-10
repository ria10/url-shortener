# URL shortener

##Technology
* Python flask

## Functionality
A Url shortening tool which does the following:
* Users should be able to enter a url into an input box on your website's front page
* If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to it

## Installation
* Create the virtual environemnt with `pipenv shell`
* Run `pipenv install` to install packages
* Run `pipenv run dev` to run the server which should open on localhost:5000
* On the home page click on the link to take you to `http://localhost:5000/shorten`
* On `http://localhost:5000/shorten` to enter the homepage where you can enter your url and click the submit url button
* Then you are presented with your shortened link

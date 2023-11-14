# 0x1A. Application server


##### Application Server Configuration

This project contains configurations and scripts for setting up and configuring an application server, for an AirBnB clone project.

## Flask Web Application

#### File: `web_flask/0-hello_route.py`: 
  - Basic Flask web application with a simple route that responds with "Hello HBNB!"

## Nginx Configuration

#### File: `2-app_server-nginx_config`: 
  - Nginx configuration file to serve a Flask web application at `/airbnb-onepage/`, proxying requests to port 5000.

## Nginx Configuration with Multiple Routes

#### File: `3-app_server-nginx_config`: 
  - Nginx configuration file to handle multiple routes, including proxying requests to port 5001 for dynamic content.

## Gunicorn Configuration for RESTful API

#### File: `4-app_server-nginx_config`: 
  - Nginx configuration file to route requests to a Gunicorn instance serving a RESTful API on port 5002.

## Web Dynamic Configuration

#### File: `5-app_server-nginx_config`: 
  - Nginx configuration file for serving a Gunicorn instance running `web_dynamic/2-hbnb.py` on port 5003.

## Systemd Service Configuration

#### File: `gunicorn.service`: 
  - Systemd service script for starting a Gunicorn process to serve `web_dynamic/2-hbnb.py` with 3 worker processes, logging errors to `/tmp/airbnb-error.log` and access to `/tmp/airbnb-access.log`.

## Reload Gunicorn with No Downtime

#### File: `4-reload_gunicorn_no_downtime`: 
  - Bash script for gracefully reloading Gunicorn without downtime by signaling the master process.

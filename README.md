# nginx_uwsgi_testing

This repo contains some testing files related to building out a 
minimal server implementation for use on a Raspberry Pi 3 Model B.

It expects a python virtual environment in venv under /var/www/demoapp/.

The code contained herein was built on Python 3.5.3.

Web server:  Nginx.
Python app server: UWSGI.

Implements static and dynamic web pages.

Database connectivity is bolted on since it is integral to most 
non-trivial apps. The database connection credentials file is moved 
outside of the git repository directory to protect this information
from inadvertent upload to github. The parent directory location is
also unreachable by the webserver itself when loaded to the server.

This remains and active work in progress...

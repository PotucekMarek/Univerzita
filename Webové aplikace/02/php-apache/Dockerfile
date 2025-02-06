FROM php:8.1-apache

# Instalace rozšíření mysqli
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

# Nastavení ServerName pro Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Kopírování chybějících souborů do webového adresáře
COPY ./public-html/css/custom.css /var/www/html/css/custom.css
COPY ./public-html/bootstrap-icons.css /var/www/html/bootstrap-icons.css
COPY ./public-html/bootstrap.js /var/www/html/bootstrap.js
COPY ./public-html/fonts/bootstrap-icons.woff2 /var/www/html/fonts/bootstrap-icons.woff2
COPY ./public-html/fonts/bootstrap-icons.woff /var/www/html/fonts/bootstrap-icons.woff

# Kopírování index.html do webového adresáře
COPY ./public-html/index.html /var/www/html/index.html
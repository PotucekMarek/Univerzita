# Use an official PHP runtime as a parent image
FROM php:8.2-apache

# Set the working directory
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Install required PHP extensions
RUN docker-php-ext-install mysqli

# Expose port 80 to the outside world
EXPOSE 80

# Set the default command to run when starting the container
CMD ["apache2-foreground"]
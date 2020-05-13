dnf update && dnf upgrade
dnf install httpd
dnf install mariadb mariadb-client
dnf install mysql-php
dnf install unzip wget
wget https://wordpress.org/latest.zip
unzip latest.zip
cd latest
cp * /var/www/html
echo "Now please configure MySQL/MariaDB"
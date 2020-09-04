SHOW DATABASES;

CREATE USER 'webuser'@'%' IDENTIFIED BY '1234';

GRANT ALL PRIVILEGES ON django_ex_db.* TO 'webuser'@'%';


CREATE USER 'iot_user'@'%' IDENTIFIED BY '1234';

GRANT ALL PRIVILEGES ON sqlDB.* TO 'iot_user'@'%';
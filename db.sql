-- Create user and set password
CREATE USER 'Sarvajith'@'%' IDENTIFIED BY '12345';

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS med2;

-- Grant all privileges to the user on the database
GRANT ALL PRIVILEGES ON med2.* TO 'Sarvajith'@'%';

-- Apply the changes and reload privileges
FLUSH PRIVILEGES;

-- Use the newly created database
USE med2;

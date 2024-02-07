CREATE DATABASE pal_collector;

CREATE USER fritzhuie WITH PASSWORD '1234567890';

GRANT ALL PRIVILEGES ON DATABASE pal_collector TO fritzhuie;

ALTER DATABASE pal_collector OWNER TO fritzhuie;
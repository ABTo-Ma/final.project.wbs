-- Create the initial Database for the WBS_DS_29 Project. It will contain five tables 
DROP DATABASE IF EXISTS sql_database_wbs_ds_29_project;
CREATE DATABASE sql_database_wbs_ds_29_project;
USE sql_database_wbs_ds_29_project;
CREATE TABLE diseases (
	disease_id INT AUTO_INCREMENT,
    disease_name VARCHAR (100) NOT NULL,
    disease_cause VARCHAR (100),
    disease_transmission VARCHAR (100),
    disease_incubation_period_min INT,
    disease_incubation_period_min_unit VARCHAR (50),
    disease_incubation_period_max INT,
    disease_incubation_period_max_unit VARCHAR (50),
    disease_contagious_period VARCHAR (50),
    disease_contagious_period_unit VARCHAR (50),
    PRIMARY KEY (disease_id)
);
CREATE TABLE countries (
	country_id INT AUTO_INCREMENT,
    country_name VARCHAR (100) NOT NULL,
    country_continent VARCHAR (50),
    country_longitude DECIMAL (9, 6),
    country_latitude DECIMAL (9, 6),
    country_official_languages VARCHAR (200),
    country_iso_code CHAR (3),
    PRIMARY KEY (country_id)
);
CREATE TABLE vaccines (
	vaccine_id INT AUTO_INCREMENT,
    vaccine_antigen VARCHAR (100) NOT NULL,
    vaccine_type VARCHAR (50),
    vaccine_dose INT,
    vaccine_dose_interval_value INT, 
    vaccine_dose_interval_unit VARCHAR(50),
    vaccine_target_population VARCHAR (255),
    disease_id INT,
    PRIMARY KEY (vaccine_id),
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);
CREATE TABLE diseases_stats_per_countries (
	disease_stat_id INT AUTO_INCREMENT,
    disease_stat_year INT NOT NULL,
    disease_stat_cases INT,
    country_id INT,
    disease_id INT,
    PRIMARY KEY(disease_stat_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);
CREATE TABLE vaccines_stats_per_countries (
	vaccine_stat_id INT AUTO_INCREMENT,
    vaccine_stat_year INT NOT NULL,
    vaccine_stat_applied INT,
    country_id INT,
    vaccine_id INT,
    PRIMARY KEY (vaccine_stat_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (vaccine_id) REFERENCES vaccines(vaccine_id)
);
SELECT @@hostname;
SELECT user();
SHOW VARIABLES WHERE Variable_name = 'port';
SHOW VARIABLES WHERE Variable_name = 'hostname';
SELECT * FROM diseases;
SELECT * FROM diseases_stats_per_countries;
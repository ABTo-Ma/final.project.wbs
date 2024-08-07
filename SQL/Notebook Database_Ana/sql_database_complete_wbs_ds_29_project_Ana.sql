-- Create the initial Database for the WBS_DS_29 Project. It will contain five tables 
DROP DATABASE IF EXISTS sql_database_complete_wbs_ds_29_project;
CREATE DATABASE sql_database_complete_wbs_ds_29_project;
USE sql_database_complete_wbs_ds_29_project;
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
    country_code VARCHAR(255) NOT NULL, -- Code of the country
    country_name VARCHAR(255) NOT NULL, -- Name of the country
    -- country_latitude DOUBLE NOT NULL, -- Latitude of the country
    -- country_longitude DOUBLE NOT NULL, -- Longitude of the country
    PRIMARY KEY (country_id) -- Primary key to uniquely identify each country
);
CREATE TABLE vaccines (
	vaccine_id INT AUTO_INCREMENT,
    vaccine_description VARCHAR (250),
    PRIMARY KEY (vaccine_id)
);
CREATE TABLE vaccines_schedules (
    vaccine_schedule_id INT AUTO_INCREMENT, -- Automatically generated ID for each entry
    vaccine_id INT,
    vaccine_rounds FLOAT, -- how many aplications are needed for immunization
    vaccine_target_population VARCHAR(255), -- target population for the vaccine
    vaccine_age_administration VARCHAR (50), -- age for administration
    vaccine_age_administration_unit VARCHAR(50),
    country_id INT,
    PRIMARY KEY (vaccine_schedule_id),
    FOREIGN KEY(country_id) REFERENCES countries(country_id),
    FOREIGN KEY(vaccine_id) REFERENCES vaccines(vaccine_id)
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
SELECT * FROM countries;
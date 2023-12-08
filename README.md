# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


Markus Indeck, Luke Albinger, Olivia Jacob, Austin Omala

# Project Overview
This app is designed to manage information of members, equipment, trainers, nutritionists, workoutplans, and more for gym managers. An app was created via AppSmith.

# Youtube link -------->  https://youtu.be/K_Lvu9nbN0g

# Database Design
The db/ folder generates a MYSQL database within a MYSQL container.
database diagram: <img width="715" alt="Screenshot 2023-12-07 at 5 28 07 PM" src="https://github.com/mindeck/23f-project-boilerplate-fittech/assets/152943305/1784dfc4-b933-4311-a0e1-9202ddb7c88a">

# 0x14. MySQL

This project involves setting up MySQL replication between two servers (primary and replica) and creating a backup strategy to ensure the safety and redundancy of your MySQL databases.

## Table of Contents

- [Project Overview](#project-overview)
- [Tasks](#tasks)
  - [Task 0: Install MySQL](#task-0-install-mysql)
  - [Task 1: Create MySQL User](#task-1-create-mysql-user)
  - [Task 2: Set Up Primary Database](#task-2-set-up-primary-database)
  - [Task 3: Create Replica User](#task-3-create-replica-user)
  - [Task 4: MySQL Replication](#task-4-mysql-replication)
  - [Task 5: MySQL Backup Script](#task-5-mysql-backup-script)

## Project Overview

The goal of this project is to configure a MySQL primary-replica setup, ensuring redundancy and improved load distribution. It also includes setting up a robust database backup strategy to safeguard your data in the event of unforeseen circumstances.


## Project Tasks

| File Name                    | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| 0-mysql_configuration_primary | MySQL configuration for the primary server      |
| 0-mysql_configuration_replica | MySQL configuration for the replica server      |
| 1-mysql_user                   | Script to create a MySQL user                  |
| 2-mysql_privileges             | Script to grant user privileges                |
| 3-mysql_primary_replica      | Script to configure primary-replica setup     |
| 4-mysql_backup               | Script to create a MySQL backup                |
| 5-mysql_backup               | Bash script to generate MySQL dump and compress |


## Project Structure

#### `Task 0`: Install MySQL 

- Install MySQL on the designated servers and ensure MySQL 5.7.x is used.

#### `Task 1`: Create MySQL User

- Create a MySQL user on both servers, granting privileges to check the primary/replica status.

#### `Task 2`: Set Up Primary Database

- Create a database with tables on the primary server for replication.

#### `Task 3`: Create Replica User

- Create a new user for the replica server with the necessary replication permissions.

#### `Task 4`: MySQL Replication

- Set up MySQL replication between the primary and replica servers, providing configurations for both.

#### `Task 5`: MySQL Backup Script

- Create a Bash script to generate MySQL dumps, compress them, and store them with a specific naming convention.


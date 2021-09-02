## Description
This project purpose for get data issue from jira api.

## Installation
- install python 3 in your machine
- install pip in your machine `python3 get-pip.py`
- add python package jira `pip3 install jira`
- add python package dotenv `pip3 install python-dotenv`

## How to run and configuration
- Copy or rename .env-example to .env
- make sure you fill the all variable
- For email that the email you login in to attlasian / jira
- for the token you can create in this page https://id.atlassian.com/manage-profile/security/api-tokens
- for the project key you can find in the board you have in the jira. for example = ID, UN, IDEA or anything you have.
- run the script with this command `python3 search-issues.py "ASSIGNEE NAME"`
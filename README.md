# Backendapp

Backend Technology

The backend technology uses the Python Flask framework 

The Flask_restx Api import allows for the creation of REST endpoints and the documentation of these endpoints in the Swagger tool.

REST endpoints in the backend contain models for the JSON structure that is expected from the React frontend or returned from the service layer

The backend also uses CORS (Cross-origin Resource Sharing) to allow the framework to interact with the React frontend.

SQL commands on the database are executed using SQLAlchemy



Data Management

Data is stored in a MySQL relational database hosted on the Azure platform

By using a digital certificate, the flask application is connected with our stored data and is updated depending on front-end requests.

Data within the database is accessed using SQLAlchemy in the service layer of our Flask framework.

Data management and schema maintenance are done through MySQL Workbench and DBeaver.


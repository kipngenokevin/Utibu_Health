# Utibu Health Shortlisting Assignment

## Brief
Utibu health is a health facility that caters for patients with chronic conditions such as HIV, diabetes and hypertension. Stable patients can be given medication to last several months without having to return for a doctor’s visit. They can also refill their prescriptions at the pharmacy without having to see a doctor. The pharmacist at Utibu health has an inventory system that manages the stock of medication items, customer orders, sales, invoices and payments. It runs on Microsoft SQL Server and on a legacy desktop application developed in Delphi.

The pharmacist wishes that their clients are able to make orders for their medication remotely from a mobile app and if an order is successful, based on the level of stock in the pharmacy in the current database, indicate to the client that it has been confirmed. Then the client visits the health facility to pick their medication or can have the medication sent to them. The client may pay immediately or choose to pay later at the point of collection/receipt of their medication.

You are required to devise a solution that comprises a mobile app that allows a registered customer of Utibu health to make orders for their medication and check their statement. 

The pharmacist wants to maintain the legacy database and system for face-to-face sales and have the online orders appear in that database as well. There is reliable internet in the health facility but it does not have a public IP address. You are free to use any approach, technology or tools so long as orders are eventually saved in the legacy database.

## Solution
Images Showing solution
**Running the console**
![Running the console locally](https://github.com/kipngenokevin/Utibu_Health/blob/master/images/Screenshot%202024-03-27%20at%2011.24.17.png)


**Running the API**
![Running the API](https://github.com/kipngenokevin/Utibu_Health/blob/master/images/Screenshot%202024-03-27%20at%2011.33.13.png)


**Status of the API**
![Status of API](https://github.com/kipngenokevin/Utibu_Health/blob/master/images/Screenshot%202024-03-27%20at%2011.33.26.png)


**Testing Records from the API**
![Records from API](https://github.com/kipngenokevin/Utibu_Health/blob/master/images/Screenshot%202024-03-27%20at%2011.33.56.png)


**Here is a short brief on the approach to the problem**:
* Build an API that communicates between the mobile app and the Legacy Desktop App
* The scope of this project will be to provide medication records to the mobile app

**Note** 
* Due to the time constraints, this project will **not** focus on processing patient data, neither processing of orders. The solution is only to update the medication records available in the legacy database to the mobile app.
* The goal of this project is to provide an endpoint API that can be called within the mobile app.
* This project will be tested using locally available MySql database.

### Technologies Used
Here is a list of the technologies used and how they are implemented
* **Python** - *Primary language*
* **Flask** - Web FrameWork*
* **SqlAlchemy** - *ORM*
* **JSON**

### Project Design
The solution API uses the following classes and methods to process inputs and outputs.
#### BaseModel Class 
This is the primary class that is inherited by all other classes.

It has the following attributes:
* ___id___ - primary key
* ___created_at___
* ___updated_at___

#### Medication-Records Class
This is a class that inherits from the BaseModel class.

It has the following attributes:
* ___item_name___
* ___item_category___
* ___item_count___

## Authors
* [Kevin Kipngeno](https://www.linkedin.com/in/kipngenokevin254/)

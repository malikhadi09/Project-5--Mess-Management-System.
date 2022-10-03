# Project-6--Mess-Management-System.
Mess Management System, using database.



# PROJECT TITLE:  MESS MANAGEMENT SYSTEM

# ABSTRACT:

Database management systems have become vital for organizations to manage large databases and to perform transactions upon such large data. These database applications not only store data, but also manage them, synchronize them, and help in information retrieval without errors. They reduce manual efforts and enhance the quality of information retrieval services. Due to this reason, they are widely used in almost all sectors.
Mess is a popular place where there is different food to eat, and their prices are written with a particular food. The owner of the mess keeps track of foods that has been sell and foods that are remaining. Owner may sign up for the application where he login and have all the control of the mess management system, he can insert, fetch, delete, update, fetch minimum price food and maximum price food.

# OBJECTIVES:
•	To create a functional application with a user-friendly interface dedicated to performing operations related to a mess management system.
•	To connect that application to a SQL Server Database for it to store data entered by the user.
•	To apply the concepts learned in the Database Systems course

# PROJECT BREAKDOWN:


![11](https://user-images.githubusercontent.com/92660593/193563539-5af3b983-34d4-4cb7-9e05-4c0597afbb75.PNG)


# PROJECT DESCRIPTION:

Our project is divided into two elements. Back End and Front End

# 1. Front End: 

The front end of the project has been programmed on the python programming language, where we have used Tkinter as a library. We have added library of tkinter on python using from tkinter import*. And we used different commands on it to produce a front end.
 There exist a windows form that provides a huge number of options to create a presentable interface. There are total 5 forms in our project discussed above. And each form consists of insert, delete, update, fetch functions. And for Desi foods, Fast food, Dessert consists of 2 extra functions. That is min price and max price function.
2. Back End:

# •	Working:

We are making Mess Management System where we are using MySQL. We made this project on Python. We have four functions, and all those functions are made in one class named “DBHELPER” I have used object-oriented programming here. Functions that we created in our project are given below, and these all functions are in all the tables. Except delivery and owner details they don’t have max price and min price function. Insertion, deletion, updating, fetching, max price, min price.
We created database named “mess” in MySQL and then afterwards we connected MySQL server with python using MySQL. Connector. Then we created two tables in python that are described in description one table is “DESI FOODS”,“FAST FOODS”,’’DESSERT’’,
’’OWNERDETAILS’’,DELIVERYDETAILS’’.
# •	Insertion function:
In insertion function we are inserting the data of different columns. and after we entered the data, and it will be added in particular database. 
# •	Fetching function:
In Fetching function, we are fetching the data already present in the database. We have created fetching functions for all tables.
# •	Deletion Function:
If we want a particular that to be deleted from the data base, we can also do that. I have created function that would delete any data from the data base that the owner wants to. We have created fetching functions for all tables.
# •	Updating data function:
If we want to update a particular data, owner has entered wrong data in the database we can simple update that and for that we have created updating data function. We have created fetching functions for all tables. 


# MAX PRICE / MIN PRICE FUNCTION:
We used this function in FAST FOOD, DESI FOOD and DESSERT where the owner can get the max price food and min price. 
 
# Methodology:

•	The username and password are already saved in the database, by entering that in login form if the username and password matches the next form will be opened successfully. If not, it displays an error message.

![image](https://user-images.githubusercontent.com/92660593/193563333-d8db3723-a5d6-40e2-88a5-9fc22c787f97.png)

•	Upon the login being successful, the user will be directed to the main menu of the application where they will be given multiple options which include menus of Fast food,  Desi food, Dessert, Owner Details, Delivery Details.
 
 ![image](https://user-images.githubusercontent.com/92660593/193563369-a9e10185-790d-4b99-8d2b-11948e19b5fa.png)


# DESI FOODS:

•	The first buttons will have all details regarding desi foods available. Where the owner can insert, delete, update, fetch all the data. He can also get the max price and min price foods.
 
![image](https://user-images.githubusercontent.com/92660593/193563395-ef3fc5ed-dc65-44f3-ab9f-c2b6330abe36.png)
 

# FAST FOODS:
•	The second buttons will have all details regarding fast foods available. Where the owner can insert, delete, update, fetch all the data. He can also get the max price and min price foods.

![image](https://user-images.githubusercontent.com/92660593/193563407-b8b10e50-8b80-4e9d-84e3-b5b1bc2109ec.png)


# DESSERT:
•	The third buttons will have all details regarding desserts available. Where the owner can insert, delete, update, fetch all the data. He can also get the max price and min price desserts. 
 
![image](https://user-images.githubusercontent.com/92660593/193563432-de4812d9-ce62-4010-af4a-1a701c919680.png)





# OWNER DETAILS:
•	The fourth buttons will have all details regarding owners of mess management system. Where the owner can insert, delete, update, fetch all the data. 

![image](https://user-images.githubusercontent.com/92660593/193563456-7049f9ee-fa94-4121-aa27-bde6e6f2d270.png)


# DELIVERY DETAILS:
•	The fifth buttons will have all details regarding riders available. Where the owner can insert, delete, update, fetch all the data. 

 ![image](https://user-images.githubusercontent.com/92660593/193563474-88c8f7de-dec9-47b2-bb98-853324dc3224.png)


# CONCLUSION:
We were successful in creating a database application with all functionalities related to a mess management system. The owner can only login to the application, and he can perform multiple operations efficiently which include insertion, deletion, updating, fetching. 





























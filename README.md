# Fundamental Project

## Resources

**Presentation:** https://docs.google.com/presentation/d/1RqRxEf90R1PpkNKtaCyQBBos2Q0X5ucNnLt1nxIvnM4/edit?usp=sharing

**Trello:** https://trello.com/b/0zckZt2W/crud-system

**Website:** http://35.246.125.90:5000/

## Content Page
* Brief
* Tools
* Project Planning
* Entity Relationship Diagram
* CI/CD Pipeline
* Risk Assessment
* Testing
* Application Design
* Improvements
* Issues

## Brief
I have been tasked to create an application that can Create, Read, Update and Delete data from the database while using agile working method on this project. Using skills and knowledge I have learnt over the last few weeks to assist me in creating this project.

## Tools
The software and languages chosen for this project are listed below.

*Trello
*Database
*Flask
*Git
*Pytest
*Jenkins
*Gunicorn

Trello is used to keep track of the project's progress. What task should be done on the day and what is left to be done.

Database will be hosted on GCP (Google Cloud Platform) where all my data for this project being stored.

Flask is used create front end website of the application using Python, this will be main way for the users to communicate with the application as well as reading, creating, updating and deleting data on the database.

Git and Github is used to version control and the ability to work on the project from different machines. All the changes to the application will be recorded and noted on the time of the changes and the content that is changed too.

Unit testing with Pytest; sets out a range of tasks for the app and provide what should happen when the app runs the test. It tests makes sure that each section of the code runs correctly and pytest returns the coverage of the test ran which indicates which part of the code is tested and which has not.

Jenkins used to automate the running of the app. Providing the git repository  and the correct shell commands, the app can be built, tested, and deployed.

Gunicorn is used to test run the app in a production environment where multiple users can access the app.

## Project Planning
For Project planning and tracking, Trello was used for this task as free, simple, and portable with their mobile version of Trello. The Trello board features a range of blocks which holds information of the current progress of the development for this project. As well as the planned, doing and testing; there are links to the Git Hub repository, Risk Assessment and User cases.

[Trello Board](https://trello.com/b/0zckZt2W/crud-system)

Trello Board can be accessed with the link above and inside the Trello Board you can find: 

**Resources** - This section contains links to Git Hub Repo and Risk Assessment making easy access to files and all the elements can be found in the Trello.

**User Stories** - This section contains what the Users would want to do on the application set out for this project. 

**Product Tasks** - This section contains all the tasks that still need to be done and currently on the waiting list. 

**Doing** - This section is where the tasks are currently doing and not yet finished 

**Done** - This section is where the tasks are completed and tested. It is working as intended with no bugs. 

**Testing** - This section test runs the code with different tools like Pytest and Gunicorn where the application is running in a production environment and testing the application fully line by line.

## Entity Relationship Diagram
ERD is created to give a clearer overview of the databases created for this project and the relationship between the tables. While drawing the ERD, it is easier to identify any problems between tables and resolve them before creating the database as mending ERD is easier than mending databases. During this project there are two versions of the ERD:

**Old**

The old version of the ERD shows only 2 tables but this is a many to many relationship therefore it needs a child table in between the 2 tables to provide a better data structure where it can hold data from 2 different tables.

![OldERD](https://i.imgur.com/L7O2lQz.png)

**New**

This is the new version of the ERD where the 2 tables is joint by 1 child tables changing many to many to two set of one to many relationship table.

![NewERD](https://i.imgur.com/8kA33Wt.png)

## CI/CD Pipeline
![CICDPipeline](https://i.imgur.com/SE8vRR6.png)

This diagram shows the usage of the CI/CD Pipeline. It shows the continuous integration pipeline used in this project, the tools that is used to create the application and the software used to host database and how all the tools are connected together and performing unique tasks in this project.

By using continuous integration development method, it enables the development team to detect problems early and resolve them as soon as possible. Jenkins will pull from the repository when something new is pushed into the repository and begin the installation of the new application onto the cloud VM. Which then it will begin to run tests automatically and save the test report into a file which later can be viewed.

## Risk Assessment
![RiskAssessment](https://i.imgur.com/02NSvDo.png) 

This is the risk assessment done before the development of the app, identifying the risks while developing the app. After the development of the app, the risk assessment is revisited to update any risk that might need an update on the risks or mitigation.

![RiskAssessmentUpdate](https://i.imgur.com/Rv9XBbn.png) 

This is the risk assessment after the development of the app, where the risks are revisited and reassessed to see how likely or the effect of the listed risk could have effect on the app Risk Assessment

## Testing
Unit testing is performed to check a small section of code within the app by using Pytest, a coverage report can be produced as well as which line of code is missing and has yet been tested.

![Coverage Report](https://i.imgur.com/NP007tZ.png)

Jenkins is used to perform testing but in a automated way.

![Jenkins Testing](https://i.imgur.com/hjg0w8h.png) 

Production environment testing is performed by using Gunicorn, this is allowing a better understand how the app would function when placed in an environment where multiple users can access it.

![Gunicorn Testing](https://i.imgur.com/sdQw0qd.png)

Integration Testing is performed to simulates the forms on the web app being clicked on, compared to Unit testing where it is based on the HTTP response integration testing completes a set of action which this test submits a form to add a stock onto the database and where it should take the user after completing the form.

## Application Design

This project is really HTML and the functionality aspect heavy where no CSS is included. This app allows the users to Create, Read, Update and Delete data from a database hosted by Google Cloud Platform. This app is based on a stock and order model where users can check what stocks does the store have and check when orders are made.

**Home Page**

![HomePage](https://i.imgur.com/DRHqxSg.png)

From the start, users will be greeted by the homepage of the app, where the users can see all the current stocks the store has. Information like the Name, Price, how many in the store and what type of product it is. On the navigation bar is where you can swap between the stock or the order side of the app. Addition can be made by clicking Add a stock and while on the order side, users will see Add a Order instead.

**Add Stock** 

![AddStock](https://i.imgur.com/BXKwJDb.png)

From here, users can create data entries and submit it onto the database. It will redirect you back into the homepage after adding.

**Update Stock** 

![UpdateStock](https://i.imgur.com/gNv8q7k.png) 

![UpdateStockAfter](https://i.imgur.com/YRjUMmL.png)

Update function allows the user to amend information about the stock they added, this could be the name change or the price change. From the screenshots, the first data item's name got changed.

**Delete Stock** 

![DeleteStock](https://i.imgur.com/wM5yDQE.png)

The delete function  removes a data entry from the database.

**Order** 

![OrderPage](https://i.imgur.com/gVsKCOS.png) 

This page displays all the current orders on the populated on the database. Similarly, to the stock section, there's also a **Add**, **Update** and **Delete** function built in.

**Order Update** 

![UpdateOrder](https://i.imgur.com/eOnNSVr.png) 

On the order update page, users can change the date and choose stocks to append but the function has yet fully implemented.

## Improvements
There are many ways for this app to improve on the functionality side as well as the visual side with CSS.

* As mentioned in the Application Design section above, in the update order section the append stock into orders is not fully implemented and that should added onto the app so users can track which order has order which stock.

*There are no login system which prevent unauthorised users from accessing and make changes to the database.

* Include CSS to make the app more user friendly and greater consistency in design.

## Issues
There are bugs that could affect the users experience when using this app:

* When the data insert incorrectly or missing information, there are no error messages to prevent that from happening. However, the name column does prevent the same stock name to be added.

* The add stock to order list is there but not fully functioning as it should.

## Author
Vincent Lin

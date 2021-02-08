# Pet App

## Brief
The aim of this project was to primarily create a CRUD application. CRUD represents an application with create, read, update and delete functionality. In order to do so, the following supporting tools, methods and automation covered in the core modules during the first 6 weeks of the bootcamp was taken into consideration:
*	A Kanban Board from Trillo
*	Project Management
*	Python Testing
*	Git
*	Basic Linex
*	Python Web Development
*	Continuous Integration
*	Cloud Fundamentals
*	Databases

## Project Outline
My project is based on a relational database where an individual is able to choose the pet they would like. In this case, an individual can have many pets and a pet cannot have more than one owner hypothetically speaking which represents the one-to-many relationship required for this project.

## ER Diagram
An ERD (entity-relationship diagram) can be used to represent two or more tables within a single database. The database was created using the create.py and models.py python files which were in a MySQL server on Google Cloud Platform server which I then accessed on an Ubuntu Virtualbox. As we had studied Flask, it made sense to work with Flask’s framework, an API of python, I also used MySQL in Flask with the installation of the Flask-MySQL package. This made accessing and making changes to the database tables from the front-end helpful.

![Database ER diagram](https://user-images.githubusercontent.com/77278616/107169912-ef9de980-69b6-11eb-9345-a35766601b10.jpeg)

It can be seen as above, there are two tables labelled Owner and Pet. Person table includes Person ID and name where person ID is the primary key and the pet table includes pet's name, person and person's ID where pet ID is the primary key and person's ID is the foreign key.

## CI (continuous integration) pipeline

![CI pipeline](https://user-images.githubusercontent.com/77278616/107168773-2b837f80-69b4-11eb-884c-c8e79672c29d.JPG)

The diagram above illustrates the (CI) pipeline diagram involving the various tools needs in order to deploy a web application. It begins with source control which can be used to push or pull to a VSC system which was Git in my case. This can then be used to complete or fetch work in project tracking. The CI server which is Jenkins is at the center of the CI pipeline which can pull code from VSC and poll code to VSC. Python can be used to build code but, in this project, this is not applied so we complete automated testing in Python. Python then sends back the report to Jenkins either saying whether the code has passed or failed. In the case of the code failing, this would be sent to the developer who can then work on the source code. Any code built will be produced as artifacts repository which can be utilized at a later stage for integration testing which also doesn’t apply to the project undertaken.

## Project Management
Link to Kanban Board providing more information on how I went about the process of Project Management: https://trello.com/b/4eHQG4Ov/pet-app-kanban-board#

## Risk Assessment

![Risk Assessment](https://user-images.githubusercontent.com/77278616/107166108-ea3ba180-69ac-11eb-94d7-49f8101f89d2.JPG)

## Testing

Pytest was used to test the coverage of the flask application with the use of unit testing. The aim was to get 70-85% and I was able to get a coverage of 92% showing the python functionality was working which is required before the deployment of the web application.

Unfortunately my Jenkins job failed due to the a problem I was facing with my VirtualBox which I was unable to fix.

![pytest application](https://user-images.githubusercontent.com/77278616/107165882-3df9bb00-69ac-11eb-857f-cf026be5d0e1.JPG)

## Problems
My idea initially was to make a recipe app where users were able to add, edit and delete their reviews but also preview recipes with cook enthusiasts being able to add, edit and delete their recipes. However, I quickly realized this was out of my depth considering how soon the deadline was after learning and applying the concepts. I therefore changed to my pet idea which was a lot simpler and I had confidence it would pass the tests during the testing stage due to its simplicity.

Furthermore, during the first three weeks of the assignment, I was working on GCP however after the installation of SQLAlchemy, the virtual instance was incredibly slow and often froze. We also were unable to install Jenkins due to the limited capacity of the VM on GCP. This was quickly resolved with the installation of the Ubuntu Virtualbox however it took some time to get used to the interface. Functions such as copy and paste was not a default setting therefore, I changed this to do so, I also had some scaling issues which made the interface look unpleasant.

I had a major issue with running SQLAlchemy on VirtualBox which resulted in my Jenkins job failing. This meant I couldn’t test my dummy data and my localhost also wasn’t functioning properly due to this operational SQLAlchemy error.

## Possible Improvements
As this was my first project utilizing Flask, MySQL, Python, etc, I wasn’t confident in being creative in my idea. In order to gain more out of the project, next time I would add some more attributes such as pet breed, location, etc. I also had no login or password which means that anyone can assess the database so an improvement I would be considering adding username and password.

## Contributors
Subeca Kirupananthan

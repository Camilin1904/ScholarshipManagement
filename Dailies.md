Sup, it's Andrés Camilo Romero Ruiz, leader of the group, and i'm here to leave a message:

Before starting the dailies I've been working in parallel on the following to advance the development of the project:

HTML and CSS development, I have advanced in the implementation of the page:
* Home from the admin view, functionalities still need to be assigned but the CSS part it's probably fully designed.
* Login, is fully designed but i've been working on features
* Signin, it is fully designed and functional. However I think it will be discarded during the project
* Search, is partially designed and has no functionality

Icon Selection: create the icons folder and add the ones I have used so far in the CSS

Django: I have been working on ways like creating user, login, filter, enumerations for calls and I have been working on data modeling for users

All of this work will be uploaded in the daily files as a zip, since they're outdated for the actual branches, but they're going to be used and might be uploaded latter in commits with different names ;D

# Dailies:

## 19/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar    | I set up the project environment and created the branch on which I will work on user story 4   | I will start the development of user story 4 by creating a base view in HTML for the creation of announcements and an initial table model for the data that will be stored in the database   | No |
| Camilo Carmona Valencia | I set up one of the branches I will be using | I will start development in US1 by setting up the data base table for scholarships | No |
|Andrés Camilo Romero | I work on HTML, CSS and forms for functionalities in general, they can be seen in the zip file |I will set up the project enviroment and created the branch on which I will work on user story 15, also I'll bring the HTML, CSS and python code that i've been working for the login and signin functionalities before the dailies started, that includes forms and working on setting the data base table for users | No |
| Juan Sebastián Libreros | I set up the project environment and created the branch on which I will work on user story 13 | I will start the development of user story 13 by creating a base view in HTML for the search of applicants and start the function of change states of the applicant to "Beneficiary" if accepted or "Not accepted" if it is discard | No |
| Brayan Steven Ortega | I set up the project environment and created one of the branches I will be using to work on user story 11 | I will start the development of user story 11 by creating a base view in HTML for the creation/addition of a applicant | No |


## 20/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar    | I created the base template of the "announcement creation" view and the base form that will be used in this view   | I will include the "announcement creation" view in the page and link it in the header | No |
| Andrés Camilo Romero | I set up the HTML, CSS and python code for login and signin functionalities | I will look if cookies are needed for the logout and mantaining a state in the app or if I need some sort of new table in the data base, probably I will ask Domi about this next monday because of exams| No |
| Camilo Carmona Valencia | I created the table for donors in the data base | I will link scholarships with donors and develop the new creation process | No |
| Brayan Steven Ortega | I created the table for applicants and start the base view in HTML for the creation/adition of a applicant | I will continue creating the base view and i will link it with the home page  | No |
| Juan Sebastián Libreros | I did some research to create the base view in HTML of the change of satet of the applicants. I couldn't do much because I got sick and due to tomorrow's exam | I will start creating a template for the base view of the applicants management| No |


## 21/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar |  I made the "announcement creation" view visible on the page and included the link in the base view  | I will extend the information requested in the form displayed in the "announcement creation" view | No |
| Camilo Carmona Valencia | I was unable to link the tables because of my academic situation | I will link the tables | Partial exams |
| Andrés Camilo Romero | I discover that probably it would be better if I use the integrated parts of django since it contains methods to authenticate the users and group them based on the permissions they have | I will keep on searching on how to use them with my own user class or if it's needed to inherit them from the user class that django offers | Python documentation is kind of confusing compare to java so I will try and search in other sites about it. And also exams |
| Juan Sebastián Libreros | unfortunately my disease got worse and I wasn't able to work properly, even though I solved a git problem and understood more about how the python django framework works for making the modify function of my User Story. Also I pushed my branch into the repository | I will do my best to create the and advance on my duty of making the function of modify state | I'm sick, but it's a minor issue|
| Brayan Steven Ortega | I was unable to continue creating the base view | I will link the base view of the creation/addition of an applicant with the home page | Partial exams |


## 22/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I created a new table for the database linked to the announcement table and investigated about the Django databases | I will continue to investigate about the databases in Django | I have to learn more about Django databases before I continue with "US4" |
| Andrés Camilo Romero Ruiz | I found a two hour video that explains how to use django authentication and user management | I'm looking to see the video so I can improve the login functionality and make the logout | My laptop charger is dying and a new one comes on monday so let's hope the best |
| Camilo Carmona Valencia | I added the relationship between table Scholarship and table donors, errors unfixed | I will delete the values previously present on the table scholarships to make migrations and test the link | No |
| Brayan Steven Ortega | I fixed some variables for the table of the database and link the base view of creation/addition of an applicant with the base page | I will investigate about HTML and how improve the implementation and the relation between the code with the HTML | I need to learn more about HTML |
| Juan Sebastián Libreros | I created the module for the applicant management function, also fixed my venv and started to link the main app with my module | I will link the app and start with a simple function to test the functionality before a base view | No, I got better |

## 25/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
|Juan Sebastián Libreros | I created the model of an applicant on my app and tried to connect the main home with my module but I failed. However the team decided move the project to the ScholarshipModule class so I did just minor changes to facilitate the change of on app to another. | I will learn about Bootstrap because all the team decided to migrate to this library and also move my project to the main one | I need to do a synchronous work with my partner in charge of stories 11 and 12 because I depend on his database .| 
| Camilo Carmona Valencia | I Upgraded the user interface of the create scholarship screen, this includes creating a template for other screens to use, I also created a test class for the scholarships table | I will expand my testing classes, while also making the ui better and more consistent with what was planned, I will also begin to work on US2 as all the logic behind US1 is done and we may be migrating from css to bootstrap | A possible bootstrap migration may mean remaking the user interface for the scholarship creation screen, other than that, no |
| Andrés Camilo Romero Ruiz| I finished US15 and US16, more details about this can be seen in the last commit of US15 branch | I will make both pull request for merge with the dev branch, I'll start looking at a bootstrap migration on the views that I already work with to decide about it | I will have to see another tutorial, but now for bootstrap, I'm thinking that I might not have time until weekend |
| Juan Camilo Salazar | I watched a couple of videos about databases in Django, so now I can continue with US4|I will finish the necessary tables for US4 and add a unit test case for the announcement creation | No |
| Brayan Steven Ortega | I created multiple applicants in the databases and also i created the basic pages in html to complete the US11, finally i had to fix some variables for the table of the database again to create the applicant without problems | I will upgrade interface of the create applicant screen and the applicant home page | No |

## 26/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
|Juan Camilo Salazar | I created four new tables for US4 and a single test to verify that an announcement is created correctly| I will finish the functionalities of the announcement creation page | No| 
|Juan Sebastián Libreros | I integrated my module on the main module, also created a pseudo searcher to test queries to finally create my function | I will test the queries to create the function of my module and also integrate Bootstrap on my module if possible | No |
| Camilo Carmona Valencia | I made the ui consistent with what was planned, while also modifying the form for scholarships so that it is more convenient | I will begin to work on US2, as for the ui, I will begin my migration at a latter date | No |
| Andrés Camilo Romero Ruiz| I started the bootstrap migration on the views that I already work with and learning about it | I must continue the migration and help Brayan with a home page that he needs | No |
| Brayan Steven Ortega | I did merge with dev and Andrés help me to start the creation of the user interface view of the home page for the financial staff | I will continue doing the user interface for the home page for the financial staff and also working in the page of applicant creation | No |

## 27/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
|Juan Camilo Salazar | I added all the fields needed in the "announcement creation" page | I will solve an error in the "announcement creation" page so all elements can be saved correctly | No| 
|Juan Sebastián Libreros | I added an basic search of applicants to prove my status change function of an specific applicant. Also fixed some errors on applicant's model | Integrate the creation of applicants to my module and test it to then do a basic status change on specific applicants | No |
|Brayan Steven Ortega | I finished the home page for the financial staff view to access all its features and I started the interface view of addition/creation of an applicant and also fixed some errors on the datebase adding the status of the applicant | i will finish the interface view of addition/creation of an applicant using the design given by Andres | No |
| Andrés Camilo Romero Ruiz| I worked on bootstrap to see its capabilities and make some home pages to learn how to redirect the user based on the role | After analyzing the situation we have decided as a group to continue working on CSS since it offers more freedom than bootstrap when designing pages, so I am going to look to improve and redesign pages | No |
| Camilo Carmona Valencia | I have begun work on US2 | I will find a way to make the filter query more elegant | My inability to remember of dailies |

## 28/09/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Andrés Camilo Romero Ruiz | I improved the CSS for login and singup pages in the CSS branch | Today I shall finish the CSS for those pages and make the home pages for each role, implement a method that based on the user's role redirects him to the respective home page and make the pull request so I can start my last user story| No |
|Juan Camilo Salazar| I did solve the error that interfered with the announcement save in the database and started working on the "new announcement" functionality | I will finish the "new announcement" functionality so the design of a page is the only thing left to complete US4| No |
|Brayan Steven Ortega | I researched about CSS and HTML to continue advancing on the Applicant creation page | I will continua improving the CSS of the Applicant creation page to end the US11 | No |
| Camilo Carmona Valencia | I made no further advancements on US2, rather, I made a little change to US1, as I added an enumeration for the scholarship type, though I did not link it | I will finish what I started yesterday and link the two, making the changes I see fit, as for US2, I hope to be able to begin to properly work on it | No |
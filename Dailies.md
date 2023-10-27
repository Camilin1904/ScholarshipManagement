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
|Juan Sebastián Libreros | I added the applicant screen to visualize the information easier to test the change of function. Also integrated the US11 to my branch to test it and integrated with my user story | I will do and test the changer of status function also investigate on how to pass information from one screen to another in HTML | No | 

## 29/09/2023
| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I Finished polishing the input method for the type of scholarship | As all that is left in US1 is ui, I will begin to work on the logic of US2 | No|
| Juan Camilo Salazar| I finished all of US4 functionalities so page design it's the only thing left | I will start the design of the "announcement creation" page using CSS | I have to learn about CSS|
| Andrés Camilo Romero Ruiz |  I finished the CSS improve and make the pull request so my team has templates to work with | I'm not going to work today, feel like it's enough, but on the weekend I hope to start and finish the last US that I have assigned | No |
| Brayan Steven Ortega |  I founded a new funcionality to implement in the creation of an Applicant and I continue improving the CSS | I will finish the CSS first and then implement the new functionality | No |
| Juan Sebastián Libreros | I found a little problem on my US and I got to do a new functonality expanding the previous one and its editing the whole applicant | I will create the function of edit an applicant also, learn the proper way to do it and focus on HTML and CSS | I need to learn how to edit a table on django |

## 02/10/2023
| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I investigated about CSS and how to properly place the items on the page | I will organize and style the announcement creation page with CSS | No|
| Andrés Camilo Romero Ruiz | I started and almost finished user story 10 on assigning user roles, all the front is done and I still have a part of the backend pending, its progress can be seen in the US10 branch | Today, with what I have seen during class, I hope to finish the user story and make a pull request. In this way, I will have finished all the user stories that concern me functionally. I will remain attentive to what my classmates need. | No |
| Camilo Carmona Valencia | I Finalized the update of the ui of US1, while also finalizing the ui for US2 | I will further improve US2 | No |
|Juan Sebastián Libreros | I created the css for an early search applicant screen. Also investigated about how the queryset function on django. Finally I solved some doubts about my user story | I will learn how sessions work to create a proper edition of applicant | No |
|Brayan Steven Ortega | I ended the css for the US11 and I fixed some errors in a table in the database to finally made the pull request to dev with all the functionalities of US11 | I will start working on the US12 | No |

## 03/10/2023
| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I finished the front-end part of US4 | I will add alerts to the announcement creation page so US4 is done | No|
| Andrés Camilo Romero Ruiz | I finish user story 10 about role assigns and made the pull request so my stories are done | I shall review Brayan's pull request to dev | No |
| Camilo Carmona Valencia | I made the type filters stay when applied | I will work on test for both of my user stories | No |
| Brayan Steven Ortega | I started researching the queries and filtering necessary to start the US12 | I will continue researching the information necessary to start the US12  | No |
| Juan Sebastián Libreros | I finally got the necessary to create the edit function of my User Story. I added an functional version of a search function | I will make the edit screen work and prepare the necessary to start my next user story | No |

## 04/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Andrés Camilo Romero Ruiz | I reviewed Brayan's pull request to dev | Nothing | I left my laptop charger at the University and i have homework for tomorrow so i'm screwed |
| Camilo Carmona Valencia  | I was preoccupied with other duties | I wil test US1 and make my PR | I...also left my laptop's charger at university, so I'm also screw |
| Juan Camilo Salazar | I finished US4  | I will reformat my code to comply with the codeStyle and I will make the pull request | No, I didn't leave my laptop's charger at the university |
| Juan Sebastián Libreros | I fixed an error on search method. I couldn't do to much due to my academic situation| I will investigate on how sessions work because I am blocked with that function | I need some help with the sessions theme | 
| Brayan Steven Ortega | I founded the form to make the necessary queries to complete the US12 | I will help Salazar to resolve the merge with dev so he can make his PR | No, I checked that my charger was in my backpack | 

## 05/10/2023

Hello, the whole team decided that today we aren't able to make our daily. This is because of mutiple reasons but the most important was an exam that drain all of our time and energy. We hope you understand our situation.
Good morning, good evening and good night.

![](https://cdn.discordapp.com/attachments/696493127246151731/1159689294236090509/Gatito.webp?ex=6531efd1&is=651f7ad1&hm=30a0a27d77da7da87005ed6f3428a9e139428eaecf265ef15e5ecbf897c22eac&)

## 06/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I couldn't work yesterday| I will create a new branch and start working on a new user story (US5) |No|
| Andrés Camilo Romero Ruiz | Nothing | Today I hope to help Brayan with the CSS of US-12 and Sebastian with a question about sending data between screens to allow editing of an object that has been selected from a list | No |
| Juan Sebastián Libreros | I couldn't work yesterday | I will recieve the help of Andrés Camilo to fix the sessions problem I got |No|
| Brayan Steven Ortega | Nothing | I will create the US12 branch and start to make the page of filter an applicant with the necessary input |No|

## 07/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I successfully merged branch US1 with new developments on dev so that i may be able to do my PR | I will continue work on US2 do that I may also make a pull request from that | Forgetting to do my daily does not help me, other than that no. |
| Juan Sebastián Libreros | I fixed the problems i got with sessions thanks to Andres Camilo's help | I will finish my edit function and then start with my secons user story. I got to coordinate to create the search applicant part with Brayan. I'm close to do my PR | No |
| Andrés Camilo Romero Ruiz | I did the CSS that brayan asked my to do and fixed with Sebastian the problem | I will work on notifications for the role assign function and look for ways improves on my user stories | No |
| Brayan Steven Ortega | I did the US12 branch and started to create the page in HTML with the CSS that Andrés made | I will work on querys to filter the search of a student and I will show on the page the list of students in the database | No |

## 08/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I was unable to proceed any further as I am a Class assistant (monitor) and was grading | I will finish US2 | No |
| Juan Camilo Salazar| I set up the new branch and files needed for US5| I will make the new form (that includes the search filters) and the table that will display the search results | No |

## 09/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I made the announcement search page and displayed all the registered announcements in the table | I will improve the table and start making queries for the search filter | No |
| Andrés Camilo Romero Ruiz | I worked on the notifications branch | I will ask domi about tests for the project and US in backend and frontend | No |

## 10/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Brayan Steven Ortega | I helped Libreros with some final functionalities and I accepted the pull request from Libreros with dev | I will do nothing because I'm getting late to home and I have a quiz tomorrow| No |
| Andrés Camilo Romero Ruiz | I found the next video about testing https://www.youtube.com/watch?v=P_hXyudB8zc | I will do nothing because I'm getting late to home and I have a quiz tomorrow | No |
| Camilo Carmona Valencia | I have successfully made my filters work as intended, while also fixing how the table of scholarships is viewed in the scholarship screen | I will polish a couple of thing before doing my Pull Request | No |
| Juan Sebastián Libreros García | I made my pull request to dev | I won't be able to work today because of academic stuff and some mechanical problems with my car | No |

## 11/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | Could't work yesterday | I will finish all the announcement search filters so US5 is fully functional | No |
| Andrés Camilo Romero Ruiz | Didn't work yesterday | I will pull and merge the notification that I work with days ago branch with dev and make the pull request | No |
| Camilo Carmona Valencia | I was not able to continue as I have an important assignment tomorrow | I will make my PR in the next few days | No |
| Brayan Steven Ortega | Didn't work yesterday | I will investigate the form to implement the necessary tests in the US11 and US12 branches | No |
| Juan Sebastián Libreros | Didn't work yesterday | I will advance with the las details of my las user story. However I won't be able to work to much because I got an important assigment tomorrow | No |

## 12/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I had an important assignment, therefore I was unable to finish US2 | I will finish US2 | No |
| Juan Camilo Salazar | I created four new search filters for the announcements| I will make the final search filter and start styling the announcement search page with CSS | No |
| Andrés Camilo Romero Ruiz | I made the pull request for the notification branch | I have to make some refactors in the notification branch since some parts of the code are useless| No |
| Brayan Steven Ortega | I researched about tests that I might need to test the US11 and US12 branches | I have to make some reformats in the US11 ans US12 branches to comply with the coding style | No |

## 13/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I added a new search filter, so US5 is now fully functional, and began styling the page with CSS  | I continued styling the page with CSS and linked it to the home page and to the announcement creation page| No |
| Juan Sebastián Libreros | I wasn't able to work because an important assignment | I will connect filter screen with the view of applicant. Almost done with the US17 | Besides forgetting to make my daily, no |
| Brayan Steven Ortega | I started to make the code reformat of the US11 and US12 | I will finish the code reformat of bouth branches to start the implementation of the tests | No |

## 14/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Sebastián Libreros | I connected filter screen with the view of applicant | Fix some issues that presented after connecting the two screens | No |

## 15/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Andrés Camilo Romero Ruiz | Created the test branch where I did a littles test for the user model and rename the tests so they all can be run at the same time | I shall explain brayan how the tests works | No |
| Brayan Steven Ortega | I created the branch Reformat and start to apply the coding style to the US11 and US12 branches, also I helped Libreros to end the the CSS for his user story | I will end the coding style and I will make the tests for the US11 and US12 branches |No |
| Juan Sebastián Libreros García | I fixed some issues that presented after connecting the two screens | I will end my user story and pull request the branch. Also start with tests | No |

## 16/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I finished the front-end part of US5 | I will reformat the code in order to apply the code style and make the pull request| No |
| Camilo Carmona Valencia | I finished US2 and pull requested | I will probably do some tests | Forgetting to do my dailies |
| Juan Sebastián Libreros | I ended my user story and pull request the branch | I will reformat the code | No |


# SECOND SPRINT

## 18/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | Yesterday we started the second sprint | I will make the HTML and CSS base files in order to begin with US6 | No |
| Camilo Carmona Valencia | We started the second sprint | I will do a small refactor as I will separate the views that I use into different archives | No |
| Andrés Camilo Romero Ruiz | The second sprint started | I am going to investigate and test how to generate csv and excel files from python to start with US9 for generating reports | No |
| Juan Sebastián Libreros | The second sprint started | I will refactor the code and separate the new view of the US3 and start my user story | No |
| Brayan Steven Ortega | The second sprint started | I will create the US8 branch to start my user story and I'm going to do a small refactor separating the views that I use | No |

## 19/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar | I started US6 and I created the base files and methods I´ll be needing for this| I will link the announcement edition page from the announcement search page and show the information corresponding to the selected announcement | No |
| Juan Sebastián Libreros | I refactored the code and separated the new view of the US3 and started my user story | I wil create the new view on html to edit and work on US3 | No |
| Andrés Camilo Romero Ruiz | I was capable of creating an excel and csv files with sample values through python | I will search on how to allow the user to select a folder to save de excel and csv that are supposed to be created | No |
| Brayan Steven Ortega | I started the US8 and I separated the views that I use in diferent files | I will create in the data base the tables that I need to complete the US8 | No |
| Camilo Carmona Valencia | I was able to do the small refactors, but didn't have the time to properly connect them | It is my birthday, so noting :) | No |

## 20/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I had other assignments so I couldn't work | I will properly separate my views into different archives | No |
| Andrés Camilo Romero Ruiz | I searched about how to allow the user to select a folder | I shall keep on searching because apparently there's no way to do it with only HTML or JavaScript since it creates vulnerabilities for the user so the browsers stop this to be done, some posts in stack overflow tells that in can be done with help of programming languages as java, so I will keep on looking | No |
| Juan Sebastián Libreros | I created the new view on html to edit and work on US3| I won't be ablo to work beacause of some duties I got to attend | No |
| Juan Camilo Salazar |I linked the announcement edition page and related it with the information of the selected announcement| I will work on displaying the form with the announcement's previous information | No |
| Brayan Steven Ortega | I created in the data base the necessary tables and start the implementation of the status update registration | I will continue make the implementation and the integration with the necessary views already created | No |

## 21/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Camilo Carmona Valencia | I have taken my user story and begun research for pdf generation | I will continue researching | My lack of knowledge and possibly conflicts with a dependency |
| Andrés Camilo Romero Ruiz | Yesterday I could implement a folder chooser but only on pure python, when I try to move it to the Django framework inside a view it stopped working | Today I will keep on searching if I'm doing something wrong or if there's another way out of it | No |
| Brayan Steven Ortega | I implemented the saving of the applicant's status when they are registered in an announcement | Today I will continue working on the implementation of the functionalities for my user story | No |

## 22/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar |I made the information of the selected announcement visible on the edition page| I will make it possible to change the information shown on the edition page | No |

## 23/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Juan Camilo Salazar |I made the base information of an announcement editable| I will investigate dynamic forms in order to create or delete additional events | I need to know more about JavaScript |
| Andrés Camilo Romero Ruiz | I didn't find a way out for the select folder option | I will ask domi about it today so the file can at least appear on download files | No |
| Camilo Carmona Valencia | I Discovered a library to generate a pdf from an html file, unfortunately I have not been able to make images work | I will continue to troubleshoot the pdf generation | My lack of knowledge regarding the use of teh xhtml2pdf library |
| Brayan Steven Ortega | I didn't work yesterday due to other duties | I will continue to the implementations in the US8 and I will start make the corrections in the US11 to improve the applicant creation as discussed in class | No |
| Juan Sebastián Libreros | I finished my user story | I will fix some details on my user story and start a big reformat. Also help my co-workers with their duties if required | No |

## 24/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Andrés Camilo Romero Ruiz | I solved the problem of downloading the csv so now it's sent to the downloads folder | I will learn javascript to implement dynamic search lists so it feels more interactive for the user | No |
| Juan Sebastián Libreros | I fixed some details of my user story | I will reformat and adapt to the new style the team accorded | Besides reading bad the date, no |
| Brayan Steven Ortega | I continued with the implementation of US8 to keep a record of when an applicant's status is changed and also I created the branch of US11a to make the improvement | I will start to make the corrections of the US11 in the branch US11a to improve the applicant creation with a better interface | No |
| Camilo Carmona Valencia | I continued my research regarding pdf generation and images | I will continue until I can render a pdf with an image | My lack of knowledge |

## 25/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
| Andrés Camilo Romero Ruiz | I implemented dynamic search for lists and tables | I will implement dynamic search for list of buttons so my teammates can use the implementation to their own purposes | No |
| Juan Camilo Salazar | I continued investigating dynamic forms | I will start the implementation of dynamic forms for the additional events in an announcement| No |
| Juan Sebastián Libreros | I couldn't work yesterday due to personal problems | I will continue reformating the app | No |
| Camilo Carmona Valencia | I was able to get images rendering in a pdf using xhtml2pdf | I will make the report template | No |
| Brayan Steven Ortega | I started to work in the US11a separating the forms of applicant creation to do this in steps for the user | I will add in the applicant table in the database a field for the picture of the applicant and also create this in the applicant creation page | No |

## 26/10/2023

| Name | What did you do yesterday? | What will you do today? | Are there any impediments in your way? |
|----------|----------|----------|----------|
|Juan Camilo Salazar| I created the announcement individual view, changed the connections to the announcement edit page, and started implementing dynamic forms| I will continue the implementation of the dynamic form | No |
| Andrés Camilo Romero Ruiz | I implemented a dynamic search for list of buttons and pushed the commit so my teammates can use the dynamics searches I made | I will make a progress bar and start the form for generate reports | No |

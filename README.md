# MongoDB Task Manager

A task manager site created using a non-relational database, MongoDB. This site was created as part of a walkthrough project from the Code Institute.

![MongoDB Task Manager Responsive Site Image](static/images/mongodb-taskmanager.png)

Link to deployed site: [MongoDB Task Manager](https://mongodb-taskmanager.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/kera-cudmore/mongodb-taskmanager?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/kera-cudmore/mongodb-taskmanager?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kera-cudmore/mongodb-taskmanager?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/kera-cudmore/mongodb-taskmanager?style=for-the-badge)

## CONTENTS

* [User Experience](#User-Experience)
  * [User Stories](#User-Stories)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Typography](#Typography)
  * [Imagery](#Imagery)
  * [Wireframes](#Wireframes)
  * [Features](#Features)
  * [Accessibility](#Accessibility)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Database Used](#Database-Used)
  * [Frameworks Used](#Frameworks-Used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#Programs-Used)
  * [Defensive Programming](#Defensive-Programming)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#Deployment)
  * [Local Development](#Local-Development)
    * [How to Fork](#How-to-Fork)
    * [How to Clone](#How-to-Clone)

* [Testing](#Testing)
  
* [Credits](#Credits)
  * [Code Used](#Code-Used)

- - -

## User Experience

### User Stories

#### First Time Visitor Goals

* As a first time user, I want the site to be easy to navigate.
* As a first time user, I want to be able to add categories to store my tasks in.
* As a first time user, I want to be able to save tasks I create in a category of my choice.
* As a first time user, I want to be able to sign up for an account.

#### Returning Visitor Goals

* As a returning user, I want to be able to edit tasks.
* As a returning user, I want to be able to edit categories.
* As a returning user, I want to be able to log in to my account.

#### Frequent Visitor Goals

* As a frequent user, I want to be able to delete tasks I no longer want.
* As a frequent user, I want to be able to delete categories that I no longer need.

- - -

## Design

### Colour Scheme

The colour theme for the site is the same as the one used during the walkthrough videos, the colours used are from Materialize blue colour palette.

![Materialize colour palette](documentation/materialize-colour.png)

### Typography

No font was specified for use with the site, therefore the default font settings were used.

### Imagery

The site has been created to  learn and showcase CRUD functionality, no images have been used. All icons used in this project were sourced from [Font Awesome](https://fontawesome.com/).

### Wireframes

Wireframes were created for mobile, tablet and desktop using Balsamiq.

![Home Page](documentation/wireframes/home.png)

![Tasks Page](documentation/wireframes/tasks.png)

![Profile Page](documentation/wireframes/profile.png)

![Manage Categories Page](documentation/wireframes/manage-categories.png)

![Edit Category Page](documentation/wireframes/edit-category.png)

### Features

The website is comprised of 9 pages: The register page which allows users to register an account, the login page, the home page which displays all the users tasks, the profile page, the new task page which allows users to create a new task, the manage categories page which displays all categories, the edit category and edit task pages which allow users to edit an existing category & task and the add tasks and add categories pages which allow users to create new categories and tasks.

All Pages on the website have:

* A Favicon. The favicon for the site was created at [Favicon.io](https://favicon.io/emoji-favicons/check-box-with-check) and was generated using the following graphics from Twitter Twemoji:

  * Graphics Title: 2611.svg
  * Graphics Author: [Copyright 2020 Twitter, Inc and other contributors](https://github.com/twitter/twemoji)
  * Graphics Source: [Twemoji](https://github.com/twitter/twemoji/blob/master/assets/svg/2611.svg)
  * Graphics License: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)

    ![MongoDB Task Manager Favicon](documentation/favicon.png)

* A Navbar.The navbar contains links to the home, login and register pages when a user is not logged in. When a user is logged in the navbar will then display links for home, profile, new task, manage categories and log out. The navbar is responsive and on smaller devices uses the hamburger icon. When this is clicked the menu opens to the right of the screen.

  ![MongoDB Task Manager Navbar - Desktop](documentation/navbar-desktop.png)

  ![MongoDB Task Manager Navbar - Mobile](documentation/navbar-mobile.png)

  ![MongoDB Task Manager Navbar - Mobile Open](documentation/navbar-mobile-open.png)

- - -

`Home Page (Tasks)`

![Home Page/Tasks Page](documentation/homepage.png)

`Register Page`

![Register Page](documentation/registerpage.png)

`Login Page`

![Login Page](documentation/loginpage.png)

`Profile Page`

![Profile Page](documentation/profilepage.png)

`Add Category Page`

![Add Category Page](documentation/addcategorypage.png)

`Add Task Page`

![Add Tasks Page](documentation/addtaskpage.png)

`Categories Page`

![Categories Page](documentation/categoriespage.png)

`Edit Category Page`

![Edit Category Page](documentation/editcategorypage.png)

`Edit Task Page`

![Edit Tasks Page](documentation/edittaskpage.png)

- - -

Future Implementations.

* Defensive programming - I would like to add a modal that pops up when a user wants to delete a category. This would provide an extra layer of security to confirm that the user does want to delete the record from the database, and would alert the user to the fact that this action is permanent and cannot be undone.
* 404 Error Page.
* I would like to improve the profile page for the user, and use this area to allow the user to change their password for their account.

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. This has been have achieved by:

* Using semantic HTML.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient colour contrast throughout the site.

- - -

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

### Database Used

[MongoDB](https://www.mongodb.com/) - A non-relational database used to store the users login information, the categories and the tasks.

### Frameworks Used

[Flask](https://pypi.org/project/Flask/) - A microframework.

[Materialize](https://materializecss.com/) - Version 1.0.0 for the front end framework.

### Libraries & Packages Used

[Font Awesome](https://fontawesome.com/v5/search) - Version 5.15.3 - For the iconography on the website.

[PyMongo](https://pypi.org/project/pymongo/) - Python Driver for MongoDB.

### Programs Used

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Tiny PNG](https://tinypng.com/) To compress images.

[Favicon.io](https://favicon.io/) To create favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

[Shields.io](https://shields.io/) To add badges to the README

[Pip](https://pypi.org/project/pip/) - Tool for installing python packages

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine

### Defensive Programming

This walkthrough project has introduced the concept of defensive programming, however there are still areas that could be improved.

- - -

## Deployment & Local Development

### Deployment

The site is deployed using [Heroku](https://www.heroku.com). To deploy to Heroku:

1. To successfully deploy on Heroku we first need to create some files: a requirements.txt file and a Procfile.

2. The requirements.txt file contains all the applications and dependencies that are required to run the app. To create the requirements.txt file run the following command in the terminal:

    ```bash
    pip3 freeze --local > requirements.txt
    ```

3. The Procfile tells Heroku which files run the app and how to run it. To create the Procfile run the following command in the terminal:

    ```bash
    echo web: python app.py > Procfile
    ```

    NOTE: The Procfile uses a capital P and doesn't have a file extension on the end.

4. If the Procfile has been created correctly it will have the Heroku logo next to it. It is also important to check the Procfile contents, as sometimes on creation a blank line will be added at the end of the file. This can sometimes cause problems when deploying to Heroku, so if the file contains a blank line at the end, delete this and save the file. Make sure to save both these files and then add, commit and push them to GitHub.

5. Login (or sign up) to [Heroku.com](https://www.heroku.com).

6. Click the new button and then click create new app.

7. You will then be asked to give your app a name (these must be unique) and select a region. Once these are completed click create app.

8. You will now need to connect the Heroku app to the GitHub repository for the site. Select GitHub in the deployment section, find the correct repository for the project and then click connect.

9. Once the repository is connected, you will need to provide Heroku some config variables it needs to build the app. Click on the settings tab and then click reveal config vars button. You will now need to add the environment key/value variables that were used in the env.py file:

    | KEY | VALUE |
    | :-- | :-- |
    | IP | 0.0.0.0 |
    | PORT | 5000 |
    | SECRET_KEY| YOUR_SECRET_KEY* |
    | MONGO_URI | MONGO_URI* |
    | MONGO_DBNAME | MONGO_DB* |
    | DEBUG | TRUE** |

    *Denotes a value that is specific to your app.

    **This is set to true while deploying to enable us to see any bugs. Please change to FALSE after deployment.

10. You're now ready to click the enable automatic deploys and create button. Heroku will start building the app.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [mongodb-taskmanager](https://github.com/kera-cudmore/mongodb-taskmanager).
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mongodb-taskmanager](https://github.com/kera-cudmore/mongodb-taskmanager).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3 and press enter.

- - -

## Testing

Please see [testing.md](TESTING.md) for all testing performed

- - -

## Credits

### Code Used

This site was created as part of a walkthrough project with the Code Institute.

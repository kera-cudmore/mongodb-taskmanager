# MongoDB Task Manager

![MongoDB Task Manager Site Responsive Image](static/images/mongodb-taskmanager.png)

Visit the deployed site: [MongoDB Task Manager](https://mongodb-taskmanager.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [JavaScript Validator](#JavaScript-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
  * [WAVE Testing](#WAVE-Testing)
* [MANUAL TESTING](#MANUAL-TESTING)
  * [Testing User Stories](#Testing-User-Stories)
  * [Full Testing](#Full-Testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.

During development I made use of google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [add_category.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fadd_category)
* [add_task.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fadd_task)
* [categories.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fget_categories)
* [edit_task.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fedit_task%2F62a5e16f0995a585ef6ec670)
* [login.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Flogin)
* [profile.html](documentation/testing/profile-htmlvalidator.png)
* [register.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fregister)
* [tasks.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fget_tasks)
* [edit_category.html](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmongodb-taskmanager.herokuapp.com%2Fedit_category%2F629a1fc0c611a37970709c45)

[style.css](documentation/testing/css.png)

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js]](documentation/testing/javascript.png)

- - -

### Python Validator

[PEP8](http://pep8online.com/)was used to validate the python files.

* [app.py](documentation/testing/python.png)

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

### Mobile Results

- - -

### WAVE Testing

[WAVE](http://wave.webaim.org/) (Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

- - -

## MANUAL TESTING

### Testing User Stories


| Goals | How are they achieved? | |
| :--- | :--- | :--- |
| `First Time Visitors` | | |
| I want the site to be easy to navigate. | The site features a navbar which allows the user to easily navigate through the site. | [Navbar](documentation/navbar-desktop.png) |
| I want to be able to add categories to store my tasks in. | When the user navigates to the manage categories page they are given the option to create a new category. | [Add New Categories](documentation/categoriespage.png) |
| I want to be able to save tasks I create in a category of my choice. | The user is given the option to create a new task from the home page, and when creating the task they can assign the task to the category of their choice. | [Save Task in Category of my choice](documentation/addtaskpage.png) |
| I want to be able to sign up for an account. | If a user is not signed in to the site, the register link will display in the navbar, allowing users to sign up to an account. | [Sign up page](documentation/registerpage.png) |
| `Returning Visitors` | | |
| I want to be able to log in to my account. | If a user is not logged in, the navbar will display a login and register link. | [Login to account](documentation/loginpage.png) |
| I want to be able to edit tasks. | When the user expands a task, they are given the option via button to edit the task. | [Edit Tasks](documentation/edittaskpage.png) |
| I want to be able to edit categories. | When the user visits the categories page, they are given the option via button on each category card to edit the category. | [Edit Categories](documentation/editcategorypage.png) |
| `Frequent Visitors` | | |
| I want to be able to delete categories that I no longer need. | When the user visits the manage categories page, they are given the option via button on each category card to delete the category. | [Delete Categories](documentation/categoriespage.png) |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| ` Navbar` |
| Task Manager site name | Redirects the user to the home page | Clicked the link | Redirected to the home page | Pass |
| Home |  Redirects the user to the home page  | Clicked the link | Redirected to the home page | Pass |
| Profile (Logged in user) | Redirects the user to the profile page | Clicked the link | Redirected to the profile page | Pass |
| New Task (Logged in user) | Redirects the user to the new task page | Clicked the link | Redirected to the new task page | Pass |
| Manage Categories (Logged in user) | Redirects the user to the manage categories page | Clicked the link | Redirected to the manage categories page | Pass |
| Log Out (Logged in user) | Logs the user out of the session and redirects to the home page. Links in the navbar should change to only display home, login and register | Clicked the link | User logged out and redirected to the home page. Links changed in navbar to only display home, login and register  | Pass |
| Login (No user in session) | Redirects the user to the login page | Clicked the link | Redirected to the login page | Pass |
| Register (No user in session) | Redirects the user to the register page | Clicked the link | Redirected to the register page | Pass |
| Hamburger menu on smaller devices | Opens the full nav menu | Clicked on the hamburger menu | full menu opens | Pass |
| ` Home Page` |  |  |  |  |
| Search Tasks - Search for a task (successful search)| A search will be carried out on the term entered into the search bar and return any results | Searched for a term that would return a result | A task that matched the search term was returned | Pass |
| Search Tasks - Search for a task (unsuccessful search)| A search will be carried out on the term entered into the search bar and return feedback to the user if the search was unsuccessful | Searched for a term that wouldn't return a result | A message displayed to let the user know there were no results found | Pass |
| Search Tasks - Reset the search | When the reset button is clicked the search will default to its original blank condition | Clicked reset button with text in the search bar  | Text removed and search reset to default condition | Pass |
| All Tasks are displayed | All tasks are displayed in date order | Checked the database to confirm all tasks displaying, and checked displaying in date order | All tasks are displaying and in date order | Pass |
| Click on a task bar | The task will open up to display more information to the user | Clicked on a bar | The task expands to display further information to the user | Pass |
| Task Done Button | When the user clicks the button, the task is removed from the list and a flash message displayed to let the user know the task has been deleted | Clicked button | Task removed from list | Pass |
| Edit Task Button | When the user clicks the button they are redirected to the edit task page, with the task information prepopulated | Clicked button | Redirected to the edit task page with the task information prepopulated | Pass |
| `New Task Page` |  |  |  |  |
| Ask Task Button - form not filled in | The user will be prompted to enter the task information | Clicked add task button without filling in form | Tooltips assist user in filling out the required fields | Pass |
| Add Task Button - form filled in | The user will be redirected to the home page where they will be able to see their task in the list of tasks, and a flash message lets the user know the task was successfully added | Created a task and clicked the add task button | Flash message displayed to let me know task successfully added and task appears in the list of tasks. | Pass |
| `Edit Task Page` |  |  |  |  |
| Cancel button | User is redirected to the task page and no changes are made to the task | Clicked cancel button | Redirected to tasks page with no changes made to the task | Pass |
| Edit Task Button | Flash message displays task edited successsfully | Edited task and clicked button | Flash message displayed to let me know edit was successful | Pass |
| `Manage Categories Page` |  |  |  |  |
| Add Category Button | On click, redirects user to the add category page | Clicked button | Redirected to the add category Page | Pass |
| Edit Category Button | User is redirected to the edit category page, where the category information is prepopulated | Clicked the edit category button | Redirected to the edit category page | Pass |
| Delete Category Button | The category card will be deleted and all tasks saved to that category are also cascade deleted from tasks | Clicked delete | Category deleted from the categories page, flash message displays to let user know the delete was sucessful. Any tasks linked to that category have also been deleted | Pass |
| `Add Category Page` |  |  |  |  |
| Add Category Button - Form not filled in | The user is prompted to fill in the category name | Clicked button without filling in form | Form doesn't submit and the category name input appears red to assist user knowing what they haven't filled in | Pass |
| Add Category Button - Form filled in | The Category is created and the user redirected to the manage categories page where they can see the new category. A flash message lets the user know the category was successfully created. | Created a new category and clicked add category | Redirected to manage categories page where a flash message lets me know the category was added. The new category is displayed on the page | Pass |
| `Edit Category Page` |  |  |  |  |
| Cancel Button | Returns the user to the manage categories page with no changes made to the category | clicked cancel button | Redirected to the manage categories page, no changes were made to the category | Pass |
| Edit Category Button | User will be redirected to the manage categories page where a flash message tells them the category has been successfully updated. The Category has been updated | Changed a category name and clicked edit category button | Redirected to the manage categories page where a flash message displays my category has been successfully updated. The category name on the category card has been changed. | Pass |

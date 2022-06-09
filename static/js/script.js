// Mobile Collapse for Navbar
$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
});

// Collapsible tasks
$(document).ready(function () {
    $('.collapsible').collapsible();
});

// Tooltip
$(document).ready(function () {
    $('.tooltipped').tooltip();
});

// Dropdowns for the categories in add task
$(document).ready(function(){
    $('select').formSelect();
  });

/* Date Picker for Task Due Date
  - format = the way the date is formatted to be stored in the database
  - yearRange = the number of years to display on either side of the current year
  - showClearBtn = gives the users the option to clear the datepicker
  - i18n = allows us to customise the calendar text - changing done button to select
*/
$(document).ready(function () {
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "select"
        }
    });
});
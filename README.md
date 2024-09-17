

# THE FOOTBALL ACADEMY ANALYTICS PROGRAM

![CCCCP header](/assets/images/terminal-overview.webp)
![CCCCP header](/assets/images/worksheet-overview.webp)

The Football Academy Analytics Program, is made to update the revenue of the 3 teams of a football academy, and is automated to calculate the total revenue, the difference compared to the previous month revenue, and to update the previous month revenue worksheet with the total revenue last calculated by the program,after all data are inserted and all other worksheet have been updated, so that si already in the system for the next update.

Link to the [Deployed Project](https://the-football-academy-analytics-b24b05f91367.herokuapp.com/)

Link to the [Worksheets](https://docs.google.com/spreadsheets/d/1dbK8_8o8HC8mALul1UhLBv48BKOpbxaC7maUhdOv3q8/edit?gid=1676227007#gid=1676227007)

## Contents


- [Site owner goals](#site-owner-goals)
- [User goals](#user-goals)
- [Pre development](#pre-development)
- [Development](#development)
- [Features](#features)
  - [Teams Revenue Update System](#teams-revenue-update-system)
  - [Feedback Messages](#feedback-messages)
  - [Validation](#validation)
- [Google Sheets](#google-sheets)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Testing Browsers](#Testing-browsers)  
  - [Code Validation](#code-validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
- [Bugs](#bugs)
- [Acknowledgements](#acknowledgements)

### Site owner goals

Provide a program that is easy to use and maintain.
Present a program that gives clear instructions each time a member of the staff visits.
Keep track of the individual teams and tariff plans revenue, and be able to automatic calculate the total and the difference between the current and last month ones.
Add the submitted informations and get access to them via a Google Sheets worksheet.

### User goals

Get clear instructions on how to use the system in front of them that they can refer to if needed.
The ability to easily input the revenue for the three teams of the academy and for the three different payment plans.
Get an automatic calculation of the total revenue of the three teams and a comparisation with the previous month one, also having the last total calculated automatically added to the previous month worksheet, to be ready for the next update.
Receive feedbacks when values are entered correctly and worksheets updated.

### Pre development

I wrote out notes and created a flow chart. All I had to do then is follow my notes and code one area at a time before moving on to the next. Below is the flow-chart i created using [Lucid Charts](https://www.lucidchart.com/pages/).

![ccccp flow chart](/assets/images/flow-chart.webp)

### Development

Code was written for each part of the program starting with the header and input for staff to add data and instruction on how to do that correctly. Once each section was working the development of the following section took place. Once all sections had been created testing took place, making sure all the validation criteria were respected and the correct error was shown when the data entered was not valid. Also tested that the worksheet were updated correclty and that the automatic calculations were giving the correct results. 


## Features

### Teams revenue update system

The program allows users to insert data to update the revenue for the 3 teams of the football academy. The user is required to insert 3 values respective to the 3 different payment plans, as players of the academy can book a single training session, a pack of 12 training sessions or annual subscription that gives access to unlimited training sessions. The program then requires to enter data for the 3 teams in a sequence, the under8 first automatically followed by the under11 and under13 team at last, providing instructions and examples on how to insert data correctly to the user:

![ccccp under8 data](/assets/images/under8.webp)
![ccccp under11 data](/assets/images/under11.webp)
![ccccp under13 data](/assets/images/under13.webp)

### Feedback Messages

The program provides feedback messages to the user, to inform when data has been entered correctly,if the worksheets have been updated or if the system is calculating some values:

![ccccp feedback messages](/assets/images/feedback.webp)

### Validation

The program has an automatic validation system that informs the user if the data entered is valid, showing an error depending on the type of wrong data entered and redirecting the user to the input request, as shown in the picture below:

![ccccp ](/assets/images/literal-error.webp)
![ccccp](/assets/images/list-error.webp)

## Google Sheets

Google Sheets worksheets were used in this project to update and show the data entered by the user, and the data automatically calculated and updated by the program itself.
Six different worksheets were created, with three of them related to the teams, and other three related to the total revenue, previous revenue and the difference between the total just calculated and the previous one. 

Link to the [Football Academy Analytics Worksheets](https://docs.google.com/spreadsheets/d/1dbK8_8o8HC8mALul1UhLBv48BKOpbxaC7maUhdOv3q8/edit?gid=1676227007#gid=1676227007)

![ccccp under8 worksheet](/assets/images/worksheet-overview.webp)
![ccccp under11 worksheet](/assets/images/under11-worksheet.webp)
![ccccp under13 worksheet](/assets/images/under13-worksheet.webp)
![ccccp total worksheet](/assets/images/total-worksheet.webp)
![ccccp previous worksheet](/assets/images/previous-worksheet.webp)
![ccccp difference worksheet](/assets/images/difference-worksheet.webp)


## Technologies Used

The main technology used to create this program is Python.
I also used [Colorama](https://pypi.org/project/colorama/) library to change color to the terminal text,
and [Heroku](https://dashboard.heroku.com/apps/the-football-academy-analytics) and [Github](https://github.com/alelodato/The-Football-Academy-Analytics) to deploy the project.
The flow chart was made using [Lucid Charts](https://www.lucidchart.com/pages/).

## Testing

Once the portal was operational I set about testing it for errors and to ensure any possible errors that can be made were caught.

### Manual Testing

The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Test Passed** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Program Started | User is shown a header and instructions on what data to insert, follow by an input request | Program start screen presented | Yes |
| Under8 team data input | User is asked to enter data for the under 8 team | Under8 revenue data team  input requested| Yes | 
| Under11 team data input | User is asked to enter data for the under 11 team | Under11 revenue data team  input requested| Yes | 
| Under13 team data input | User is asked to enter data for the under 13 team | Under13 revenue data team  input requested| Yes | 
| Data Validation | Errors shown if user enters incorrect data | Errors shown | Yes |
| Feedback Messages | User is shown feedback messages related to input entered, worksheet update and automatic calculations by the program | Feedback messages are shown correctly | Yes |
| Teams Worksheets | Data entered by the user is shown correctly and the related worksheet is updated correctly | Worksheets updated correctly and correct data shown | Yes |
| Total Revenue Worksheet | The total revenue for the 3 teams should be automatically calulated and shown in this worksheet | Total revenue for the 3 teams calculated and shown in the worksheet correctly | Yes |
| Difference Revenue Worksheet | The revenue difference in between this and last month for the 3 teams should be automatically calulated and shown in this worksheet | Revenue for the 3 teams calculated and shown in the worksheet correctly | Yes |
| Previous Revenue Worksheet | The total month revenue calculated is to be add in this worksheet at the end of the program, to be ready for next update | Total revenue for the 3 teams calculated and shown in this worksheet correctly at the end of the program| Yes |

### Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome
- Edge
- Firefox
- Safari

It worked without issues in the above browsers.

### Code Validation

PEP8 - Python code was validate using the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/#)
All code validated and where docstrings were too long they were adjusted. The only errors shown are related to the messages and feedbacks printed to the terminal,that are longer than 79 characters.

## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example corri-construction-p3) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.
   
The deployed project live link is [HERE](https://the-football-academy-analytics-b24b05f91367.herokuapp.com/)

## Bugs

No bugs experienced in deployed project.

## Acknowledgements

I want to acknoledge my mentor Jubril for suggesting using the Colorama library to add color to the program text.

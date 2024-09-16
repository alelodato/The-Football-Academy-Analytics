

# THE FOOTBALL ACADEMY ANALYTICS PROGRAM
![CCCCP header](/assets/images/terminal-overview.webp)
![CCCCP header](/assets/images/worksheet-overview.webp)

The Football Academy Analytics Program, is made to update the revenue of the 3 teams of a football academy, and is automated to calculate the total revenue, the difference compared to the previous month revenue, and to update the previous month revenue worksheet with the total revenue last calculated by the program,after all data are inserted and all other worksheet have been updated, so that si already in the system for the next update.

The deployed project live link is [HERE](https://the-football-academy-analytics-b24b05f91367.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Contents


- [User goals:](#user-goals)
- [Site owner goals](#site-owner-goals)
- [Pre development](#pre-development)
- [Development](#development)
- [Features](#features)
  - [Slow Typing Instructions](#slow-typing-instructions)
  - [Name and profession input](#name-and-profession-input)
  - [Hourly pay and employee number](#hourly-pay-and-employee-number)
  - [Working dates, days and hours](#working-dates-days-and-hours)
  - [Confirm information so far](#confirm-information-so-far)
  - [Tax and National Insurance](#tax-and-national-insurance)
  - [Confirmation of information](#confirmation-of-information)
  - [What the portal checks](#what-the-portal-checks)
  - [Error Page](#error-page)
- [Google Sheets](#google-sheets)
  - [Payments](#payments)
  - [Tax](#tax)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
  - [Libraries](#libraries)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

### Site owner goals

Provide a program that is easy to use and maintain.
Present a program that gives clear instructions each time a member of the staff visits.
Keep track of the individual teams and tariff plans revenue, and be able to automatic calculate the total and the difference between the current and last month ones.
Add the submitted informations and get access to them via a Google Sheets worksheet.
### User goals:

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

The program has been well tested and the results can be viewed [here - TESTING](https://alelodato/The-Football-Academy-Analytics/blob/main/TESTING.md)

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

### Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
   
The deployed project live link is [HERE](https://corri-construction-8c4725a33281.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Bugs

After importing the type element so that text can be typed out a line at a time the codes for Fore.WHITE or bold kept showing up e.g. '\033[1m' for bold was typed out. To fix this I had to remove - colorama.init(autoreset=True) - which  meant I had to go through each line of code to ensure if one line was red, all subsequent lines didn't turn red. 

## Credits

Free Code Camp Python for everyone course that helped me get my project started - [here](https://www.youtube.com/watch?v=wgkC8SxraAQ)

py4e autograder to help with checking maths - [here](https://www.py4e.com/tsugi/store/test/pythonauto )

Geek for Geek to help me use strip() to add required field for first/last name - [here](https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/)


Help putting together the function that calculates income tax and national insurance I started with this video and adapted it - [here](https://www.youtube.com/watch?v=b4lok6-_GGg )

To change numerical value to end in two figures only - [here](https://tutorial.eyehunts.com/python/how-to-display-2-decimal-places-in-python-example-code/)

Using colorama import - [here](https://www.youtube.com/watch?v=u51Zjlnui4Y )


Being able to bold and center font - taken from w3Schools - [here](https://www.w3schools.com/python/ref_string_center.asp)


## Acknowledgements

Code Institute women-in-tech group for their support during huddles and when reviewing my code.

Peer-review slack channel for help trying to find any issues/break the code.

Tutor support for help with figuring out how to round numbers in Google sheet.

Travis.media community - To help with date/hours/time function so it worked correctly.

My mentor Andre Aquilina for teaching me about the proper structure for code - e.g. imports, functions, main code and for encouraging me to create the Google sheets addition and for helping with explaining coding.

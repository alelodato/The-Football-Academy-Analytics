
# Testing

Once the portal was operational I set about testing it for errors and to ensure any possible errors that can be made were caught.

The deployed project live link is [HERE](https://the-football-academy-analytics-b24b05f91367.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Manual Testing

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

## Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome
- Edge
- Firefox
- Safari

It worked without issues in the above browsers.

## Code Validation

PEP8 - Python style guide checker imported - https://pypi.org/project/pep8/
All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code and it stopped working so they were left as longer lines to avoid this issue. pycodestyle . - was used in Codeanywhere terminal to list any issues.


### [BACK TO README](https://github.com/todiane/corri-construction-p3/blob/main/README.md)
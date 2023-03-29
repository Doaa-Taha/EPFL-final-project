# MY FINAL PROJECT
  It's a shopping list with a cost tracker. 
- What does it do?  
  It allows the user to add items to buy with their quantities and prices and then it calculate the cost with the ability to update or delete the item. The user can also search for his/her cost for a specific date. 
- What is the "new feature" which you have implemented that we haven't seen before?  
  tracking the cost of the user's shopping list and ability to update or delete data.

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? 
No

## Project Checklist
- [T] It is available on GitHub.
- [T] It uses the Flask web framework.
- [T] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: json , os
- [T] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name: products.py
  - Line number(s): 8 : 20
  - Name of two properties: name, quantity, price, date
  - Name of two methods: cal_cost, update_amount
- [T] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [T] It uses modern JavaScript (for example, let and const rather than var).
- [T] It makes use of the reading and writing to a file feature.
- [T] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: products.py
  - Line number(s): 31, 74
  - File name: helpers.py
  - Line number(s): 22, 35, 52, 61, 72, 82, 90
- [T] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: products.py
  - Line number(s):29
  - File name: helpers.py
  - Line number(s):24, 51, 60, 71, 81, 93
- [T] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [T] It doesn't generate any error message even if the user enters a wrong input.
- [T] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [T] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.
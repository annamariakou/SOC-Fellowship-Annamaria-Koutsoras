# 🐍 Intro to Python

Welcome to Python 101! Python is a programming language used across many fields like web development, data analysis and AI. Due to its simplicity and readability it's a great language for you to begin your programming journey.

## 🚀 Objectives

- Create a plan and break down problems.
- Python fundamentals:
  - Variables & Types
  - Operations
  - Lists
  - Conditions and if statements
  - Functions
- Continued pair programming.
- Test your work.

## 📖 Resources

If you need a refresher on the fundamentals mentioned above, please review the resources below before beginning the workshop.

- [Python Tutorial](https://www.w3schools.com/python/default.asp)
- [Operators](https://www.geeksforgeeks.org/python-operators/)
- [Lists](https://developers.google.com/edu/python/lists)
- [Conditions and if statements](https://www.geeksforgeeks.org/conditional-statements-in-python/)
- [Functions](https://youtu.be/zvzjaqMBEso?feature=shared)

## 🚨 Install

Before you begin make sure you've installed python on your machine. Instructions can be found [here](https://www.python.org/downloads/).

You must also install the VS Code Python extension by Microsoft. You can find it in the marketplace [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## 🎟️ Tickets

Let's get coding!

### ✨ Ticket 1 - Getting Started ✨

### Ticket 1a

It's time to create your first python file! Create a file called `main.py`.

### Ticket 1b

Now let's make sure your file is working correctly. Print `Welcome to Python 101` and check that it prints correctly in your console.

💡 If your message isn't printing. Double check that you've installed python properly and revist how to run python code in your console. Hint: It's just like starting a video!

### Ticket 1c

Add a comment above your printed message that says `Ticket 1b`

💡 As you continue through the workshop, it's important to comment your code to track your work and write a plan.

### ✨ Ticket 2 - Food Shopping ✨

Sunday has come around and you realised you forgot to go food shopping! Oh no 😮!

### Ticket 2a

As you have a weekly budget to work with, assign `100` pounds to a variable called `weekly_budget`.

Print `weekly_budget` to your console.

### Ticket 2b

You've arrived to Tesco and as you add coffee and sugar to your basket, you realise you need to calculate how much remaining budget you have.

Create two variables `item_one` and `item_two`. Assign **£3** to `item_one` and **£5** to `item_two`.

Print `item_one` and `item_two` to your console.

### Ticket 2c

Add `item_one` and `item_two` assigning them to the variable `total_spent`.

Next, subtract the remaining `total_spent` from `weekly_budget` and assign it to a variable called `remaining_budget`.

Print `remaining_budget` to your console.

### ✨ Ticket 3 - Shopping List ✨

### Ticket 3a

You realise you forgot your shopping list at home! In order to not forget anything, create a list called `shopping_list` with these 4 new items; **Apples, Grapes, Olive Oil, Soap** . Each item is a **string**.

Print `shopping_list` to your console.

### Ticket 3b

Your mum just called you to tell you to add pineapple to the list. Using one of python's built in methods, add pineapple to `shopping_list`.

Print `shopping_list` to your console. You should now see pineapple added to the end of your list.

### ✨ Ticket 4 - Tracking Items ✨

As the basket gets fuller we need to create a function to track what we've picked up.

### Ticket 4a

Create a function called `checklist`. Give the function two parameters with the first one as `shopping_list` and the secone one as `item`.

‼️ The parameter `shopping_list` is taken from the variable you declared in step 3a. Ensure that this global variable is still declared (do not delete or comment it out).

### Ticket 4b

In function `checklist` write an if...else statement that follows the following conditions:

- Removes the item from `shopping_list` if it is in `shopping_list`. Prints `"Item removed from shopping list"`
- Otherwise print `"Item is not on shopping list"`

### Ticket 4c

To run the function you must:

- Call the function `checklist`

To see your updated shopping list:

- Print `shopping_list`.

## 🎯 Testing

Once you've completed all the tasks, complete the following steps to test your work -

In your terminal run:

```bash
  pip install pytest
```

Then to run the tests that have already been added to test_main.py run:

```bash
  pytest test_main.py
```

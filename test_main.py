import pytest
from main import checklist

def test_print_welcome_message(capsys):
    print("Welcome to Python 101")
    captured = capsys.readouterr()
    assert captured.out == "Welcome to Python 101\n"

def test_weekly_budget(capsys):
    weekly_budget = 100
    print(weekly_budget)
    captured = capsys.readouterr()
    assert captured.out == "100\n"

def test_item_prices(capsys):
    item_one = 3
    item_two = 5
    print(item_one)
    print(item_two)
    captured = capsys.readouterr()
    assert captured.out == "3\n5\n"

def test_remaining_budget(capsys):
    weekly_budget = 100
    item_one = 3
    item_two = 5
    total_spent = item_one + item_two
    remaining_budget = weekly_budget - total_spent
    print(remaining_budget)
    captured = capsys.readouterr()
    assert captured.out == "92\n"

def test_shopping_list_initial(capsys):
    shopping_list = ["Apples", "Grapes", "Olive Oil", "Soap"]
    print(shopping_list)
    captured = capsys.readouterr()
    assert captured.out == "['Apples', 'Grapes', 'Olive Oil', 'Soap']\n"

def test_shopping_list_append(capsys):
    shopping_list = ["Apples", "Grapes", "Olive Oil", "Soap"]
    shopping_list.append("Pineapple")
    print(shopping_list)
    captured = capsys.readouterr()
    assert captured.out == "['Apples', 'Grapes', 'Olive Oil', 'Soap', 'Pineapple']\n"

def test_checklist_exists(capsys):
    shopping_list = ["Apples", "Grapes", "Olive Oil", "Soap", "Pineapple"]
    checklist(shopping_list, "Apples")
    captured = capsys.readouterr()
    assert "Apples" not in shopping_list
    assert len(shopping_list) == 4
    assert captured.out == "Item removed from shopping list\n"

def test_checklist_not_exists(capsys):
    shopping_list = ["Apples", "Grapes", "Olive Oil", "Soap", "Pineapple"]
    checklist(shopping_list, "Bananas")
    captured = capsys.readouterr()
    assert "Bananas" not in shopping_list
    assert len(shopping_list) == 5
    assert captured.out == "Item is not on shopping list\n"

if __name__ == "__main__":
    pytest.main()

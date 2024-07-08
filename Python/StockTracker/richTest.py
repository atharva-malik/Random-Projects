from rich.console import Console
from rich.table import Table
from rich import print as p

table = Table(title="Rich Table Example")
table.add_column("Fruit", style="green")
table.add_column("Price", justify="right")

fruits = ["Apple", "Orange", "Watermelon", "Pear", "Grape", "Strawberry"]
prices = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00]

for fruit, price in zip(fruits, prices):
    table.add_row(fruit, str(price))

p(table)
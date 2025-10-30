"""Inventory System Module
Provides add, remove, load, and save operations for stock data.
"""

import json
import logging
from datetime import datetime
import ast

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global stock dictionary
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a given quantity of an item to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(
            "Invalid input types for add_item: item=%s, qty=%s",
            item,
            qty
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a given quantity of an item from stock, delete if quantity <= 0."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Tried to remove non-existent item: %s", item)
    except TypeError:
        logging.error("Invalid type for qty in remove_item: %s", qty)


def get_qty(item):
    """Return quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file without using global statement."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        logging.warning("File not found: %s. Starting with empty stock.", file)


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print all stock items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block for testing the inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("mango", 15)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

    safe_expr = "['eval', 'used']"
    result = ast.literal_eval(safe_expr)
    print("Safe evaluation result:", result)


if __name__ == "__main__":
    main()

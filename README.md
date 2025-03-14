# OOP Assignment

## Overview 📱📱
This script demonstrates basic **Object-Oriented Programming (OOP)** concepts in Python, including:
* **Classes & Objects**
* **Inheritance**
* **Polymorphism**
* **Constructors**

The script defines two main classes:
1. **Device**: A generic class representing devices with common attributes such as `brand`, `model`, and `battery_percentage`.
2. **Smartphone**: A class that inherits from `Device` and adds smartphone-specific methods like `make_call()` and `send_message()`.
3. **Tablet**: Another class that inherits from `Device`, with unique attributes such as `screen_size` and methods like `browse_internet()` and an overridden `check_battery()` method.

## Features ✨
* **Smartphone Class**: Simulates actions like making calls, sending messages, and checking/charging the battery.
* **Tablet Class**: Demonstrates polymorphism by overriding the `check_battery()` method and adding a tablet-specific method for internet browsing.
* **Inheritance**: Both the `Smartphone` and `Tablet` classes inherit from the base `Device` class, sharing common functionality while introducing their own unique features.
* **Polymorphism**: The `Tablet` class overrides the `check_battery()` method to behave differently than the `Device` class.

## Requirements 🛠️
* Python 3.x

## How to Run 📋
1. Clone this repository to your local machine:

```bash
git clone https://github.com/alphac137/oop-assignment.git
```

2. Navigate to the project directory:

```bash
cd oop-assignment
```

3. Run the script using Python:

```bash
python3 main.py
```

## Example Output 📟
The script will output the following:

```
Smartphone Actions:
Calling 987-654-3210 from 123-456-7890...
Battery is at 50%.
Apple iPhone 14 charged to 80%.
Sending message: 'Hey, how are you?' to 987-654-3210

Tablet Actions:
Browsing the internet on Samsung Galaxy Tab with a 10 inch display.
Tablet battery is at 75%, with a 10 inch screen.
Samsung Galaxy Tab charged to 95%.
```

## Concepts Covered 🔍
* **Classes**: Creating a class with attributes and methods.
* **Objects**: Instantiating objects from a class and interacting with them.
* **Inheritance**: Using the base `Device` class and extending it in `Smartphone` and `Tablet`.
* **Polymorphism**: Overriding the `check_battery()` method in the `Tablet` class to show different behavior from the base class.

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

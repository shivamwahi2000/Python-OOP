# Python-OOP

This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python.

## Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data and code to manipulate that data. OOP focuses on the following key concepts:

### 1. Classes and Objects

- **Class**: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
- **Object**: An instance of a class. It is created using the class blueprint and can have its own unique data.

### 2. Encapsulation

Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit, or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data.

### 3. Inheritance

Inheritance is a mechanism where a new class (child class) inherits attributes and methods from an existing class (parent class). This allows for code reuse and the creation of a hierarchical relationship between classes.

### 4. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is the ability to redefine methods in derived classes.

### 5. Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. It helps in reducing programming complexity and effort.

## Example Concepts in the Project

The `BankAccount` class in this project demonstrates some of these OOP concepts:

- **Class and Object**: The `BankAccount` class is a blueprint for creating bank account objects.
- **Encapsulation**: The class encapsulates the account holder's information and balance, and provides methods to interact with these attributes.
- **Inheritance**: If there were other types of accounts (e.g., `SavingsAccount`, `CheckingAccount`), they could inherit from the `BankAccount` class.
- **Polymorphism**: Methods in derived classes could override methods in the `BankAccount` class to provide specific functionality.
- **Abstraction**: The class provides a simplified interface for interacting with the account, hiding the complex implementation details.
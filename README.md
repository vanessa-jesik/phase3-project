# Cookbook and Recipe Management System

This Cookbook and Recipe Management System is a Python-based application that allows users to manage cookbooks and recipes. It provides a command-line interface (CLI) for performing various operations, such as creating, updating, and deleting cookbooks and recipes, as well as searching for specific cookbooks and recipes based on different criteria.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [CLI Commands](#cli-commands)
- [Project Structure](#project-structure)
- [Database](#database)
- [Seed Data](#seed-data)
- [Contributing](#contributing)

## Features

- **Cookbook Management**: Users can create, update, list, and delete cookbooks.
- **Recipe Management**: Users can create, update, list, and delete recipes associated with cookbooks.
- **Search Functionality**: Users can search for cookbooks and recipes by name, author, ID, cuisine, servings, and cook time.
- **Data Persistence**: Data is stored in an SQLite database, allowing for data persistence between sessions.
- **Sample Data**: The system includes seed data with predefined cookbooks and recipes for testing.

## Getting Started

### Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3
- SQLite (for database storage)

### Installation

1. Clone the repository to your local machine
2. Change into the project directory
3. Install the required Python packages

## Usage

To use the Cookbook and Recipe Management System, follow these steps:

1. Run the seed.py script to initialize the database with sample data:
    - python seed.py
2. Run the CLI interface to interact with the system:
    - python cli.py

### CLI Commands

The CLI provides the following commands:

- **List all cookbooks**: List all cookbooks in the system.
- **Find cookbooks by name**: Find a cookbook by its name.
- **Find cookbooks by author**: Find cookbooks by the author's name.
- **Find cookbook by ID**: Find a cookbook by its unique identifier.
- **Create cookbook**: Create a new cookbook by providing its name, author, and publishing date.
- **Update cookbook**: Update the details of an existing cookbook.
- **Delete cookbook**: Delete a cookbook from the system.
- **List all recipes**: List all recipes in the system.
- **Find recipes by name**: Find a recipe by its name.
- **Find recipe by ID**: Find a recipe by its unique identifier.
- **Find recipes by cuisine**: Find recipes by cuisine type.
- **Find recipes by servings**: Find recipes by the number of servings.
- **Find recipes by cook time parameters**: Find recipes based on specific cooking time parameters.
- **Create recipe**: Create a new recipe by providing its name, cuisine, cook time, servings, and associated cookbook ID.
- **Update recipe**: Update the details of an existing recipe.
- **Delete recipe**: Delete a recipe from the system.
- **List all recipes in a cookbook**: List all recipes associated with a specific cookbook.
- **Exit the program**: Terminate the CLI application.

## Project Structure

The project is organized into the following modules:

- `models`: Contains the Cookbook and Recipe classes that define the database schema.
- `lib`: Contains the Python scripts used for various functionalities.
- `seed.py`: Initializes the database with sample data.

## Database

The application uses an SQLite database to persist cookbook and recipe data. The database schema is defined by the Cookbook and Recipe classes in the `models` module.

## Seed Data

The `seed.py` script populates the database with initial data, including predefined cookbooks and recipes. This data can be used for testing and demonstration purposes.

## Contributing

This project was created by Github users **vanessa-jesik** and **adgholson**. Contributions to this project are welcome! If you have ideas for improvements or feature additions, please open an issue or submit a pull request.
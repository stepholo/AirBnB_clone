# AirBnB Clone - The Console

Welcome to the AirBnB Clone - The Console project! This project serves as the initial step towards building a comprehensive web application, emulating the functionality of the popular platform Airbnb. In this endeavor, you will be crafting a powerful command interpreter that will enable you to manage various objects central to the AirBnB experience, such as Users, States, Cities, Places, Amenities, and Reviews. This command interpreter will be your tool to interact with the backend of the application and manipulate the data stored within it.

## Background Context

Before embarking on this exciting journey, it's essential to grasp the core concepts underpinning the AirBnB clone and the various objects you will be orchestrating. Familiarizing yourself with these concepts will empower you to construct a strong foundation for the subsequent tasks in the project.

### Key Concepts to Focus On

- **Python Packages:** Modular code organization through packages is crucial for a scalable project.
- **AirBnB Clone:** Understanding the architecture and design of the AirBnB-like platform.
- **Serialization and Deserialization:** The process of converting objects into a storable format and vice versa.
- **Command-Line Interface (CLI):** Building an interactive shell for user interaction.
- **Unit Testing:** Writing tests to ensure the functionality of your code.

## Getting Started

### Prerequisites

- Python 3.8.5
- pycodestyle (version 2.8.*)

### Installation

1. Clone this repository: `git clone https://github.com/your-username/AirBnB_clone.git`
2. Navigate to the project directory: `cd AirBnB_clone`

## Usage

To start the command interpreter, execute the following command:

```bash
./console.py
```

Upon launching the console, you'll find yourself in an interactive mode with the prompt `(hbnb)` indicating its readiness for your commands.

### Available Commands

1. `create <class_name>`: Creates a new instance of the specified class (e.g., `create BaseModel`).
2. `show <class_name> <id>`: Displays the string representation of an instance.
3. `destroy <class_name> <id>`: Deletes an instance.
4. `all [class_name]`: Displays the string representation of all instances of the specified class or all classes if no class name is provided.
5. `update <class_name> <id> <attribute_name> "<attribute_value>"`: Updates the specified attribute of an instance.

### Examples

```bash
(hbnb) create BaseModel
2d8d11eb-2341-4a0e-b80d-3e40da69661f
(hbnb) show BaseModel 2d8d11eb-2341-4a0e-b80d-3e40da69661f
[BaseModel] (2d8d11eb-2341-4a0e-b80d-3e40da69661f) {'id': '2d8d11eb-2341-4a0e-b80d-3e40da69661f', 'created_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456), 'updated_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456)}
(hbnb) all BaseModel
["[BaseModel] (2d8d11eb-2341-4a0e-b80d-3e40da69661f) {'id': '2d8d11eb-2341-4a0e-b80d-3e40da69661f', 'created_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456), 'updated_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456)}"]
(hbnb) update BaseModel 2d8d11eb-2341-4a0e-b80d-3e40da69661f name "New Name"
(hbnb) show BaseModel 2d8d11eb-2341-4a0e-b80d-3e40da69661f
[BaseModel] (2d8d11eb-2341-4a0e-b80d-3e40da69661f) {'id': '2d8d11eb-2341-4a0e-b80d-3e40da69661f', 'created_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456), 'updated_at': datetime.datetime(2023, 8, 10, 12, 0, 0, 123456), 'name': 'New Name'}
(hbnb) quit
```

## Authors

This project was developed by Margaret Maina and Stephen Oloo.

## Contributing

We encourage contributions to this project. If you wish to contribute, please submit pull requests or reach out to the authors.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

We extend our gratitude to the AirBnB concept for inspiring this project. Special thanks to the instructors and mentors who guided us through the development process. Your support was invaluable in realizing this achievement.
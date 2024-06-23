![Foxhole Automate](assets/banner.png)

# Foxhole Automate

Foxhole Automate is a Python3 project designed to cater to the specific needs of players in the Foxhole game, particularly when multitasking between building and eating.

## Description

This automation tool is essential for Foxhole players who find it cumbersome to manage tasks like building and eating simultaneously. It provides a seamless solution tailored specifically for Foxhole gameplay.

The source code is open and freely available for anyone to modify according to their preferences. If you wish to customize keybindings or make other adjustments, you are encouraged to clone the repository, make your changes, build the tool, and enjoy a streamlined gaming experience.

## Inspiration

This project was inspired by [FoxholeTool](https://github.com/mmaenz/FoxholeTool).

## Table of Contents

- [Foxhole Automate](#foxhole-automate)
  - [Description](#description)
  - [Inspiration](#inspiration)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Building](#building)
    - [Development Build](#development-build)
    - [Production Build](#production-build)
  - [Contributing](#contributing)
  - [Future Plans](#future-plans)
  - [License](#license)

## Usage

Foxhole Automate provides several key bindings to automate common tasks in the game. All function keys are toggled, meaning pressing the key again will stop the corresponding action. Here are the default bindings and their functionalities:

- **F2**: Scrooping
  - Pressing F2 starts scrooping.
  - Pressing F2 again stops scrooping.
  - Right-clicking or pressing any of the WASD keys also stops scrooping.

- **F3**: Move Forward
  - Pressing F3 starts moving forward.
  - Useful for long distances between point A and point B during logistics
  - Pressing F3 again stops moving forward.
  - Pressing and releasing W will also stop moving forward.
  - Currently, there is a bug where mouse clicking can unintentionally stop this function.

- **F4**: Collecting Materials (Shift + Left Click)
  - Pressing F4 starts collecting materials from storage bunkers, town halls, relics, or stockpiles.
  - This action requires the user to have their mouse pointer over the item they want to collect.
  - Pressing F4 again stops collecting materials.
  - Pressing any of the WASD keys or right-clicking also stops collecting materials.

- **F5**: Artillery Reload and Fire
  - Pressing F5 starts the auto fire mechanism for artillery.
  - Pressing F5 again stops the auto fire mechanism.
  - Pressing any of the WASD keys or right-clicking also stops the artillery firing.

## Installation

To install Foxhole Automate:

1. **Download the Latest Release:**
   - Go to the [Releases](https://github.com/CamposmDev/foxhole-automate/releases) page.
   - Download the latest release package (`zip` or `tar.gz` file) for your operating system.

2. **Extract the Package:**
   - Extract the downloaded package to a directory of your choice.

3. **Run the Program:**
   - Open a terminal or command prompt.
   - Navigate to the extracted directory containing the executable.
   - Execute the binary file:
     ```bash
     ./foxhole-auto   # Replace with the actual name of your binary file
     ```

   - You may need to make the binary file executable if it's not already:
     ```bash
     chmod +x foxhole-auto   # Replace with the actual name of your binary file
     ```

## Building

### Development Build

To build the program for development purposes, follow these steps:

1. **Install Dependencies:**
   - Make sure you have Python3 installed on your system.
   - Install the required dependencies using pip:
     ```bash
     pip install pynput
     ```

2. **Run the Program:**
   - Navigate to the project directory:
     ```bash
     cd path/to/foxhole-auto
     ```
   - Execute the main script:
     ```bash
     python3 src/main.py
     ```

### Production Build

For a production build, which includes creating a standalone executable, follow these steps:

1. **Install PyInstaller:**
   - Install PyInstaller, a tool to package Python applications into standalone executables:
     ```bash
     pip install pyinstaller
     ```

2. **Build the Program:**
   - Run the build script to generate the executable:
     ```bash
     python3 build.py
     ```
   
3. **Locate the Binary File:**
   - After successful execution, the built executable will be located in the `dist` directory.

## Contributing

We welcome contributions to the Foxhole Automate project! To contribute, please follow these steps:

1. **Fork the Repository:**
   - Click the "Fork" button at the top right of the repository page to create a copy of the repository on your GitHub account.

2. **Clone the Forked Repository:**
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/CamposmDev/foxhole-automate.git
     ```

3. **Create a New Branch:**
   - Create a new branch for your feature or bugfix:
     ```bash
     git checkout -b feature-or-bugfix-name
     ```

4. **Make Your Changes:**
   - Implement your changes or new features in the new branch.

5. **Commit Your Changes:**
   - Commit your changes with a clear and concise commit message following conventional commit conventions:
     ```bash
     git add .
     git commit -m "type(scope): description of your changes"
     ```

     For example:
     ```bash
     git commit -m "feat(controls): add F6 key binding for new feature"
     ```

6. **Push to Your Fork:**
   - Push your changes to your forked repository on GitHub:
     ```bash
     git push origin feature-or-bugfix-name
     ```

7. **Create a Pull Request:**
   - Open a pull request to the main repository. Provide a detailed description of your changes and any additional context that might be needed for the maintainers to review your contribution.

## Future Plans

Future plans for the Foxhole Automate include transitioning it into a system tray application. This enhancement will allow the tool to run discreetly in the background, providing easy access to its functionalities while minimizing interference with gameplay.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

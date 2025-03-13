This project is a Dash application that visualizes data about video cameras installed in various cities in Georgia from 2019 to 2021. The application provides interactive graphs and maps to display the data.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/alexnat009/dash-app-videoCamera-map.git
    cd dash-app-videoCamera-map
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, execute the following command:
```sh
python creatingMap.py
python mainPage.py
```

The application will be available at `http://127.0.0.1:33507/`.

## Files

- mainPage.py: The main file that sets up and runs the Dash application.
- creatingMap.py: A script to create maps for the application.
- requirements.txt: A list of Python packages required for the project.
- assets: Contains CSS files for styling the application.
- dataset: Contains Excel files with data for each year.
- fonts: Contains custom fonts used in the application.
- website: Contains HTML files for the maps displayed in the application.


## Data Source

The data used in this application is sourced from:
- [info.police.ge](https://info.police.ge/page?id=305)
- [askgov.ge](https://askgov.ge)
- OpenStreetMap

## License

This project is licensed under the MIT License. See the LICENSE file for details.

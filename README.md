# Hansom (Flask Implementation)
*the flask implementation of hansom*

## Installation

This application requires Flask and Socket.IO

0. Make sure you're on Python 3 and have Java and Pip.

1. Clone this repository.

2. `cd` into HansomFlask. `cd HansomFlask`

3. Install the requirements directly with `pip install -r requirements.txt`

4. Download cassandra from https://cassandra.apache.org/.

5. Enter the cassandra directory, open the bin folder, and doubleclick on cassandra.bat.

6. `cd` into hansom. `cd hansom`

7. Run `python db_setup.py`

8. Edit config.json to the relevant values. Username and password are anything you like, set into the database. Hostname is your own IP address. Database name is your database name.

8. Run `python Hansom.py`

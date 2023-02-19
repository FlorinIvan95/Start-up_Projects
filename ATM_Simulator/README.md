This is a ATM Simulator where the card number and PIN must be entered to see the amount of money and to be able to make transactions (withdrawal/deposit).
Any transaction is registred on a MySQL database.

How to use:
1. download the "ATM_Simulator" folder to your PC
2. create an empty database in MySQL with the name "atm_simulator_v2" (another name can be used, but you will have to put the same name for the "database" inside the python code "main")
3. Select the "atm_simulator_v2" database with a double click or use the command "USE atm_simulator_v2" in a query MySQL window
4. Use the button "Open a SQL script file in a new query tab" and open the MySQL file "atm_simulator_v2" from the "ATM_Simulator" folder
5. Execute the script
6. In the python file "main" set the database connection using the "user" and "password" that you use when you create a connection in MySQL.

If you don't have the "pymysql" module installed:

1. Open Terminal
2. Type pip install pymysql
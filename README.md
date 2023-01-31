# Fetch Rewards - Take Home Test

**Name:** Rahul Sai Rajapalayam Sivakumar

**Email:** [rsr4@illinois.edu](mailto:rsr4@illinois.edu)


## How to run

- Clone the repo
- No libraries needed - just a Python installation required (uses inbuilt libraries)
- Run `python3 fetch_task.py <balance>` in the root directory. Eg. `python3 fetch_task.py 5000`
- A sample `transactions.csv` file is included in the root directory for testing, which corresponds to the sample data given in the instructions.
- The program will output a dictionary of the unique payers and the balance for each payer


## How it works
- The program first checks if there are enough arguments (ie. the balance argument is present)
- The program then checks if the input for the balance argument is valid (ie. a positive integer)
- Next, the program checks if the file `transaction.csv` exists in the root directory, and has the correct headers.
- The transactions are read from the file and stored in a list. Then this list is sorted by the timestamp in ascending order (oldest points to be spent first i.e. oldest based on transaction timestamp).
- For each transaction, the program checks the balance and subtracts (or adds if points are negative) corresponding to the transaction. Once the balance reaches zero, the program stops processing transactions.
- The program then prints the dictionary of unique payers and their added balances.
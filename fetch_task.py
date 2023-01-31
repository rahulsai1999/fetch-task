import sys
import csv
from dateutil.parser import parse


def check_csv_file():
    # Check if the CSV file exists and has the correct headers
    try:
        with open("transactions.csv", "r") as csvfile:
            # check if the csv file has correct number of columns
            reader_variable = csv.reader(csvfile, delimiter=",")
            for row in reader_variable:
                if len(row) != 3:
                    print("Invalid number of columns: " + str(row))
                    sys.exit(1)

            # check if the csv file has correct header
            csvfile.seek(0)
            header = next(reader_variable)
            if header[0] != "payer" or header[1] != "points" or header[2] != "timestamp":
                print("Invalid header: " + str(header))
                print("Correct header: payer,points,timestamp")
                sys.exit(1)
            
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def spend_points(balance):
    payers = {}
    transactions = []

    if balance < 0:
        print("Balance cannot be negative")
        sys.exit(1)

    # Read the transactions from the CSV file into a list
    with open("transactions.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            # Skip the header row if it exists
            if row[0] == "payer":
                continue

            # Convert the amount to an integer
            row[1] = int(row[1])

            # Add the transaction to the list
            transactions.append(row)

    # Sort the transactions by timestamp
    transactions.sort(key=lambda x: parse(x[2]))

    for trx in transactions:
        # Check if the balance is greater than 0
        if balance > 0:
            amt = trx[1]

            # Check if the transaction amount is negative
            if amt < 0:
                balance += -amt
                trx[1] = 0

            # Check if the transaction amount is lesser than the balance
            elif amt > 0 and amt <= balance:
                balance -= amt
                trx[1] = 0

            # Check if the transaction amount is greater than the balance
            elif amt > 0 and amt > balance:
                trx[1] -= balance
                balance = 0

        # If the balance is 0, break out of the loop
        else:
            break

    # Print the remaining balance for each payer
    for trx in transactions:
        if trx[0] in payers:
            payers[trx[0]] += trx[1]
        else:
            payers[trx[0]] = trx[1]

    print(payers)


if __name__ == "__main__":
    # Check that the user has provided the correct number of arguments
    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
        print("Usage: python fetch_task.py <points to be spent>")
        sys.exit(1)
    else:
        balance = int(sys.argv[1])
        check_csv_file()
        spend_points(balance)

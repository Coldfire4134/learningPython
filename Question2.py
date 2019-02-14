#! /usr/bin/python
# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as
# following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

account = 0
successfulTransaction = 1
while successfulTransaction:
    transaction = raw_input("Enter Transaction: ").split(" ")
    if transaction[0] == 'D':
        account += int(transaction[1])
    elif transaction[0] == 'W':
        account -= int(transaction[1])
    elif transaction[0] == "quit":
        successfulTransaction = 0
        print(account)

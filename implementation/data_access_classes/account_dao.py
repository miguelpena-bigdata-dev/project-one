from interface.data_access_object_interface import DataAccessObjectInterface
from implementation.data_model_classes.account import Account
import logging
import mysql.connector
from mysql.connector.cursor import MySQLCursor

class AccountDAO(DataAccessObjectInterface):
    """
        This class is meant for retrieving, updating, creating, or deleting accounts from the accounts table.
    """
    def __init__(self):
        self.accounts: list[Account] = [] # used for caching accounts. individual account is returned.
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    def get_all_accounts(self) -> bool:
        """
            This method will cache all accounts from the accounts table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor() 
        query = 'SELECT * FROM accounts;'
        cursor.execute(query)
        self.accounts = []
        for _, row in enumerate(cursor):
            self.accounts.append(Account(row[0], row[3], row[4], row[1], row[2], row[5]))

        logging.info('All accounts retrieved from database.')
        return self.accounts

    def get_account_by_username(self, username: str) -> Account:
        """
            This method will return account associated with provided username. 

            This method should be accessible when logging in. 

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query = f'SELECT * FROM accounts WHERE accountUsername = \'{username}\';'
        cursor.execute(query)
        tmp_account = None
        for _, row in enumerate(cursor):
            tmp_account = Account(int(row[0]), row[3], row[4], row[1], row[2], int(row[5]))


        logging.info('Account retrieved from database.')
        return tmp_account

    def create_account(self, account: Account) -> bool:
        """
            This method will insert specified account into accounts table for saving.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def update_account(self, account: Account) -> bool:
        """
            This method will update the specified account in the accounts table.

            This method can be used to update an account's role.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def delete_account_by_username(self, username: str) -> bool:
        """
            This method will delete an account with the specified username.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

             
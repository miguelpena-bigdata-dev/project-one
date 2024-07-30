from interface.admin_service_interface import AdminServiceInterface
from interface.input_validation_interface import InputValidation

from implementation.data_access_classes.account_dao import AccountDAO
from implementation.data_access_classes.medication_dao import MedicationDAO
from implementation.data_access_classes.orders_dao import OrdersDAO

from implementation.data_model_classes.account import Account
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.shop_order import Shop_Order

from enum import Enum

admin_service_state = Enum('ADMIN_STATE', [
    'INITIAL_STATE',
    'ACCOUNTS_STATE',
    'MEDICATIONS_STATE',
    'ORDERS_STATE',
    'CLOSING_STATE'
])

class AdminService(InputValidation, AdminServiceInterface):
    def __init__(self, current_account):
        self.account_dao: AccountDAO = AccountDAO()
        self.medication_dao: MedicationDAO = MedicationDAO()
        self.orders_dao: OrdersDAO = OrdersDAO()

        self.accounts: list[Account] = self.account_dao.get_all_accounts()
        self.medications: list[Medication] = self.medication_dao.get_all_medications()
        self.shop_orders: list[Shop_Order] = self.orders_dao.get_all_orders()

        self.current_account = current_account

    def set_state(self, state_value: int) -> None:
        ...

    
    def get_state(self) -> int:
        ...
    
    
    def display_accounts(self) -> None:
        ...
    
    
    def display_orders(self) -> None:
        ...

    
    def apply_role(self) -> None:
        ...

        
    def display(self) -> None:
        ...

    
    def run(self) -> None:
        ...
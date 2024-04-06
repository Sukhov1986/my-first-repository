from mypackage.salary import SalaryEmployee


class RepresentativeEmployee(SalaryEmployee):
    def __init__(self, id_employee, name, weekly_salary, commission):
        super().__init__(id_employee, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission

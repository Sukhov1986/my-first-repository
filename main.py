from mypackage.representative import RepresentativeEmployee
from mypackage.salary import SalaryEmployee
from mypackage.hourly import HourlyEmployee
from mypackage.payroll_system import PayrollSystem
salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
representative_employee = RepresentativeEmployee(3, "Николай Хорольский", 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    representative_employee,
])

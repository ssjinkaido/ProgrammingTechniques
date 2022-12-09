
from api import (PayrollSystem, SalaryEmployee, CommissionEmployee, HourlyEmployee)



if __name__ == "__main__":

    payroll_system = PayrollSystem()

    payroll_system.add_employee(SalaryEmployee(payroll_system.generate_identifier(), 'John Smith', 85000))
    payroll_system.add_employee(CommissionEmployee(payroll_system.generate_identifier(), 'Kevin Bacon', 50000, 2500))

    jane_doe = HourlyEmployee(payroll_system.generate_identifier(), 'Jane Doe', 15)
    payroll_system.add_employee(jane_doe)

    jane_doe.hours_worked = 42

    payroll = payroll_system.calculate_pay_month()
    print('Payroll:')
    for p in payroll.items():
        print(f'- for {p[0]}: {p[1]}')
    print(f'total is {payroll_system.calculate_payroll()}')

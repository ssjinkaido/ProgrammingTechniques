from abc import ABC, abstractmethod
class Company(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_invoice(self) -> str:
        pass
    
class CompanyA(Company):
    
    def get_invoice(self) -> str:
        invoice = "some format of invoice for A company"
        return invoice


class CompanyB(Company):
    def get_invoice(self) -> str:
        invoice = "some format of invoice for B company"
        return invoice


class CompanyC(Company):
    def get_invoice(self) -> str:
        invoice = "some format of invoice for C company"
        return invoice


class CompanyD(Company):
    def get_invoice(self) -> str:
        invoice = "error"
        return invoice

class InvoiceService:
    @staticmethod
    def generate_invoice(company: Company) -> str:
        return company.get_invoice()

if __name__ == "__main__":
    print(InvoiceService.generate_invoice(CompanyA('A')))
    print(InvoiceService.generate_invoice(CompanyB('B')))
    print(InvoiceService.generate_invoice(CompanyC('C')))
    print(InvoiceService.generate_invoice(CompanyD('D')))

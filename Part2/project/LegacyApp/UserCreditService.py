import datetime


class UserCreditService:
    pass


class UserCreditServiceClient:
    class __Worker:
        def get_credit_limit(self, name: str, surname: str, dob: datetime.date) -> int:
            return 1500

    def __init__(self) -> None:
        pass

    def __enter__(self):
        return self.__Worker()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass

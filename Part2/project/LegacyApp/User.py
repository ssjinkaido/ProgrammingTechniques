from __future__ import annotations
import datetime
from .Client import IClient
from typing import Optional, Union
from abc import ABC, abstractmethod


class IUser(ABC):
    @property
    @abstractmethod
    def client(self: IUser) -> IClient:
        ...

    @client.setter
    @abstractmethod
    def client(self: IUser, value: IClient) -> None:
        ...

    @property
    @abstractmethod
    def date_of_birth(self: IUser) -> datetime.date:
        ...

    @date_of_birth.setter
    @abstractmethod
    def date_of_birth(self: IUser, value: datetime.date) -> None:
        ...

    @property
    @abstractmethod
    def email_address(self: IUser) -> str:
        ...

    @email_address.setter
    @abstractmethod
    def email_address(self: IUser, value: str) -> None:
        ...

    @property
    @abstractmethod
    def first_name(self: IUser) -> str:
        ...

    @first_name.setter
    @abstractmethod
    def first_name(self, value: str) -> None:
        ...

    @property
    @abstractmethod
    def surname(self: IUser) -> str:
        ...

    @surname.setter
    @abstractmethod
    def surname(self: IUser, value: str) -> None:
        ...

    @property
    @abstractmethod
    def has_credit_limit(self: IUser) -> Union[bool, None]:
        ...

    @has_credit_limit.setter
    @abstractmethod
    def has_credit_limit(self: IUser, value: Union[bool, None]) -> None:
        ...

    @property
    @abstractmethod
    def credit_limit(self: IUser) -> int:
        ...

    @credit_limit.setter
    @abstractmethod
    def credit_limit(self: IUser, value: int) -> None:
        ...


class User(IUser):
    def __init__(
        self: User,
        client: IClient,
        date_of_birth: datetime.date,
        email_address: str,
        first_name: str,
        surname: str,
    ):
        self.__client = client
        self.__date_of_birth = date_of_birth
        self.__email_address = email_address
        self.__first_name = first_name
        self.__surname = surname
        self.__has_credit_limit: Optional[bool] = None
        self.__credit_limit = -1

    @property
    def client(self: User) -> IClient:
        return self.__client

    @client.setter
    def client(self: User, value: IClient) -> None:
        self.__client = value

    @property
    def date_of_birth(self: User) -> datetime.date:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self: User, value: datetime.date) -> None:
        self.__date_of_birth = value

    @property
    def email_address(self: User) -> str:
        return self.__email_address

    @email_address.setter
    def email_address(self: User, value: str) -> None:
        self.__email_address = value

    @property
    def first_name(self: User) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self: User, value: str) -> None:
        self.__first_name = value

    @property
    def surname(self: User) -> str:
        return self.__surname

    @surname.setter
    def surname(self: User, value: str) -> None:
        self.__surname = value

    @property
    def has_credit_limit(self: User) -> Optional[bool]:
        return self.__has_credit_limit

    @has_credit_limit.setter
    def has_credit_limit(self: User, value: Optional[bool] = None) -> None:
        self.__has_credit_limit = value

    @property
    def credit_limit(self: User) -> int:
        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self: User, value: int) -> None:
        self.__credit_limit = value

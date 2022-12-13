from __future__ import annotations
from .ClientStatus import ClientStatus
from abc import ABC, abstractmethod


class IClient(ABC):
    @property
    @abstractmethod
    def id(self: IClient) -> int:
        ...

    @id.setter
    @abstractmethod
    def id(self: IClient, value: int) -> None:
        ...

    @property
    @abstractmethod
    def name(self: IClient) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self: IClient, value: str) -> None:
        ...

    @property
    @abstractmethod
    def status(self: IClient) -> ClientStatus:
        ...

    @status.setter
    @abstractmethod
    def status(self: IClient, value: ClientStatus) -> None:
        ...


class Client(IClient):
    def __init__(
        self: Client,
        id: int = 1,
        name: str = "",
        status: ClientStatus = ClientStatus.UNDEFINED,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: Client) -> int:
        return self.__id

    @id.setter
    def id(self: Client, value: int) -> None:
        self.__id = value

    @property
    def name(self: Client) -> str:
        return self.__name

    @name.setter
    def name(self: Client, value: str) -> None:
        self.__name = value

    @property
    def status(self: Client) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: Client, value: ClientStatus) -> None:
        self.__status = value

from __future__ import annotations
from .ClientStatus import ClientStatus
from abc import ABC, abstractmethod


class IClient(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        ...

    @id.setter
    @abstractmethod
    def id(self, id) -> None:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self, name) -> None:
        ...

    @property
    @abstractmethod
    def status(self) -> ClientStatus:
        ...

    @status.setter
    @abstractmethod
    def status(self, status) -> None:
        ...


class ClientVIP(IClient):
    def __init__(self, id: int = -1, name: str = "", status=ClientStatus.VIP) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status) -> None:
        self.__status = status


class Client(IClient):
    def __init__(self, id: int = -1, name: str = "", status=ClientStatus.VIP) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status) -> None:
        self.__status = status


class ClientIP(IClient):
    def __init__(self, id: int = -1, name: str = "", status=ClientStatus.IP) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status) -> None:
        self.__status = status


class ClientNormal(IClient):
    def __init__(
        self, id: int = -1, name: str = "", status=ClientStatus.NORMAL
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status) -> None:
        self.__status = status


class ClientUndefined(IClient):
    def __init__(
        self, id: int = -1, name: str = "", status=ClientStatus.UNDEFINED
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status) -> None:
        self.__status = status

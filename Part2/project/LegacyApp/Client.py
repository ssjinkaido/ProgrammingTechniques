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


class ClientVIP(IClient):
    def __init__(
        self: ClientVIP,
        id: int = 1,
        name: str = "",
        status: ClientStatus = ClientStatus.VIP,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: ClientVIP) -> int:
        return self.__id

    @id.setter
    def id(self: ClientVIP, value: int) -> None:
        self.__id = value

    @property
    def name(self: ClientVIP) -> str:
        return self.__name

    @name.setter
    def name(self: ClientVIP, value: str) -> None:
        self.__name = value

    @property
    def status(self: ClientVIP) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: ClientVIP, value: ClientStatus) -> None:
        self.__status = value


class ClientIP(IClient):
    def __init__(
        self: ClientIP,
        id: int = 1,
        name: str = "",
        status: ClientStatus = ClientStatus.IP,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: ClientIP) -> int:
        return self.__id

    @id.setter
    def id(self: ClientIP, value: int) -> None:
        self.__id = value

    @property
    def name(self: ClientIP) -> str:
        return self.__name

    @name.setter
    def name(self: ClientIP, value: str) -> None:
        self.__name = value

    @property
    def status(self: ClientIP) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: ClientIP, value: ClientStatus) -> None:
        self.__status = value


class ClientNormal(IClient):
    def __init__(
        self: ClientNormal,
        id: int = 1,
        name: str = "",
        status: ClientStatus = ClientStatus.NORMAL,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: ClientNormal) -> int:
        return self.__id

    @id.setter
    def id(self: ClientNormal, value: int) -> None:
        self.__id = value

    @property
    def name(self: ClientNormal) -> str:
        return self.__name

    @name.setter
    def name(self: ClientNormal, value: str) -> None:
        self.__name = value

    @property
    def status(self: ClientNormal) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: ClientNormal, value: ClientStatus) -> None:
        self.__status = value


class ClientUndefined(IClient):
    def __init__(
        self: ClientUndefined,
        id: int = 1,
        name: str = "",
        status: ClientStatus = ClientStatus.UNDEFINED,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: ClientUndefined) -> int:
        return self.__id

    @id.setter
    def id(self: ClientUndefined, value: int) -> None:
        self.__id = value

    @property
    def name(self: ClientUndefined) -> str:
        return self.__name

    @name.setter
    def name(self: ClientUndefined, value: str) -> None:
        self.__name = value

    @property
    def status(self: ClientUndefined) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: ClientUndefined, value: ClientStatus) -> None:
        self.__status = value

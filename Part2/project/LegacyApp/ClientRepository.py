from __future__ import annotations
from DB.DBAccess import DBAccess, DBTable
from .Client import ClientVIP, ClientIP, ClientNormal, ClientUndefined, IClient
from .ClientStatus import ClientStatus
from .tools import static_initializer
from typing import Type


class ClientFactory:
    @staticmethod
    def get_client(id: int, name: str, status: ClientStatus) -> IClient:
        if status == ClientStatus.VIP:
            return ClientVIP(id, name, status)
        elif status == ClientStatus.IP:
            return ClientIP(id, name, status)
        elif status == ClientStatus.NORMAL:
            return ClientNormal(id, name, status)
        elif status == ClientStatus.UNDEFINED:
            return ClientUndefined(id, name, status)

        return ClientUndefined(id, name, status)


@static_initializer
class ClientRepository:
    __table_name = "clients"
    __table_description = ["name", "status"]
    __table_datatypes = [str, ClientStatus]
    __clients: DBTable

    @classmethod
    def static_init(cls: Type[ClientRepository]) -> None:
        cls.__clients = DBAccess.add_table(
            cls.__table_name, cls.__table_description, cls.__table_datatypes
        )
        cls.__clients.add_entry(1, ["Hugo Lasticot", ClientStatus.VIP])
        cls.__clients.add_entry(2, ["Madeleine Proust", ClientStatus.IP])
        cls.__clients.add_entry(3, ["Huguette Ponsif", ClientStatus.NORMAL])
        cls.__clients.add_entry(4, ["Georges Amphitryon", ClientStatus.VIP])
        cls.__clients.add_entry(5, ["Anibal Dupont", ClientStatus.IP])
        cls.__clients.add_entry(7, ["Georina Dupond", ClientStatus.NORMAL])
        cls.__clients.add_entry(8, ["Victor Elysea", ClientStatus.IP])
        cls.__clients.add_entry(9, ["Céline Quiboit", ClientStatus.NORMAL])
        cls.__clients.add_entry(10, ["Muriel Labeille", ClientStatus.NORMAL])

    @classmethod
    def get_by_id(cls: Type[ClientRepository], id: int) -> IClient:
        entry = cls.__clients.get_entry(id)
        return ClientFactory.get_client(
            id, entry.get_value_by_column("name"), entry.get_value_by_column("status")
        )

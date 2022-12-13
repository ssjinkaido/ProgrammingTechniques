from __future__ import annotations
import datetime

from .Client import IClient
from .ClientStatus import ClientStatus
from .ClientRepository import ClientRepository
from .User import User
from .UserCreditService import UserCreditServiceClient
from .UserDataAccess import UserDataAccess


def get_credit_limit(user: User) -> None:
    with UserCreditServiceClient() as user_credit_service:
        credit_limit = user_credit_service.get_credit_limit(
            user.first_name, user.surname, user.date_of_birth
        )
    if user.client.status == ClientStatus.VIP:
        user.has_credit_limit = False
    elif user.client.status == ClientStatus.IP:
        user.has_credit_limit = True
        user.credit_limit = credit_limit * 2
    else:
        user.has_credit_limit = True
        user.credit_limit = credit_limit


def validate_name(firname: str, surname: str) -> bool:
    if (firname == "") or (surname == ""):
        return False
    return True


def validate_email(email: str) -> bool:
    if ("@" in email) and ("." not in email):
        return False
    return True


def validate_age(dateOfBirth: datetime.date) -> bool:
    now = datetime.datetime.now()
    age = now.year - dateOfBirth.year
    if (now.month < dateOfBirth.month) or (
        (now.month == dateOfBirth.month) and (now.day < dateOfBirth.day)
    ):
        age = age - 1
    if age < 21:
        return False
    return True


def validate_input(
    firname: str, surname: str, email: str, dateOfBirth: datetime.date
) -> bool:
    if not validate_name(firname, surname):
        return False
    if not validate_email(email):
        return False

    if not validate_age(dateOfBirth):
        return False
    return True


def get_client(clientId: int) -> IClient:
    a = ClientRepository()
    client = ClientRepository.get_by_id(clientId)
    return client


def create_user(
    firname: str, surname: str, email: str, dateOfBirth: datetime.date, client: IClient
) -> User:
    user = User(
        client=client,
        date_of_birth=dateOfBirth,
        email_address=email,
        first_name=firname,
        surname=surname,
    )
    return user


def validate_user(user: User) -> bool:
    if user.has_credit_limit and (user.credit_limit < 500):
        return False
    return True


class UserService:

    # THIS METHOD SHOULD STAY STATIC, with same prototype...
    @staticmethod
    def add_user(
        firname: str,
        surname: str,
        email: str,
        dateOfBirth: datetime.date,
        clientId: int,
    ) -> bool:
        # but you may add typing and you should modify its implementation...
        if not validate_input(firname, surname, email, dateOfBirth):
            return False

        client = get_client(clientId)
        user = create_user(firname, surname, email, dateOfBirth, client)
        get_credit_limit(user)
        if not validate_user(user):
            return False
        UserDataAccess.add_user(user)
        return True

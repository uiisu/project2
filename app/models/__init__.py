import datetime
from typing import Union, List

from pydantic import BaseModel, conint, computed_field, field_validator, ValidationInfo


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    """
     Attributes:
        name (str): Имя.
        age (conint): Возраст, не может быть меньше 0 и больше 100.
        message (str, optional): Сообщение, необязательно.
    """
    name: str
    age: conint(ge=0, le=100)
    message: Union[str, None] = None

    @computed_field
    @property
    def adult(self) -> bool:
        """Совершеннолетний. False если age < 18, иначе True"""
        return False if self.age < 18 else True


class Mapping(BaseModel):
    """
     Attributes:
        list_of_ids (List[Union[int, str]]): Список id.
        tags (List[Union[str, None]]): Список тегов.
    """
    list_of_ids: List[Union[int, str]]
    tags: List[Union[str, None]]


class Meta(BaseModel):
    """Использует модель Mapping.

     Attributes:
        last_modification (datetime.date): Дата последнего изменения, должна соответствовать формату "%d/%m/%Y".
        list_of_skills (List[str], optional): Список навыков, необязательно.
    """
    last_modification: datetime.date
    list_of_skills: Union[List[str], None] = None
    mapping: Mapping

    @field_validator("last_modification", mode="before")
    @classmethod
    def date_format(cls, value: str, info: ValidationInfo) -> datetime.date:
        assert isinstance(value, str), info.field_name + " не соответствует формату '%d/%m/%Y'"
        return datetime.datetime.strptime(value, "%d/%m/%Y").date()


class BigJson(BaseModel):
    """Использует модели User и Meta."""
    user: User
    meta: Meta


# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass

from enum import IntEnum
from pydantic import BaseModel, Field
from collections import defaultdict
from typing import Annotated, Optional, DefaultDict

class UserType(IntEnum):
    NO_USER = 1
    EXTRA_USER = 2


class User(BaseModel):
    id: Optional[str]
    name: Optional[str]


class Container(BaseModel):
    mapping: DefaultDict[UserType, Annotated[User, Field(default_factory=User)]] = defaultdict(User)

if __name__ == "__main__":
    test = Container()
    print(test)
    test.mapping[UserType.NO_USER] = User(id="cb", name="Charlie Brown")

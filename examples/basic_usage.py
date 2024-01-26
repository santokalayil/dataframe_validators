from typing import Annotated, TypeAlias
from pydantic import (
    BaseModel,
    root_validator,
    EmailStr,
    Field,
    field_validator,
    conlist,
)

AgeInt: TypeAlias = Annotated[int, Field(strict=False, gt=0)]
# ValidAgeCasted: TypeAlias = Annotated[int, Field(strict=False, gt=0)]
WeightFloat: TypeAlias = Annotated[float, Field(strict=True, ge=15, le=100)]
StudentId: TypeAlias = Annotated[str, Field(strict=False, min_length=6, max_length=6)]
IdStr: TypeAlias = Annotated[str, Field(strict=False, pattern=r"^\d{4}$")]
InterestList: TypeAlias = conlist(item_type=str, min_length=2)  # type: ignore


class Student(BaseModel):
    id: IdStr  # Field(strict=True, pattern=r"^\d{4}$")
    # ^ start of string $ end of string. but it should contain only numbers. len should be 4 digits
    student_id: StudentId
    name: str
    age: AgeInt
    weight: WeightFloat
    email: EmailStr
    interests: InterestList

    class Config:
        use_enum_values = True
        title = "Student Model"
        extra = "allow"
        str_strip_whitespace = True
        # str_to_upper = True
        frozen = True  # mutable

    @field_validator("interests", mode="before")
    def split_interests(cls, value):
        return map(str.upper, value.split(",")) if isinstance(value, str) else value

    # @field_validator("id", mode="after")
    # def convert_id_2_str(cls, value):
    #     return str(value) if isinstance(value, int) else value

    # @field_validator()


s = Student(
    id="4556",
    student_id="HLKEK2",
    name="Santo",
    age="12",
    weight=100,
    email="santokalayil@gmail.com",
    interests="badminton, cHess, coding",  # type: ignore
)
s

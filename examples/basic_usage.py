from pydantic import (
    BaseModel,
    root_validator,
    EmailStr,
    Field,
    confloat,
    conint,
    field_validator,
    constr,
)


class Student(BaseModel):
    id: str = Field(pattern=r"^\d{4}$")
    # ^ start of string $ end of string. but it should contain only numbers. len should be 4 digits
    student_id: constr(strip_whitespace=True, to_upper=True, min_length=6, max_length=6)  # type: ignore
    name: str
    age: conint(ge=12, le=24)  # type: ignore
    weight: confloat(ge=15, le=100)  # type: ignore
    email: EmailStr
    interests: list[str]

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


s = Student(
    id="4556",
    student_id="HLKEK2",
    name="Santo",
    age="12",
    weight=100,
    email="santokalayil@gmail.com",
    interests="badminton, cHess, coding",  # type: ignore
)

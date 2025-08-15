from typing import Annotated

from pydantic import BaseModel, StringConstraints, model_validator


class UserDetails(BaseModel):
    pk: int
    username: str
    email: str
    first_name: str
    last_name: str


class PasswordUpdated(BaseModel):
    detail: str


PasswordType = Annotated[str, StringConstraints(min_length=2, max_length=128, strip_whitespace=True)]


class PasswordChange(BaseModel):
    new_password: PasswordType
    confirm_password: PasswordType

    @model_validator(mode="after")
    def new_password_matches_confirm_password(self):
        if self.new_password != self.confirm_password:
            raise ValueError("The new password does not match the confirm one.")
        return self

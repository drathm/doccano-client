from typing import List, Optional

from pydantic import (
    BaseModel,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
    field_validator,
    model_validator,
)


class Label(BaseModel):
    id: Optional[int] = None
    example: int
    prob: float = 0.0
    manual: bool = False
    user: Optional[int] = None


class Category(Label):
    label: int


class Span(Label):
    label: int
    start_offset: NonNegativeInt
    end_offset: NonNegativeInt

    @model_validator(mode="after")
    def check_start_offset_is_less_than_end_offset(self):
        if self.start_offset >= self.end_offset:
            raise ValueError("start_offset must be less than end_offset.")
        return self

    def to_tuple(self) -> tuple:
        return self.start_offset, self.end_offset, self.label


class Relation(Label):
    from_id: int
    to_id: int
    type: int


class BoundingBox(Label):
    x: NonNegativeFloat
    y: NonNegativeFloat
    width: NonNegativeFloat
    height: NonNegativeFloat
    label: int


class Segment(Label):
    points: List[NonNegativeFloat] = Field(default_factory=list)
    label: int

    @field_validator("points")
    def check_points_length_is_even(cls, points):
        if len(points) % 2 != 0:
            raise ValueError("The length of points must be even.")
        return points


class Text(Label):
    text: str

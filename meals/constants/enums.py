import enum
from ib_common.constants import BaseEnumClass


class MealTypeChoices(BaseEnumClass, enum.Enum):
    BREAKFAST= "BREAKFAST"
    LUNCH= "LUNCH"
    DINNER= "DINNER"


class MealPreferenceTypeChoices(BaseEnumClass, enum.Enum):
    FULL= "FULL"
    HALF= "HALF"
    CUSTOM= "CUSTOM"
    SKIPPED = "SKIPPED"


class AteMealStatusChoices(BaseEnumClass, enum.Enum):
    ATE = "ATE"
    SKIPPED = "SKIPPED"
    NULL = "NULL"


class FoodItemCategoryChoices(BaseEnumClass, enum.Enum):
    RICE = "RICE"
    PANCAKE = "PANCAKE"
    BEVERAGES = "BEVERAGES"


class BaseSizeUnitChoices(BaseEnumClass, enum.Enum):
    KG = "KG"
    PISCES = "PISCES"
    LITTERS = "LITTERS"


class ServingSizeUnitChoices(BaseEnumClass, enum.Enum):
    PISCES = "PISCES"
    LADDLE = "LADDLE"
    GLASS = "GLASS"


import enum
from ib_common.constants import BaseEnumClass


class MealType(BaseEnumClass, enum.Enum):
    BREAKFAST= "BREAKFAST"
    LUNCH= "LUNCH"
    DINNER= "DINNER"


class MealPreferenceType(BaseEnumClass, enum.Enum):
    FULL= "FULL"
    HALF= "HALF"
    CUSTOM= "CUSTOM"
    SKIPPED = "SKIPPED"


class AteMealStatusType(BaseEnumClass, enum.Enum):
    ATE = "ATE"
    SKIPPED = "SKIPPED"
    NULL = "NULL"


class FoodItemCategoryType(BaseEnumClass, enum.Enum):
    RICE = "RICE"
    PANCAKE = "PANCAKE"
    BEVERAGES = "BEVERAGES"


class BaseSizeUnitType(BaseEnumClass, enum.Enum):
    KG = "KG"
    PISCES = "PISCES"
    LITTERS = "LITTERS"


class ServingSizeUnitType(BaseEnumClass, enum.Enum):
    PIECES = "PIECES"
    LADLE = "LADLE"
    GLASS = "GLASS"


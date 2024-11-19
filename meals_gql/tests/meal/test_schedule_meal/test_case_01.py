import pytest

from meals.tests.factories.models import MealFactory, UserFactory, UserMealFactory
from meals_gql.tests.meal.test_get_meal_preference.base_test import GetMealPreferenceTest
from meals_gql.tests.meal.test_schedule_meal.base_test import ScheduleMealTest


@pytest.mark.django_db
class TestCase(ScheduleMealTest):

    USER_ID = "test_user"

    def test_schedule_meal(self, snapshot):
        # Arrange
        meal = MealFactory()
        user = UserFactory(id=self.USER_ID)
        user_meal = UserMealFactory(meal_id=meal.id, user_id=user.id)

        variables ={
              "params": {
                "userId": user.id,
                "mealId": meal.id,
                "mealType": meal.meal_type
              }
            }

        # Act
        self.execute_schema(
            query=self.QUERY,
            variables=variables,
            snapshot=snapshot,
        )
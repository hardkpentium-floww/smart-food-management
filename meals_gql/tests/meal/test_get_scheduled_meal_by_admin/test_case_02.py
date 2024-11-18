import pytest

from meals.tests.factories.models import MealFactory, UserFactory, UserMealFactory
from meals_gql.tests.meal.test_get_scheduled_meal_by_admin.base_test import GetScheduledMealByAdminTest


@pytest.mark.django_db
class TestCase(GetScheduledMealByAdminTest):

    USER_ID = "test_user"

    def test_get_scheduled_meal_by_admin_with_no_meals(self, snapshot):
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
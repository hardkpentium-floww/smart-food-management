import pytest
from datetime import datetime, timedelta

from meals.tests.factories.models import ItemFactory
from meals_gql.tests.item.test_get_items.base_test import GetItemsTest


@pytest.mark.django_db
class TestCase(GetItemsTest):

    USER_ID = "test_user"

    def test_get_items_with_no_items(self, snapshot):
        # Arrange

        # items = ItemFactory.create_batch(5)

        variables ={
              "params": {
                "offset": 0,
                "limit": 5
              }
            }

        # Act
        self.execute_schema(
            query=self.QUERY,
            variables=variables,
            snapshot=snapshot,
        )
from graphql_service.utils.base_test import GraphQLBaseTestCase


class AddMealForUserTest(GraphQLBaseTestCase):
    QUERY = """
    query Query($params: GetMealPreferenceParams!) {
          getMealPreference(params: $params) {
            ... on UserMealPreference {
              mealPreference
            }
          }
        }
    """




from graphql_service.utils.base_test import GraphQLBaseTestCase


class GetScheduledMealByAdminTest(GraphQLBaseTestCase):
    QUERY = """
    query Query($params: GetMealPreferenceParams!) {
          getMealPreference(params: $params) {
            ... on UserMealPreference {
              mealPreference
            }
          }
        }
    """



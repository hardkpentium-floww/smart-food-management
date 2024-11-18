from graphql_service.utils.base_test import GraphQLBaseTestCase


class GetItemsTest(GraphQLBaseTestCase):
    QUERY = """
    query Query($params: GetItemsParams!) {
      getItems(params: $params) {
        ... on Items {
          items {
            id
            name
            category
            baseSizeUnit
            servingSizeUnit
          }
        }
        ... on ItemsNotFound {
          message
        }
      }
    }
    """




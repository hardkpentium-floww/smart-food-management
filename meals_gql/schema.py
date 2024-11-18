import graphene

from graphql_service.utils.logger import log_error
from graphql_service.middlewares import middlewares
from graphql_service import context
from typing import Dict, Sequence
from graphql.error import GraphQLError

from meals_gql.item.resolvers.get_items import resolve_get_items
from meals_gql.item.types.types import GetItemsParams, GetItemsResponse
from meals_gql.meal.mutations.add_meal_for_user import AddMealForUser
from meals_gql.meal.mutations.save_meal_status import SaveMealStatus
from meals_gql.meal.mutations.schedule_meal import ScheduleMeal
from meals_gql.meal.mutations.update_scheduled_meal import UpdateScheduledMeal
from meals_gql.meal.resolvers.get_meal_preference import resolve_get_meal_preference
from meals_gql.meal.resolvers.get_meal_status import resolve_get_meal_status
from meals_gql.meal.resolvers.get_scheduled_meal_by_admin import resolve_get_scheduled_meal_by_admin
from meals_gql.meal.resolvers.get_scheduled_meal_for_user import resolve_get_scheduled_meal_for_user
from meals_gql.meal.types.types import GetScheduledMealByAdminResponse, GetScheduledMealByAdminParams, \
    GetScheduledMealForUserResponse, GetScheduledMealForUserParams, GetMealPreferenceResponse, GetMealPreferenceParams, \
    GetMealStatusResponse, GetMealStatusParams
from meals_gql.user.mutations.update_incampus_status import UpdateIncampusStatus


class Query(graphene.ObjectType):
    get_items = graphene.Field(
        GetItemsResponse,
        params=GetItemsParams(required=True),
        resolver=resolve_get_items
    )

    get_scheduled_meal_by_admin = graphene.Field(
        GetScheduledMealByAdminResponse,
        params=GetScheduledMealByAdminParams(required=True),
        resolver=resolve_get_scheduled_meal_by_admin
    )

    get_scheduled_meal_for_user = graphene.Field(
        GetScheduledMealForUserResponse,
        params=GetScheduledMealForUserParams(required=True),
        resolver=resolve_get_scheduled_meal_for_user
    )

    get_meal_preference = graphene.Field(
        GetMealPreferenceResponse,
        params=GetMealPreferenceParams(required=True),
        resolver=resolve_get_meal_preference
    )

    get_meal_status = graphene.Field(
        GetMealStatusResponse,
        params=GetMealStatusParams(required=True),
        resolver=resolve_get_meal_status
    )




class Mutation(graphene.ObjectType):
    add_meal_for_user = AddMealForUser.Field(required=True)
    schedule_meal = ScheduleMeal.Field(required=True)
    update_incampus_status = UpdateIncampusStatus.Field(required=True)
    save_meal_status = SaveMealStatus.Field(required=True)


schema = graphene.Schema(query=Query, mutation=Mutation)


def execute_graphql_as_sync(query, variables, middleware, context_obj):
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(
        schema.execute_async(
            query,
            variables=variables,
            middleware=middleware,
            context=context_obj,
        )
    )
    loop.close()
    return result


def handle_graphql_errors(errors: Sequence[GraphQLError], operation_name):
    if errors is None:
        return
    try:
        for error in errors:
            _ = log_error(error=error, logger_name=operation_name)
    except Exception:
        pass


def execute_schema(query, variables, user_id):
    result = execute_graphql_as_sync(
        query=query,
        variables=variables,
        middleware=middlewares,
        context_obj=context.get_context(user_id),
    )
    handle_graphql_errors(result.errors, operation_name="Graphene Error")
    return result

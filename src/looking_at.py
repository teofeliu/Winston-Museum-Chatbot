import utils
from models.cohere_model import CohereModel
from navigation.navigation_system import NavigationSystem


class LookingAt:
    def __init__(self, model: CohereModel):
        self.nav = NavigationSystem()
        self.main_model = model

    def handle_looking_at_query(self, query):
        """
        Handles queries asking for directions.

        Steps:
        1. Extract the artwork name from the query.
        2. If the artwork name is not specified, ask the main model for a suggestion.
        3. Call the Directions API with the artwork name.
        4. Handle any errors or cases where directions are not found.
        5. Format the directions in a user-friendly way.
        6. Return the formatted directions.

        :param query: str - The user's query asking for directions.
        :return: str - The response to be given to the user.
        """
        looking_at = self.nav.what_am_i_looking_at(utils.random_position())
        full_query = (
            "The User is referencing artwork they are currently looking at in a query. Reply to the user.\n\n"
            f"User's Query: \"{query}\"\n\n"
            f"\"{looking_at}\"\n\n"
        )
        yield from self.main_model.chat(full_query)
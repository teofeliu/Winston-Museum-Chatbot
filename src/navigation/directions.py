from navigation.navigation_system import NavigationSystem
import logging
from models.cohere_model import CohereModel
from cohere_config import co
import utils


class Directions:
    def __init__(self, model: CohereModel):
        self.nav = NavigationSystem()
        self.main_model = model

    def handle_directions_query(self, query):
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
        artwork = self.main_model.retrieve_painting(query)
        directions = self.nav.get_directions(utils.random_position(), artwork)

        # Construct the response string with proper formatting
        full_query = self.format_directions(directions, query, artwork)

        yield from self.main_model.chat(full_query)

        """
        try:
            artwork_name = self.extract_artwork_name(query) or self.get_artwork_suggestion(
                query)  # if no artwork name is found, we go to the main LLM to suggest an artwork name

            if artwork_name:
                directions = self.call_directions_api(artwork_name)
                if directions:
                    self.format_directions(directions, query)

            # Fallback to the main model if no artwork name found or directions are empty
            self.fallback_to_main_model(query)

        except Exception as e:
            logging.error(f"Error in handle_directions_query: {e}")
            self.fallback_to_main_model(query)
        """

    def fallback_to_main_model(self, query):
        """
        Fallback to the main model for processing the query.

        :param query: str - The user's query.
        :return: str - The response from the main model.
        """
        logging.info(f"Fallback to main model for query: {query}")
        self.main_model(query)

    def extract_artwork_name(self, query):
        """
        Extracts the artwork name from the query.

        This function should be implemented with logic to parse the query and identify the artwork name.

        :param query: str - The user's query.
        :return: str or None - The extracted artwork name or None if not found.
        """
        for artwork in self.artwork_collection:
            if artwork in query.lower():
                return artwork
        return None  # or an appropriate response indicating no artwork was found

    def get_artwork_suggestion(self, query):
        """
        Asks the main model for an artwork suggestion based on the query.

        :param query: str - The user's query.
        :return: str or None - Suggested artwork name or None if no suggestion is made.
        """
        # Call to the main model for artwork suggestion
        pass

    def call_directions_api(self, artwork_name):
        """
        Calls the Directions API to get directions to the specified artwork.

        :param artwork_name: str - The name of the artwork.
        :return: dict or None - The directions data or None if not found.
        """
        # API call logic
        current_position = (1, 1)  # Define or obtain the current position
        directions = self.nav.get_directions(current_position, artwork_name)
        return directions if directions else None

    def format_directions(self, directions, query, artwork):
        """
        Formats the directions into a user-friendly response.

        :param query:
        :param directions: dict - The raw directions data from the API.
        :return: str - Formatted directions.
        """
        full_query = (
            "Task: Determine if the user's query for directions matches the identified artwork in the museum. "
            "If it matches, provide the directions to the artwork. If not, indicate that the artwork is not in the "
            "collection without a reference to Closest Artwork Identified.\n\n"
            f"User's Query: \"{query}\"\n\n"
            f"Closest Artwork Identified: \"{artwork}\"\n\n"
            "Directions to Artwork (use only if relevant): "
            f"\"{directions}\"\n\n"
        )

        print(full_query)

        return full_query

    def retrieve_artwork_doc(self, response):
        pass

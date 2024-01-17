from utils import load_artwork_details


class NavigationSystem:
    def __init__(self):
        # Load artwork details from the utility function
        artwork_details = load_artwork_details()
        self.artworks = {title: details['position'] for title, details in artwork_details.items()}
        self.room_distances = {1: 8, 2: 13, 3: 13}

    def get_directions(self, current_position, destination):
        if destination not in self.artworks:
            return "Destination not found in the museum."

        destination_position = self.artworks[destination]
        directions = []

        current_room, current_orientation = current_position
        destination_room, destination_wall = destination_position

        path_to_destination = self.find_path(current_room, destination_room)
        for next_room in path_to_destination:
            next_room_direction = self.get_direction_to_next_room(current_room, next_room)
            navigate_directions, current_orientation = self.navigate_to_room(current_orientation, next_room_direction, self.room_distances[current_room])
            directions += navigate_directions
            current_room = next_room

        directions += self.locate_artwork_in_room(current_orientation, destination_wall, destination)

        return directions

    def find_path(self, current_room, destination_room):
        if current_room == destination_room:
            return []
        elif current_room == 1 or destination_room == 1:
            return [2, destination_room] if destination_room != 2 else [2]
        else:
            return [destination_room]

    def get_direction_to_next_room(self, current_room, next_room):
        room_connections = {
            1: {2: 3},  # south
            2: {1: 1, 3: 2},  # north, east
            3: {2: 4}  # west
        }
        return room_connections[current_room][next_room]

    def navigate_to_room(self, current_orientation, next_room_direction, steps):
        directions = []
        turn_direction = {
            (1, 3): "Turn around",
            (1, 2): "Turn right",
            (1, 4): "Turn left",
            (3, 1): "Turn around",
            (3, 2): "Turn left",
            (3, 4): "Turn right",
            (2, 4): "Turn around",
            (2, 1): "Turn left",
            (2, 3): "Turn right",
            (4, 2): "Turn around",
            (4, 1): "Turn right",
            (4, 3): "Turn left"
        }

        if current_orientation != next_room_direction:
            directions.append(turn_direction[(current_orientation, next_room_direction)])
            # Update orientation after turn
            current_orientation = self.update_orientation_after_turn(current_orientation, next_room_direction)

        directions.append(f"Go straight {steps} steps")
        return directions, current_orientation

    def update_orientation_after_turn(self, current_orientation, next_room_direction):
        return next_room_direction  # Updated orientation is the direction of the next room

    def locate_artwork_in_room(self, current_orientation, destination_wall, artwork_name):
        if current_orientation == destination_wall:
            return [f"{artwork_name} is in front of you."]
        elif current_orientation - 1 == destination_wall % 4:
            return [f"{artwork_name} is to your left."]
        elif current_orientation % 4 == destination_wall - 1:
            return [f"{artwork_name} is to your right."]
        else:
            return [f"{artwork_name} is behind you."]

    def what_am_i_looking_at(self, current_position):
        current_room, current_orientation = current_position

        # Filter artworks in the current room
        artworks_in_room = {name: wall for name, (room, wall) in self.artworks.items() if room == current_room}

        # Check if the user is facing any artwork directly
        for artwork, wall in artworks_in_room.items():
            if current_orientation == wall:
                return f"User is looking at {artwork}."

        # If not facing an artwork directly, suggest the closest one
        for artwork, wall in artworks_in_room.items():
            if (current_orientation % 4) + 1 == wall:
                return f"{artwork} is to the user's right."
            elif (current_orientation + 1) % 4 == wall:
                return f"{artwork} is to the user's left."
            elif (current_orientation + 2) % 4 == wall:
                return f"{artwork} is behind the user."

        return "There are no artworks in the user's current direction."
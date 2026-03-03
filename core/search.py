class SearchEngine:
    """
    A class to handle voter queries and provide search functionalities.
    """
    def __init__(self, data):
        """
        Initializes the SearchEngine with voter data.
        :param data: A list of voter records where each record is a dictionary.
        """
        self.data = data

    def search_by_name(self, name):
        """
        Searches for voters by their name.
        :param name: The name to search for.
        :return: A list of voter records matching the name.
        """
        return [voter for voter in self.data if name.lower() in voter['name'].lower()]

    def search_by_id(self, voter_id):
        """
        Searches for a voter by their ID.
        :param voter_id: The ID of the voter to search for.
        :return: The voter record if found, else None.
        """
        for voter in self.data:
            if voter['id'] == voter_id:
                return voter
        return None

    def search_by_location(self, location):
        """
        Searches for voters by their location.
        :param location: The location to search for.
        :return: A list of voter records from the specified location.
        """
        return [voter for voter in self.data if location.lower() in voter['location'].lower()]  

import requests

class Trello:
    def __init__(self, api_key, oauth_token):
        assert(api_key)
        assert(api_key != '')
        assert(oauth_token)
        assert(oauth_token != '')

        self.api_key = api_key
        self.api_base = "https://api.trello.com/1"
        self.oauth_token = oauth_token

    def retrieve_json(self, api_path, api_args):
        assert(api_path[0] != '/')
        assert(api_args)

        url = "%s/%s?%s&key=%s&token=%s" %(
            self.api_base, api_path, api_args, self.api_key, self.oauth_token)

        r = requests.get(url)
        r.raise_for_status()
        response = r.json()
        return response

    def get_board(self, board_id):
        # Limit the fields we get to avoid downloading background images, & etc.
        fields = [
            'name',
            'closed',
            'desc',
            'id',
            'idTags',
            'labelNames'
            ]
        return self.retrieve_json("boards/%s" %(board_id), "fields=%s" %(','.join(fields)))

    def get_board_lists(self, board_id):
        return self.retrieve_json("boards/%s/lists" %(board_id), "fields=all")

    def get_list(self, list_id):
        return self.retrieve_json("lists/%s" %(board_id), "fields=all")

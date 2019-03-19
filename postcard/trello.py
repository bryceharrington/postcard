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
        assert(api_path)
        assert(api_path[0] != '/')
        assert(api_args)

        url = "%s/%s?%s&key=%s&token=%s" %(
            self.api_base, api_path, api_args, self.api_key, self.oauth_token)

        r = requests.get(url)
        r.raise_for_status()
        response = r.json()
        return response

    def send_post(self, api_path, api_args, params):
        assert(api_path)
        assert(api_path[0] != '/')

        url = "%s/%s?%s&key=%s&token=%s" %(self.api_base, api_path, api_args, self.api_key, self.oauth_token)
        r = requests.post(url, data=params)
        r.raise_for_status()
        return r.json()

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

    def get_board_lists(self, board_id, sort_by="pos", reverse=False):
        board_lists = self.retrieve_json("boards/%s/lists" %(board_id), "fields=all")
        if len(board_lists) < 2:
            return board_lists
        if sort_by is None:
            return board_lists

        # Sort the list if needed
        assert(sort_by in board_lists[0].keys())
        return sorted(board_lists, key=lambda k: k[sort_by], reverse=reverse)

    def get_list(self, list_id):
        return self.retrieve_json("lists/%s" %(board_id), "fields=all")

    def add_card(self, list_id, name, desc="", pos="top", labels=None):
        # TODO: Verify labels are in the allowed set
        card = {
            'name': name,
            'desc': desc,
            'pos': pos,
            'idList': list_id,
            'idLabels': labels
        }
        response = self.send_post("cards", "idList=%s" %(list_id), card)
        assert(response)
        assert('id' in response.keys())
        return response

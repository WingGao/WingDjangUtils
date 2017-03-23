import simplejson


class JSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        return None

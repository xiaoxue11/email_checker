from werkzeug.routing import BaseConverter


# define re convert
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        super(ReConverter, self).__init__(url_map)
        self.regex = regex


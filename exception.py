class ApiUnauthenticated(Exception):
    def __init__(self, response_status, response_text):
        super(ApiUnauthenticated, self).__init__(response_status)
        self.response_text = response_text


class ApiNotFound(Exception):
    def __init__(self, response_status, response_text):
        super(ApiNotFound, self).__init__(response_status)
        self.response_text = response_text


class ApiFailedException(Exception):
    def __init__(self, response_status, response_text):
        super().__init__(response_status)
        self.response_text = response_text

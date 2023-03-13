class XmlContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.get('Content-Type') == 'application/xml':
            response['Content-Type'] = 'application/xml'

        return response
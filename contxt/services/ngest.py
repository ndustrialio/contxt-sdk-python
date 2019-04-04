from contxt.legacy.services import POST, Service


class NgestService(Service):
    def __init__(self):

        super().__init__(base_url="https://data.ndustrial.io", access_token="none")

    def sendData(self, feedToken, feedKey, data, execute=True):
        return self.execute(
            POST(uri=f"{feedToken}/ngest/{feedKey}")
            .body(data)
            .authorize(False),
            execute=execute,
        )

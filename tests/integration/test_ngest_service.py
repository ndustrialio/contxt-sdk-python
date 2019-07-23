from contxt.services import NgestService


class TestNgestService:
    service = NgestService()
    feed_token = "?"
    feed_key = "?"
    data = {}

    # TODO: how can we test this service without sending real data?
    def test_send_data(self):
        pass
        # response = self.service.send_data(self, feed_token, self.feed_key, self.data)
        # assert response

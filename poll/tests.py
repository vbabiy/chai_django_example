from django.test import TestCase
from chai import Chai
from models import Poll
import models
import datetime


class PollShowTestCase(Chai, TestCase):

    def test_shows_only_visable_poll(self):
        poll = self.mock()

        self.expect(Poll.objects.get).args(id='1').returns(poll)
        self.expect(poll.is_visable).returns(True)
        res = self.client.get("/poll/show/1/")
        self.assert_equals(res.context['poll'], poll)
    
    def test_rediects_if_poll_is_not_visiable(self):
        poll = self.mock()

        self.expect(Poll.objects.get).args(id='1').returns(poll)
        self.expect(poll.is_visable).returns(False)
        res = self.client.get("/poll/show/1/")
        self.assert_equals(res.status_code, 302)

class PollModelTestCase(Chai, TestCase):

    def setUp(self):
        super(PollModelTestCase, self).setUp()
        self.subject = Poll()
    
    def test_is_visable(self):
        now = datetime.datetime.now()

        dt = self.mock()
        mock_dt = self.mock(models, 'datetime')
        self.expect(mock_dt.now).returns(now)
        self.subject.publish_date = now
        assert self.subject.is_visable()
    
    def test_is_not_visable(self):
        now = datetime.datetime.now()

        dt = self.mock()
        mock_dt = self.mock(models, 'datetime')
        self.expect(mock_dt.now).returns(now)
        self.subject.publish_date =  now - datetime.timedelta(days=10)
        assert not self.subject.is_visable()




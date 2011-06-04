"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from chai import Chai
from models import Poll


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





from django.test import TestCase

from timeclock.models import ClockInOut
# Create your tests here.

class ClockInOutTestCase(TestCase):

    def setUp(self):

        self.post = Post.objects.create(

            author=self.user,

            time='testtime',

            date='testdate',

            notes='testnotes',

            options='testoptions'

        )

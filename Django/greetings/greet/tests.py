from django.http import HttpResponse
from django.test import TestCase
from .views import *
import unittest
from django.test.client import RequestFactory


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = daytime(request, 10)
        self.assertEqual(response, 'Good Morning')

    def test_two_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = daytime(request, 16)
        self.assertEqual(response, 'Good Evening')

    def test_three_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = daytime(request, 20)
        self.assertNotEqual(response, "Good Morning")

    def test_four_details(self):
        """Supposed to fail"""
        request = self.factory.get('')
        response = daytime(request, 5)
        self.assertEqual(response, "Good Night")


class ComplexTest(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_one(self):
        """will pass if a file named 'file' exist otherwise fail"""
        request = self.factory.get('')
        response = finput(request, 'file')
        self.assertEqual(response.status_code, 200)

    def test_two(self):
        """Will pass as no file_two exists"""
        request = self.factory.get('')
        response = foutput(request, 'file_two')
        self.assertNotEqual(response,
                            HttpResponse('no such file found'))  # what the function returns, comparing it with response

    def test_three(self):
        """Will fail"""
        request = self.factory.delete('')
        response = delfile(request, 'file_two')
        self.assertEqual(response, HttpResponse('file deleted successfully'))
# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.accounting_document import AccountingDocument  # noqa: E501
from swagger_server.models.bankaccountinfo_body import BankaccountinfoBody  # noqa: E501
from swagger_server.models.bookingsource_body import BookingsourceBody  # noqa: E501
from swagger_server.models.countries_body import CountriesBody  # noqa: E501
from swagger_server.models.hotels_body import HotelsBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.paymentmethods_body import PaymentmethodsBody  # noqa: E501
from swagger_server.models.salesperson_body import SalespersonBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_accountingdocuments_document_id_put(self):
        """Test case for accountingdocuments_document_id_put

        Update Accounting Document
        """
        body = AccountingDocument()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/accountingdocuments/{documentId}'.format(document_id='document_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bank_account_info_post(self):
        """Test case for bank_account_info_post

        Submit Bank Account Information
        """
        body = BankaccountinfoBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/bank-account-info',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_booking_source_post(self):
        """Test case for booking_source_post

        Create Booking Source
        """
        body = BookingsourceBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/booking-source',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_countries_post(self):
        """Test case for countries_post

        Create Country
        """
        body = CountriesBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/countries',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hotels_post(self):
        """Test case for hotels_post

        Create Hotel
        """
        body = HotelsBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/hotels',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_payment_methods_post(self):
        """Test case for payment_methods_post

        Create Payment Method
        """
        body = PaymentmethodsBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/payment-methods',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_salesperson_post(self):
        """Test case for salesperson_post

        Create Salesperson
        """
        body = SalespersonBody()
        response = self.client.open(
            '/Marquardt-Informatik/OIP-API/1.0.0/salesperson',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

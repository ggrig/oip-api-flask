import connexion
import six

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
from swagger_server import util


def accountingdocuments_document_id_put(body, document_id):  # noqa: E501
    """Update Accounting Document

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param document_id: ID of the Accounting Document to update
    :type document_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = AccountingDocument.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def bank_account_info_post(body):  # noqa: E501
    """Submit Bank Account Information

    Submits bank account information to the Online Invoice Portal (OIP). # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = BankaccountinfoBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def booking_source_post(body):  # noqa: E501
    """Create Booking Source

    Creates a new booking source. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = BookingsourceBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def countries_post(body):  # noqa: E501
    """Create Country

    Creates a new country entry. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = CountriesBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hotels_post(body):  # noqa: E501
    """Create Hotel

    Creates a new hotel entry. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = HotelsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def payment_methods_post(body):  # noqa: E501
    """Create Payment Method

    Creates a new payment method entry. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = PaymentmethodsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def salesperson_post(body):  # noqa: E501
    """Create Salesperson

    Creates a new salesperson entry. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = SalespersonBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

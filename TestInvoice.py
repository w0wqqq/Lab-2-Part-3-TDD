import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10,'unit_price': 3.75,'discount': 5},'Notebook': {'qnt': 5,'unit_price': 7.5,
                                                                       'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanFindInvoiceClass(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 1.02

def test_CanCalucateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalPurePrice(products) == 77.31

def totalPurePrice(self, products):
    total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
    return total_pure_price



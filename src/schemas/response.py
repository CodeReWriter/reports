from dataclasses import dataclass, field
from typing import List


@dataclass
class TotalsByPaymentType:
    code: str
    name: str
    totalSum: str

@dataclass
class TotalsByTaxRate:
    type: int
    letter: str
    name: str
    percent: str
    sign: bool
    turnover: str
    sourceSum: str
    sum: str

@dataclass
class TotalsBySale:
    ordersCount: int
    totalPawnOrdersCountIssued: int
    totalPawnOrdersCountReceived: int
    totalSum: str
    totalPawnSumIssued: str
    totalPawnSumReceived: str
    totalDiscountSum: str
    totalsByPaymentType: List[TotalsByPaymentType]
    totalsByTaxRate: List[TotalsByTaxRate]

@dataclass
class TotalsByReturn:
    ordersCount: int
    totalPawnOrdersCountIssued: int
    totalPawnOrdersCountReceived: int
    totalSum: str
    totalPawnSumIssued: str
    totalPawnSumReceived: str
    totalDiscountSum: str
    totalsByPaymentType: List[TotalsByPaymentType] = field(default_factory=list)
    totalsByTaxRate: List[TotalsByTaxRate] = field(default_factory=list)

@dataclass
class CashTotals:
    ordersCount: int
    totalSum: str
    totalCommissionSum: str

@dataclass
class Data:
    startOfPeriod: str
    endOfPeriod: str
    shiftsCount: int
    companyName: str
    pointName: str
    pointAddress: str
    tin: str
    cashierName: str
    serviceInputTotal: str
    serviceOutputTotal: str
    totalsBySale: TotalsBySale
    totalsByReturn: TotalsByReturn
    cashTotals: CashTotals
    dateTime: str

@dataclass
class ReportResponse:
    success: bool
    data: Data
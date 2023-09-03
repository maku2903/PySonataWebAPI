from enum import (
    Enum,
    auto,
)
from pydantic import (
    BaseModel,
)
from typing import (
    List,
    Optional,
)
class enumPaymentSubjectType(Enum):
    Contractor: 0
    PaymentRegistry: 104
    Employee: 106
    Office: 107

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFKDocumentCharacter(Enum):
    DP: 1
    FVZ: 2
    FVS: 3
    RUZ: 4
    RUS: 5
    RK: 6
    RK_Old: 7
    DEX: 8
    DIM: 9
    FKZ: 10
    FKS: 11
    RKZ: 12
    RKS: 13
    WB: 14
    RZL: 15
    FWN: 16
    WNT: 17
    WDT: 18
    PWN: 19
    FWV: 20
    RKW: 21
    FWZ: 22
    FWS: 23
    KFWZ: 24
    KFWS: 25
    DS: 26
    WBW: 27

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceCalculationMethod(Enum):
    Handel: 0
    Algorithm: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSideType(Enum):
    Debit: 0
    Credit: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumCurrencyRateType(Enum):
    WithoutCurrency: 0
    Purchase: 1
    Sale: 2
    Mean: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSplitOpposingAccountType(Enum):
    Debit_SplitInCreaditWithMultipleOpposingAccounts: 99
    Debit_SplitInDebitWithSingleOpposingAccount: 101
    Debit_WithoutSplitWithSingleOpposingAccount: 103
    Credit_SplitInDebitWithMultipleOpposingAccounts: 199
    Credit_SplitInCreditWithSingleOpposingAccount: 201
    Credit_WithoutSplitWithSingleOpposingAccount: 203

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumReservationPositionType(Enum):
    Unknown: 0
    SaleDocument: 18
    WarehouseDocument: 37
    ForeignOrder: 30

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumProductType(Enum):
    Article: 0
    Service: 1
    Kit: 2
    Set: 3
    ServiceProfit: 4

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumVatRegisterKind(Enum):
    Purchase_Standard: 100
    Purchase_FixedAssets: 101
    Purchase_Special1: 102
    Purchase_Special2: 103
    Purchase_NonDeductibleVat: 104
    Purchase_LowerVat: 106
    Purchase_HigherVat: 107
    Sale_Standard: 200
    Sale_WithCustomizablePeriod: 210
    Sale_ProductDeliveryWhereBuyerIsTaxPayer: 203
    Sale_NonDeductibleVat: 204
    Sale_ProductDeliveryAndServiceOutsideOfCountry: 205
    Sale_LowerVat: 206
    Sale_HigherVat: 207
    Import_Standard: 300
    Import_FixedAssets: 301
    Import_Service: 302
    Import_ProductDeliveryWhereBuyerIsTaxPayer: 303
    Import_ProductDeliveryWithSimplifiedCustomProcedure: 304
    Export_Standard: 400
    Export_NonDeductibleVat: 404
    Export_ProductDeliveryAndServiceOutsideOfCountry: 405

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumReservationType(Enum):
    Manual: 1
    Automatic: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceKind(Enum):
    Undefined: 0
    Gross: 1
    Net: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPrintParameterNotSettledDocuments(Enum):
    DoNotPrint: 0
    PrintForIssueDate: 1
    PrintForPrintDate: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSplitType(Enum):
    None_: 0
    SplitInDebit: 1
    SplitInCredit: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSubjectType(Enum):
    Empty_Null: -1
    Other: 0
    Employees: 1
    Contractors: 2
    Accounts: 3
    Offices: 4
    Currencies: 5
    IncidentalContractors: 8
    Countries: 9
    Dictionaries: 99

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceRounding(Enum):
    _0_0001: 6
    _0_001: 5
    _0_01: 0
    _0_10: 1
    _1_00: 2
    _10_00: 3
    _100_00: 4

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumJPK_V7ProductGroup(Enum):
    None_: 0
    GTU_01: 1
    GTU_02: 2
    GTU_03: 4
    GTU_04: 8
    GTU_05: 16
    GTU_06: 32
    GTU_07: 64
    GTU_08: 128
    GTU_09: 256
    GTU_10: 512
    GTU_11: 1024
    GTU_12: 2048
    GTU_13: 4096

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumParallelType(Enum):
    Undefined: 0
    Parallel: 1
    StandardWithOnRequestParallel: 2
    StandardWithAutomaticParallel: 4
    ParallelOnDebit: 8
    ParallelOnCredit: 16
    OnRequestParallel: 32
    StuckParallel: 64

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceFactorType(Enum):
    Discount: 0
    Price: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumCalculationState(Enum):
    All: 0
    Settled: 1
    NotSettled: 2
    NotSettledBeforeMaturityTerm: 3
    NotSettledAfterMaturityTerm: 4
    NotSettledWithoutMaturityTerm: 5

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumIncrementalSyncModifyType(Enum):
    InsertOrUpdate: 1
    Delete: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumDocumentStatus(Enum):
    Other: 0
    New: 4
    Partial: 8
    Realized: 16
    Closed: 32

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSettlementMethod(Enum):
    FIFO: 0
    LIFO: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceType(Enum):
    Undefined: 0
    PriceA: 1
    PriceB: 2
    PriceC: 3
    PriceD: 4
    Price_Individual: 5
    Price_Purchase: 6
    Price_Purchase_In_Currency: 7
    Price_Base: 8
    Other: 9
    Duty: 10
    Excise: 11
    Quantitative_Discount: 12
    Sale_Currency_Exchange_Rate: 13
    Purchase_Currency_Exchange_Rate: 14
    Contractor_Discount: 15
    PriceE: 16
    PriceF: 17
    PriceG: 18
    PriceH: 19
    PriceI: 20
    PriceJ: 21
    PriceK: 22
    PriceL: 23
    PriceM: 24
    PriceN: 25
    PriceO: 26
    PriceP: 27
    PriceQ: 28
    PriceR: 29
    PriceS: 30
    PriceT: 31

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSettlementType(Enum):
    Due: 0
    Obligation: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPaymentRegistryType(Enum):
    Cash: 0
    Bank: 1
    Other: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumRDFStatus(Enum):
    NoInvoice: 0
    InvoiceNotPrinted: 1
    InvoicePrinted: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumJPKDocumentKind(Enum):
    None_: 0
    VAT: 1
    KOREKTA: 2
    ZAL: 3
    PZ: 21
    WZ: 22
    RW: 23
    MM: 24

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumIndividualDiscountSubjectType(Enum):
    Contractor: 0
    ContractorKind: 1
    Product: 2
    ProductKind: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumManualSettledState(Enum):
    Automatic: 0
    Manual_NotSettled: 1
    Manual_Settled: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumOrderByType(Enum):
    Desc: 0
    Asc: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumReservationMode(Enum):
    MadeByUser: 1
    MadeByProgram: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceListConnectionType(Enum):
    Individual: 1
    LinkedWithCardIndexAndIndividualDiscounts: 2
    LinkedWithCardIndexAndIndividualDiscountsAndOtherPriceLists: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceRecalculateType(Enum):
    PurchasePriceAndBasePriceAreNotAgreed: 0
    AutomaticallyAtEveryPurchasePriceChange: 1
    AutomaticallyWhenPurchasePriceIsHigherThanBasePrice: 2
    ManuallyAtEveryPurchasePriceChange: 3
    ManuallyWhenPurchasePriceIsHigherThanBasePrice: 4

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFilterSqlCriteriaMode(Enum):
    Within: 0
    Equals: 1
    Like: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumJPK_V7DocumentAttribute(Enum):
    None_: 0
    RO: 1
    WEW: 2
    FP: 4
    MK: 8
    VAT_RR: 16
    SW: 32
    EE: 64
    TP: 128
    TT_WNT: 256
    TT_D: 512
    MR_T: 1024
    MR_UZ: 2048
    I_42: 4096
    I_63: 8192
    B_SPV: 16384
    B_SPV_DOSTAWA: 32768
    B_MPV_PROWIZJA: 65536
    MPP: 131072
    IMP: 262144
    IED: 524288
    WSTO_EE: 1048576

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPriceParameter(Enum):
    Profit: 1
    Markup: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumVatRegisterType(Enum):
    Purchase: 1
    Sale: 2
    Import: 3
    Export: 4

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFKDocumentMessageType(Enum):
    Comments: 0
    Warning: 1
    Error: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPrintParameterDocumentStatus(Enum):
    Automatic: 0
    Original: 1
    Copy: 2
    Original_Copy: 3
    Empty: 4
    Custom: 5

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumYearClosingStatus(Enum):
    Active: 0
    Closed: 1
    Aprroved: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumDefaultUnitOfMeasurementKind(Enum):
    None_: 0
    Record: 1
    Additional1: 2
    Additional2: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFiscalizationStatus(Enum):
    NonFiscal: 0
    ToFiscalization: 1
    Fiscializated: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumCalculationType(Enum):
    Due: 0
    Obligation: 1
    All: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumVatRegisterTypeABCD(Enum):
    A: 1
    B: 2
    C: 3
    D: 4

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSalePriceType(Enum):
    Undefined: 0
    PriceA: 1
    PriceB: 2
    PriceC: 3
    PriceD: 4
    PriceE: 16
    PriceF: 17
    PriceG: 18
    PriceH: 19
    PriceI: 20
    PriceJ: 21
    PriceK: 22
    PriceL: 23
    PriceM: 24
    PriceN: 25
    PriceO: 26
    PriceP: 27
    PriceQ: 28
    PriceR: 29
    PriceS: 30
    PriceT: 31

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumRecordDecsriptionKind(Enum):
    FromDocument: 0
    FromRecord: 1
    FromFirstRecord: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumDocumentReservationType(Enum):
    None_: 0
    Qunatity: 1
    IndicationDelivery: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumSplitValueType(Enum):
    Value: 0
    Percent: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFilterCriteriaMode(Enum):
    Within: 0
    StartsWith: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumFKSplitPaymentType(Enum):
    None_: 0
    SplitPayment: 1
    VoluntarySplitPayment: 3
    TaxPayerRegister: 4
    TaxPayerRegister_SplitPayment: 5
    TaxPayerRegister_VoluntarySplitPayment: 7

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPaymentType(Enum):
    Income: 0
    Expenditure: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumTransactionInterestType(Enum):
    None_: 0
    Statutory: 1
    FixedRate: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumDocumentCharacter(Enum):
    ZMO: 86
    ZWO: 103
    ZMW: 87
    ZWW: 104
    NAL: 58
    ZOB: 59
    KP: 60
    KW: 61
    BP: 62
    BW: 63
    IP: 64
    IW: 65
    TRPlus: 66
    TRMinus: 67
    FVZ: 68
    RUZ: 70
    DIM: 72
    ZRZ: 97
    FVR: 99
    FVM: 106
    WNT: 115
    FWZ: 138
    FZK: 69
    FWZK: 139
    RKZ: 71
    DMK: 73
    ZRK: 98
    FRK: 100
    FMK: 107
    WNK: 121
    DEX: 46
    PAR: 50
    SRS: 79
    RUS: 42
    REX: 126
    FVSM: 124
    FVS: 40
    FVW: 101
    SKO: 134
    SKW: 150
    WDT: 114
    SZA: 136
    SZW: 152
    DXK: 45
    PRK: 51
    SRK: 80
    RKS: 43
    RXK: 127
    FVMK: 125
    FKS: 41
    FKW: 102
    SKK: 135
    SKWK: 151
    WKS: 118
    WDTK: 120
    PW: 74
    RW: 76
    WZ: 78
    PZ: 89
    MMPlus: 82
    MMMinus: 84
    PWK: 75
    RWK: 77
    WZK: 88
    MKPlus: 83
    MKMinus: 85
    PZK: 81
    KWM: 90
    FZS: 108
    ZKS: 112
    FZZ: 128
    ZKZ: 113
    KZS: 109
    ZSK: 122
    KZZ: 111
    ZZK: 123
    FWS: 116
    FWEZ: 117
    WKZ: 119
    WDP: 129
    WPK: 130
    PZP: 131
    PPK: 132

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumDocumentSource(Enum):
    AccountingBooks: 0
    Buffer: 1
    Schemes: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumPrintParameterOperationDateFormat(Enum):
    OperationDate: 0
    OperationPeriod: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumContractorType(Enum):
    Firm: 0
    PersonFirm: 1
    Person: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumVatRateType(Enum):
    Unknown: -1
    Other: 0
    Zero: 3
    Exempt: 4
    NoSubjectTo: 5
    Basic: 10
    Reduced11: 11
    Reduced12: 12
    SuperReduced: 13
    Intermediate: 14

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumContractorSplitPayment(Enum):
    None_: 0
    Blocked: 1
    Required: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumReservationKind(Enum):
    FIFO_IndicationDelivery: 0
    FIFO_Quantity: 1
    LIFO_IndicationDelivery: 2
    LIFO_Quantity: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumReservationDocumentType(Enum):
    Unknown: 0
    SaleDocument: 16
    WarehouseDocument: 33
    ForeignOrder: 45

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumCancelationType(Enum):
    Other: 0
    Standard: 1
    ImportedFromArchive: 2
    CanceledReceipt: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class enumVatRegisterPeriodType(Enum):
    SpecificPeriod: 0
    Pending: 1
    PeriodSetByPayment: 2
    PeriodSetByMaturityTerm: 3

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()

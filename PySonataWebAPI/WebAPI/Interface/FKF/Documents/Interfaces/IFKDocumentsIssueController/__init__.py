from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    Document,
    DocumentMessage,
)
from ...ViewModels.Issue.Custom import (
    DocumentIssue as CustomDocumentIssue,
)
from ...ViewModels.Issue.PurchaseInvoice import (
    DocumentIssue as PurchaseInvoiceDocumentIssue,
)
from ...ViewModels.Issue.SaleInvoice import (
    DocumentIssue as SaleInvoiceDocumentIssue,
)
from ...ViewModels.Issue.Simple import (
    DocumentIssue as SimpleDocumentIssue,
)

from datetime import (
    datetime,
)
from pydantic import (
    BaseModel,
)
from typing import (
    Type,
    TypeVar,
    Optional,
    Tuple,
    List,
    Union,
    overload,
)


async def AddNew(
    api: AsyncAPI,
    documentIssue: Union[CustomDocumentIssue, PurchaseInvoiceDocumentIssue, SaleInvoiceDocumentIssue, SimpleDocumentIssue] = Unset()
) -> IHttpActionResult[Document]:
    match documentIssue:
        case CustomDocumentIssue():
            path = "/api/FKDocumentsIssue/NewCustom"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Document)
            return result
        case PurchaseInvoiceDocumentIssue():
            path = "/api/FKDocumentsIssue/NewPurchaseInvoice"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Document)
            return result
        case SimpleDocumentIssue():
            path = "/api/FKDocumentsIssue/NewSimple"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Document)
            return result
        case SaleInvoiceDocumentIssue():
            path = "/api/FKDocumentsIssue/NewSaleInvoice"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Document)
            return result


async def Validate(
    api: AsyncAPI,
    documentIssue: Union[CustomDocumentIssue, PurchaseInvoiceDocumentIssue, SaleInvoiceDocumentIssue, SimpleDocumentIssue] = Unset()
) -> IHttpActionResult[List[DocumentMessage]]:
    match documentIssue:
        case PurchaseInvoiceDocumentIssue():
            path = "/api/FKDocumentsIssue/NewCustom"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentMessage])
            return result
        case SimpleDocumentIssue():
            path = "/api/FKDocumentsIssue/NewSimple"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentMessage])
            return result
        case CustomDocumentIssue():
            path = "/api/FKDocumentsIssue/NewSaleInvoice"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentMessage])
            return result
        case SaleInvoiceDocumentIssue():
            path = "/api/FKDocumentsIssue/NewPurchaseInvoice"
            params = dict()
            data = documentIssue.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentMessage])
            return result

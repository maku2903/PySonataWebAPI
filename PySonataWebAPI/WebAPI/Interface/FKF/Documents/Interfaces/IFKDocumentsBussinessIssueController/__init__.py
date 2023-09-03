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
)
from ...ViewModels.Issue.Business import (
    BusinessDocumentIssue,
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


async def NewPurchaseInvoice(
    api: AsyncAPI, documentIssue: BusinessDocumentIssue
) -> IHttpActionResult[Document]:
    """
    ['Document']
    :param api:
    :type api: AsyncAPI
    :param documentIssue:
    :type documentIssue: BusinessDocumentIssue
    :returns: Document
    :rtype: Document
    """
    path = "/api/FKDocumentsBussinessIssue/NewPurchaseInvoice"
    params = dict()
    data = documentIssue.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Document)
    return result


async def NewPurchaseInvoiceCorrection(
    api: AsyncAPI, documentIssue: BusinessDocumentIssue
) -> IHttpActionResult[Document]:
    """
    ['Document']
    :param api:
    :type api: AsyncAPI
    :param documentIssue:
    :type documentIssue: BusinessDocumentIssue
    :returns: Document
    :rtype: Document
    """
    path = "/api/FKDocumentsBussinessIssue/NewPurchaseInvoiceCorrection"
    params = dict()
    data = documentIssue.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Document)
    return result


async def NewSaleInvoice(
    api: AsyncAPI, documentIssue: BusinessDocumentIssue
) -> IHttpActionResult[Document]:
    """
    ['Document']
    :param api:
    :type api: AsyncAPI
    :param documentIssue:
    :type documentIssue: BusinessDocumentIssue
    :returns: Document
    :rtype: Document
    """
    path = "/api/FKDocumentsBussinessIssue/NewSaleInvoice"
    params = dict()
    data = documentIssue.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Document)
    return result


async def NewSaleInvoiceCorrection(
    api: AsyncAPI, documentIssue: BusinessDocumentIssue
) -> IHttpActionResult[Document]:
    """
    ['Document']
    :param api:
    :type api: AsyncAPI
    :param documentIssue:
    :type documentIssue: BusinessDocumentIssue
    :returns: Document
    :rtype: Document
    """
    path = "/api/FKDocumentsBussinessIssue/NewSaleInvoiceCorrection"
    params = dict()
    data = documentIssue.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Document)
    return result

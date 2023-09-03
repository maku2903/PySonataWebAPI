from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels.Rdf import (
    RdfDocumentAttachment,
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
    api: AsyncAPI, documentId: int, newDocumentAttachment: RdfDocumentAttachment, yearId: int
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param documentId:
    :type documentId: int
    :param newDocumentAttachment:
    :type newDocumentAttachment: RdfDocumentAttachment
    :param yearId:
    :type yearId: int
    :returns: 
    :rtype: 
    """
    path = "/api/FKDocumentLinks/AddNew"
    params = dict()
    params["documentId"] = documentId

    data = newDocumentAttachment.model_dump_json(exclude_unset=True)
    params["yearId"] = yearId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def Update(
    api: AsyncAPI, documentId: int, newDocumentAttachment: RdfDocumentAttachment, yearId: int
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param documentId:
    :type documentId: int
    :param newDocumentAttachment:
    :type newDocumentAttachment: RdfDocumentAttachment
    :param yearId:
    :type yearId: int
    :returns: 
    :rtype: 
    """
    path = "/api/FKDocumentAttachments/Update"
    params = dict()
    params["documentId"] = documentId

    data = newDocumentAttachment.model_dump_json(exclude_unset=True)
    params["yearId"] = yearId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result

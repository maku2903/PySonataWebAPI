from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    CharacterRelation,
    DocumentType,
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


async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[DocumentType]:
    """
    ['DocumentType']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: DocumentType
    :rtype: DocumentType
    """
    path = "/api/DocumentTypes"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, DocumentType)
    return result


async def GetByCharacter(
    api: AsyncAPI, documentCharacter: int
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :param documentCharacter:
    :type documentCharacter: int
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/DocumentTypes"
    params = dict()
    data = None
    params["documentCharacter"] = documentCharacter

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetCharacterRelations(
    api: AsyncAPI, 
) -> IHttpActionResult[List[CharacterRelation]]:
    """
    ['List[CharacterRelation]']
    :param api:
    :type api: AsyncAPI
    :returns: List[CharacterRelation]
    :rtype: List[CharacterRelation]
    """
    path = "/api/DocumentTypes/CharacterRelations"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CharacterRelation])
    return result

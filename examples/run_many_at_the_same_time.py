import asyncio
from PySonataWebAPI import WebAPI
from PySonataWebAPI.WebAPI.Client import IHttpActionResult
from typing import Any, Tuple


async def main():
    api = WebAPI.Client.AsyncAPI(
        domain='<< your api server ip >>',  # f.e. 192.168.1.100:9000
        https=False,
        device_name='dev',
        key='<< your guid access key >>'
    )

    error = None

    async with api:
        try:
            tasks = [
                WebAPI.Interface.Interfaces.IPingController.Get(api),
                WebAPI.Interface.Products.Interfaces.IProductsController.Get(api),
                WebAPI.Interface.Products.Interfaces.IProductsController.Get(api, id=98033),
                WebAPI.Interface.Orders.Interfaces.IOrdersController.Get(api),
                WebAPI.Interface.OwnOrders.Interfaces.IOwnOrdersController.Get(api),
                WebAPI.Interface.Contractors.Interfaces.IContractorsController.Get(api),
                WebAPI.Interface.Purchases.Interfaces.IPurchasesController.Get(api),
                WebAPI.Interface.Purchases.Interfaces.IPurchasesController.GetKinds(api)
            ]
            results: Tuple[IHttpActionResult[Any]] = await asyncio.gather(*tasks)

            print('results: ', [res.model for res in results])

        except Exception as e:
            error = e

    if error:
        raise error

if __name__ == '__main__':
    asyncio.run(main())

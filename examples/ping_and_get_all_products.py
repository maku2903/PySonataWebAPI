import asyncio
from PySonataWebAPI import WebAPI


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
            # Perform an example GET request
            response = await WebAPI.Interface.Interfaces.IPingController.Get(api)
            response = response.get_response()
            # Do something with the response
            if response.ok:
                text = await response.text()
                print("Received Response:", text)
            else:
                print(f"Received an error from the server: {response.status}")

            products_data = await WebAPI.Interface.Products.Interfaces.IProductsController.Get(api=api)
            response = products_data.get_response()
            # Do something with the response
            if response.ok:
                text = await response.text()
                print("Received Response:", text)
                models = products_data.get_model()
                print(models)
            else:
                print(f"Received an error from the server: {response.status}")
        except Exception as e:
            error = e
    if error:
        raise error

if __name__ == '__main__':
    asyncio.run(main())

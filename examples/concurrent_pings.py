import asyncio
from PySonataWebAPI import WebAPI
from PySonataWebAPI.WebAPI.Client import AsyncAPI


async def ping_api(api, index, received_order):
    print(f"Call no. {index}")
    response = await WebAPI.Interface.Interfaces.IPingController.Get(api)
    response = response.get_response()
    if response.ok:
        text = await response.text()
        print(f"Received Response for call {index}: {text}")
        received_order.append(index)
    else:
        print(f"Received an error from the server for call {index}: {response.status}")


async def main():
    api = AsyncAPI(
        domain='<< your api server ip >>',  # f.e. 192.168.1.100:9000
        https=False,
        device_name='dev',
        key='<< your guid access key >>'
    )

    error = None
    received_order = []

    async with api:
        try:
            tasks = [ping_api(api, i, received_order) for i in range(1, 1000)]
            await asyncio.gather(*tasks)

            print("Order in which calls were received:", received_order)

        except Exception as e:
            error = e

    if error:
        raise error

    in_order = all(a <= b for a, b in zip(received_order, received_order[1:]))
    if in_order:
        print("received pings in order")
    else:
        print("received pings not in order")

if __name__ == '__main__':
    asyncio.run(main())

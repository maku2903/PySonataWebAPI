# PySonataWebAPI

Unofficial Symfonia WebAPI asynchronous client for python3.10+

Client is object oriented with model validation.

## Why?

Proof of concept, lack of such client and attempt to utilise my current knowledge and experience of working with `Symfonia WebAPI` server.
Incoming python integration to MS Excel is also an answer.
Also, the project has grown so much that I had to start versioning it.

Please keep in mind that this project is still in `work in progress` stage.

## Installation

Install using `pip install -U PySonataWebAPI`

## Disclaimers

This client hugely depends on typehints in official documentation of WebAPI server.
It tries to reflect models and methods from documentation for easier method use 
and easier to perform data manipulation but
there are some limitations due to documentation inaccuracies and C# / Python environment differences.
Known documentation inaccuracies are fixed on this client side.
Especially this refers to undocumented enum values (f.e. for reservation types) and
for nullable property of models fields.

Every enumeration has undocumented value handling to prevent annoying validation errors.
Example:
```python
from PySonataWebAPI import WebAPI

unknown_reservation_type = WebAPI.Interface.Enums.enumReservationType(3)
print(unknown_reservation_type)
```
Output:
```commandline
enumReservationType.Undocumented
```

Please keep in mind that this code is 99.9% generated by using script and with very little developer involvement.
Script has ability to patch known issues on model and method sides.

But they must be known before that...

## Server bugs

I have caught many errors using WebAPI server. I tried to fix some of them with patching mechanism I have designed.

### Patched models

 - WebAPI.Interface.Products.ViewModels.ProductListElement property VatRate can be None
 - WebAPI.Interface.Common.ViewModels.Dimension property DictionaryValue can be None
 - WebAPI.Interface.Products.ViewModels.Product property SetElements can be None
 - WebAPI.Interface.Products.ViewModels.ProductBarcode property Barcode can be None

### Known models bugs (not patched)

 to be written

### Patched methods

none

### Known method bugs (not patched)

to be written

## Example usage (simple exaple)

```python
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
                models = products_data.model
                print(models)
            else:
                raise Exception(f"Received an error from the server: {response.status}")
        except Exception as e:
            error = e
    if error:
        raise error

if __name__ == '__main__':
    asyncio.run(main())
```

## Models usage

to be explained...

## TODOs

 - support not settable model properties 
 - support SSL certs
 - support for selective method return type based on input parameter value
 - code autobuild and auto-versioning for past, current and upcoming WebAPI server versions

## Licence

### Project Licence

 - This project is licensed under the `Apache License 2.0` licence. A copy of the license is included in this repository.

### Third-Party Libraries

 - This project uses `Pydantic`, which is licensed under the `MIT License`. A copy of the license is included in this repository.
 - This project uses `aiohttp`, which is licensed under the `Apache License 2.0`. A copy of the license is included in this repository.

# Asyncrhonous wrapper for proxycheck.io API
[Proxycheck.io API Documentation](https://proxycheck.io/api/) | [Query Flags](https://proxycheck.io/api/#query_flags)

# Install
pip3 install git+https://github.com/MertYakupBaykan/aioproxyio.git

# Example
```python
import asyncio
import aioproxyio

async def example():

  test = proxy_io()

  print(await test.get(ip="37.60.48.2", asn=True, vpn=True))

  await test.session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()

```

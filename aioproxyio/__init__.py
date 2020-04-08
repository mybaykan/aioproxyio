import urllib
import aiohttp
import asyncio

class proxy_io:
    api_route = "https://proxycheck.io/v2/{}/"

    def __init__(self, api_key = False, session = False):
        """
        api_key,   NOT REQUIRED | proxycheck.io API Key.
        session,   NOT REQUIRED | aiogttp Session.
        """
        if api_key:
            self.api_route += "?key={}&".format(api_key)
        else:
            self.api_route += "?"


        self.loop = asyncio.get_event_loop()

        if session:
            self.session = session
        else :
            self.session = aiohttp.ClientSession(loop=self.loop)


    async def get(self, ip: str, flags: dict):
        """
        gets infomation about the passed IP
        ip,            REQUIRED     | Device IP.
        parameters,    NOT REQUIRED | proxycheck.io Flags.
        """
        api_request_link =  self.api_route.format(ip)

        if flags:
            for flag in flags:
                flags[flag] = int(flags[flag] == True)

        async with self.session.get(api_request_link, params=flags) as resp:

            if resp.status == 200:
                data = await resp.json()

                if not data.get("status"):
                    return False

                if data["status"] != "ok":
                    return False

                if data[ip].get("proxy"):
                    data[ip]["proxy"] = data[ip]["proxy"] == "yes"

                return data[ip]

            else:
                return False

if __name__ == "__main__":
    async def example():

        test = proxy_io()

        print(await test.get(ip="37.60.48.2",flags={'asn':True,'vpn':True}))

        await test.session.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
    loop.close()

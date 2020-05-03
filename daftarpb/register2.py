from goodbyecaptcha.solver import Solver
import requests
import json
import time
import sys

pageurl = "https://www.pointblank.id/member/signup"
sitekey = "6LedY2IUAAAAAK-55KzamdPZeFh6fbZnDcRhzDLE"

proxy = sys.argv[1]
method = 'images'  # 'audio'
args = ["--timeout 5"]
options = {"ignoreHTTPSErrors": True, "method": method, "args": args}


class MySolver(Solver):

    data = None

    def __init__(self, pageurl, sitekey, loop=None, proxy=None, proxy_auth=None,
                 options=None, enable_injection=True, retain_source=True, **kwargs):
        super().__init__(pageurl, sitekey, loop=loop, proxy=proxy, proxy_auth=proxy_auth,
                         options=options, enable_injection=enable_injection, retain_source=retain_source, **kwargs)
    async def on_goto(self):
        self.log('Cookies ready!')

    async def close_dialog(dialog):
        print(dialog.message)
        await dialog.dismiss()
        await browser.close()

    async def on_start(self):
        # Set or Change data
        r = requests.get(sys.argv[2]+"/akun.php")
        self.data = json.loads(r.content)
        self.log('ACCOUNT INFO')
        self.log('userid : '+self.data['username'])
        self.log('password : '+self.data['password'])
        self.log('email : '+self.data['email'])
        self.log('id : '+self.data['id'])
        await self.page.addScriptTag({'content' : 'alert = function (){}'})
        await self.page.type('input[name="userid"]', self.data['username'])
        await self.page.click('a[href="javascript:useridCheck();"]')
        await self.page.type('input[name="password"]', self.data['password'])
        await self.page.type('input[name="repassword"]', self.data['password'])
        await self.page.type('input[name="email"]', self.data['email'])
        await self.page.click('a[href="javascript:emailCheck();"]')
        while True:
             r = requests.get(sys.argv[2]+"/email.php?email="+self.data['email']+"&password="+self.data['password'])
             time.sleep(60)
             if r.content:
                 code = json.loads(r.content)
                 if code['token']:
                    await self.page.type('input[name="code"]', code['token'])
                    self.log('token : '+code['token'])
                    break

    async def on_finish(self):
        # Click button Send
        self.log('Clicking send button ...')

client = MySolver(
    # With Proxy
    pageurl, sitekey, options=options, proxy=proxy
    # Without Proxy
    # pageurl, sitekey, options=options
)

client.loop.run_until_complete(client.start())


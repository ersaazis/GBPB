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

    async def on_start(self):
        # Set or Change data
        # r = requests.get(sys.argv[2]+"/akun.php")
        # self.data = json.loads(r.content)
        # self.log('ACCOUNT INFO')
        # self.log('userid : '+self.data['username'])
        # self.log('password : '+self.data['password'])
        # self.log('email : '+self.data['email'])
        # self.log('id : '+str(self.data['id']))
        # await self.page.addScriptTag({'content' : 'alert = function (){};'})
        # await self.page.type('input[name="userid"]', self.data['username'])
        # time.sleep(1)
        # await self.page.click('a[href="javascript:useridCheck();"]')
        # await self.page.type('input[name="password"]', self.data['password'])
        # await self.page.type('input[name="repassword"]', self.data['password'])
        # await self.page.type('input[name="email"]', self.data['email'])
        # time.sleep(1)
        # await self.page.click('a[href="javascript:emailCheck();"]')
        # while True:
        #     self.log('wait 60')
        #     time.sleep(60)
        #     r = requests.get(sys.argv[2]+"/email.php?email="+self.data['email']+"&password="+self.data['password'])
        #     if r.content:
        #         code = json.loads(r.content)
        #         if code['token']:
        #             await self.page.type('input[name="code"]', code['token'])
        #             self.log('token : '+code['token'])
        #             time.sleep(1)
        #             await self.page.click('a[href="javascript:emailVerify();"]')
        #             time.sleep(3)
        #             break
        await self.page.click('input[id="join_agree"]')
        time.sleep(10)

    async def solve(self):
        """Click checkbox, otherwise attempt to decipher audio"""
        self.log('Solvering ...')
        await self.get_frames()
        self.log('Wait for CheckBox ...')
        await self.loop.create_task(self.wait_for_checkbox())
        self.log('Click CheckBox ...')
        await self.click_checkbox()
        await self.click_reload_button()
        time.sleep(5)
        try:
            result = await self.loop.create_task(
                self.check_detection(self.animation_timeout))
        except SafePassage:
            return await self._solve()
        else:
            if result["status"] == "success":
                """Send Data to Buttom"""
                # await self.loop.create_task(self.wait_for_send_button())
                # await self.click_send_buttom()
                code = await self.g_recaptcha_response()
                if code:
                    result["code"] = code
                    return result
            else:
                return result
    async def wait_for_frames(self):
        pass

    async def on_finish(self):
        # Click button Send
        self.log('Send Button ...')
        await self.page.click('a[onclick="javascript:sendIt();"]')
        self.log('GET '+sys.argv[2]+"/simpan.php?id="+str(self.data['id']))
        requests.get(sys.argv[2]+"/simpan.php?id="+str(self.data['id']))
        self.log('Create Account Success ...')
        time.sleep(20)

client = MySolver(
    # With Proxy
    pageurl, sitekey, options=options, proxy=proxy
    # Without Proxy
    # pageurl, sitekey, options=options
)

client.loop.run_until_complete(client.start())

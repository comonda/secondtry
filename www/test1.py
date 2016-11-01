import asyncio
import www.orm
from www.models import User
import sys
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from www.orm.create_pool(loop, user='root', password='364834547', db='awesome')

    u = User(name='admin', email='364834547@qq.com', passwd='123123', image='about:blank', admin=True)

    yield from u.save()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
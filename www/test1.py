import asyncio
import www.orm
from www.models import User
import sys
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from www.orm.create_pool(loop, user='root', password='364834547', db='awesome')

    u = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
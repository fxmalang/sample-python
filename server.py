import asyncio
from aiohttp import web


async def Task1():
    for i in range(100):
        print ('Task-1',i)
        await asyncio.sleep(1)



async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def HttspServer():
    # create the application, as before
    app = web.Application()
    app.add_routes([
        web.get('/', handle),
        web.get('/{name}', handle)
    ])

    # set up the web server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)
    await site.start()

    # wait forever, running both the web server and the tasks
    await asyncio.Event().wait()


loop=asyncio.new_event_loop()
loop.create_task(Task1())
loop.create_task(HttspServer())
loop.run_forever()
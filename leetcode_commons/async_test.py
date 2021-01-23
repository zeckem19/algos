import asyncio
import time

async def give_something(what):
    await asyncio.sleep(2)
    a = str(what)+'123'
    return a

async def give_something2(what):

    await asyncio.sleep(2)
    # time.sleep(2)
    a = str(what)+'456'
    return a

async def do_it():
    start = time.time()
    
    await give_something('33')
    await give_something2('44')
    print(time.time() - start)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(do_it())
loop.close()
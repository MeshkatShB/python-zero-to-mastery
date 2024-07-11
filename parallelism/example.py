import asyncio


async def say_after(delay, message):
    await asyncio.sleep(delay)
    return message


async def main():
    result = await asyncio.gather(
        say_after(1, 'Hello'),
        say_after(2, 'World')
    )
    print(result)  # Output: ['Hello', 'World']

asyncio.run(main())

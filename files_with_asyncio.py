import asyncio
import time

async def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

async def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

async def main():
    await write_to_file('file.txt', "This is a work in progress")
    text = await read_from_file("file.txt")

if __name__ == '__main__':
    asyncio.run(main())
    print("The time that the program took to run was: ", time.process_time(), "seconds")

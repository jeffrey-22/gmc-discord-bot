# Run selected tests

from test.test import *
import asyncio

if __name__ == "__main__":
    asyncio.run(test_notion_available_pages())
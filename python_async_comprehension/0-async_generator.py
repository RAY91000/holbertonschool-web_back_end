#!/usr/bin/env python3
""" Coroutine with async """

from typing import AsyncGenerator
import asyncio
import random

async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times asynchronously, yielding random number after 1 second each time"""

    for _ in range(10):
        await asyncio.sleep(1)  # D'abord attendre 1 seconde
        yield random.uniform(0, 10)  # Puis envoyer un nombre aléatoire

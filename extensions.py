from echobot import *
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    TurnContext,
)
import asyncio

bot = EchoBot()

settings = BotFrameworkAdapterSettings("","")
adapter = BotFrameworkAdapter(settings)
""" Créez un objet pour la boucle d'événements, lorsqu'elle est appelée à partir d'une coroutine ou d'un callback,
 cette fonction renvoie toujours la boucle d'événements en cours d'exécution."""
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop)
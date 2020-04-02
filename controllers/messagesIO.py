from flask import request, Response
from extensions import *
from botbuilder.schema import Activity

def test():
    return 'yes worked'

def messages():
    if "application/json" in request.headers["Content-Type"]:
        body = request.json
    else:
        return Response(status=415)
    activity = Activity().deserialize(body)
    auth_header = (
        request.headers["Authorization"] if "Authorization" in request.headers else ""
    )

    async def aux_func(turn_context):
        await bot.on_turn(turn_context)
    try:
        task = loop.create_task(
            adapter.process_activity(activity, auth_header, aux_func)
        )
        loop.run_until_complete(task)
        return Response(status=201)
    except Exception as exception:
        raise exception
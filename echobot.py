from sys import exit

class EchoBot:
    async def on_turn(self, context):
        """
            cette fonction teste si le type de l'activite est un message envoyé et s il existe un message
            puis retourne un message avec le message initialement envoye et la longeur du message
        :param context: Cet objet gère les détails de l'activité.
        :return: rien
        """
        if context.activity.type == "message" and context.activity.text:
            strlen = len(context.activity.text)
            sendInfo = "hey you send text : " + context.activity.text + "  and  the lenght of the string is  " + str(strlen)
            await context.send_activity(sendInfo)
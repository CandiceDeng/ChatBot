import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

class ChatBotView(TemplateView):
    template_name = 'index.html'



class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    bot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        # input_data = json.loads(request.body.decode('utf-8'))
        input_data = request.POST['userInput']
        if input_data == '':
            return JsonResponse({
                'message': 'userInput is empty'
            }, status=400)
        print(dir(self.bot))
        response = self.bot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

# # #Api endpoint
# class ChatBotApi(View):
#     def post(self, request, *args, **kwargs):
#         input_data = json.loads(request.body.decode('utf-8'))

#         if 'content' not in input_data:
#             return JsonResponse({
#                 'text': [
#                     'The attribute "text" is required.'
#                 ]
#             }, status=400)

#         response = self.chatterbot.get_response(input_data)

#         response_data = response.serialize()

#         return JsonResponse(response_data, status=200)

#     def get(self, request, *args, **kwargs):
#         return JsonResponse({
#             'name': self.chatterbot.name
#         })
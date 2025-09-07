from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TelegramUserSerializer
from .models import TelegramUser

#
# Create your views here.
@api_view(['POST'])
def register_user(request):
    data = request.data
    user, created = TelegramUser.objects.get_or_create(
        user_id=data['user_id'],
        defaults={'username': data.get('username','DefaultName')}
    )
    if created:
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'message': 'User is already registered'})

@api_view(['GET'])
def get_users(request):
    users = TelegramUser.objects.all()
    serializer = TelegramUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except TelegramUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
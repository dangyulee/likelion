from .models import Board
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# 전체목록
@api_view(['GET'])
def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def board_post(request):
    serializer = PostSerializer(data=request.data) # 요청 데이터(request.data)를 가지고 역직렬화를 수행해줄 수 있다.
    if serializer.is_valid(): # 유효성 검사
        serializer.save() # 역직렬화해서 만들어낸 Blog 모델을 저장한다.
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def board_detail(request, post_id):
    try:
        board = Board.objects.get(id=post_id)
        if request.method == 'GET':
            serializer = GetDetail(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = BoardSerializer(board, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET','POST'])
def comment_post(request, post_id):
    try:
        board = Board.objects.get(id=post_id)
        comment = Comment.objects.filter(post=board)
        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data) # 요청 데이터(request.data)를 가지고 역직렬화를 수행해줄 수 있다.
            if serializer.is_valid(): # 유효성 검사
                serializer.save(post=board) # 역직렬화해서 만들어낸 Blog 모델을 저장한다.
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        elif request.method == 'GET':
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
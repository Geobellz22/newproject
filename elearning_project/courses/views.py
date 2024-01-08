from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CourseSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
#def get_course(request, pk):
    #course = get_object_or_404(Course, pk=pk)
    #serializer = CourseSerializer(course)
    #return Response(serializer.data)

#@api_view(['PUT'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
#def update_course(request, pk):
    #course = get_object_or_404(Course, pk=pk)
    #serializer = CourseSerializer(course, data=request.data)
    #if serializer.is_valid():
     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['DELETE'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
#def delete_course(request, pk):
 #  course.delete()
  #  return Response(status=status.HTTP_204_NO_CONTENT)

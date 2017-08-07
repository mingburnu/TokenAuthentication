from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveAPIView
from rest_framework.serializers import ModelSerializer

from .models import Question, Choice


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class QuestionList(ListCreateAPIView):
    """
    Get / Create questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(RetrieveDestroyAPIView):
    """
    Get / Delete questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceDetail(RetrieveUpdateAPIView):
    """
    Get / Update a Choice
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UserCreate(CreateAPIView):
    """
    Create a User
    """
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()


class UserDetail(RetrieveAPIView):
    """
    Retrieve a User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

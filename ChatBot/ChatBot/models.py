from django.db import models

class User(models.Model):
    # Id = models.ForeignKey('userID', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    UserInput = models.CharField(max_length=10000)

    class Meta:  
        db_table = "user"


class Question(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)


class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
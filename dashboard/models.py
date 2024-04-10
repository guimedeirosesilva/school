from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import EmptyClass, InvalidLearners, EmptyPayer, MultiplePayers

# https://drawsql.app/teams/guis-team/diagrams/school

# Create your models here.
class User(AbstractUser):
    pass


class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth = models.DateField()
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=50)
    prefered_day_for_payment = models.IntegerField()

    # Foreign keys
    group = models.ForeignKey("Group", on_delete=models.CASCADE, related_name="students", blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")

    #----------- METHODS --------------

    # printing name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Group(models.Model):
    name = models.CharField(max_length=120)

    # Foreign keys
    contact = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="group_leader")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_groups")

    #----------- METHODS --------------

    # printing name
    def __str__(self):
        return self.name


class Class(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    appointment = models.DateTimeField()

    # Foreign keys
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="classes", blank=True, null=True)
    group = models.ForeignKey(Group,  on_delete=models.CASCADE, related_name="classes", blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="classes")

    #----------- METHODS --------------

    # Get the day of the week
    def get_weekday(self):
        weekday = self.appointment.weekday()

        match weekday:
            case 0:
                return "Monday"
            case 1:
                return "Tuesday"
            case 2:
                return "Wednesday"
            case 3:
                return "Thrusday"
            case 4:
                return "Friday"
            case 5:
                return "Saturday"
            case 6:
                return "Sunday"
            case _:
                return "Invalid Day"


    # printing name
    def __str__(self):
        return f"{self.title.capitalize()}: {self.get_weekday()}s at {self.appointment.time()} "
    

    # method to determine if it's a group class or a private class
    def type_of_class(self):
        if self.student is None and self.group is not None:
            return "GROUP"
        elif self.student is not None and self.group is None:
            return "PRIVATE"
        elif self.student is None and self.group is None:
            raise EmptyClass("the class can't be empty")
        else:
            raise InvalidLearners("you can't have a class that is both a private and a group class")



class Payments(models.Model):
    due_date = models.DateField()
    price = models.FloatField()
    is_payed = models.BooleanField(default=False)

    # Foreign keys
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payments", blank=True, null=True)
    group = models.ForeignKey(Group,  on_delete=models.CASCADE, related_name="payments", blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")

    #----------- METHODS --------------

    # method to determine if it's a group or an individual student payment
    def type_of_class(self):
        if self.student is None and self.group is not None:
            return "GROUP"
        elif self.student is not None and self.group is None:
            return "PRIVATE"
        elif self.student is None and self.group is None:
            raise EmptyPayer("there must be one payer")
        else:
            raise MultiplePayers("you can't have a class with multiple payers")
        
    
    # printing name
    def __str__(self):
        message = f"R$ {self.price} for classes to "
        
        try:
            flag = self.type_of_class()
        except (EmptyClass, MultiplePayers) as e:
            flag = e

        if flag == "GROUP":
            message += self.group.name
        elif flag == "PRIVATE":
            message += self.student.name
        else:
            message += "SOMEBODY"

        message += f" due on {self.due_date} | status: "

        if self.is_payed:
            message += "PAYED"
        else:
            message += "PENDING"

        return message
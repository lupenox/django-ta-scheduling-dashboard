from django.db import models


class AccountType(models.TextChoices):
    TA = "TA", "TA"
    ADMIN = "admin", "Admin"
    INSTRUCTOR = "instructor", "Instructor"


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    accountType = models.CharField(
        max_length=12,
        choices=AccountType.choices,
        default=AccountType.TA,
    )

    def __str__(self):
        return f"{self.username} ({self.get_accountType_display()})"


class Section(models.Model):
    number = models.CharField(max_length=255, default="UNNAMED")
    course = models.ForeignKey(
        "Course",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="course_sections",
    )
    ta = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_sections",
    )

    def __str__(self):
        if self.course:
            return f"{self.course.name} - Section {self.number}"
        return f"Section {self.number}"


class Course(models.Model):
    name = models.CharField(max_length=255)
    TAs = models.ManyToManyField(User, blank=True, related_name="ta_courses")
    instructor = models.ManyToManyField(User, blank=True, related_name="instructor_courses")
    sections = models.ManyToManyField(Section, blank=True, related_name="courses")

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    account_type = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        name = " ".join(part for part in [self.first_name, self.last_name] if part)
        return name or self.email

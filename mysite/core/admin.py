from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Post
from .models import Question
from .models import TutorialCategory
from .models import Tutorials
from .models import TutorialSeries
from .models import CV

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorials)
admin.site.register(CV)


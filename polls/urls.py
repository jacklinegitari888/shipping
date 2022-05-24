from .views import get_time, get_questions,get_detail,get_results,get_vote,get_question
from django.urls import path

urlpatterns = [
   path("questions/",get_questions),
   path("questions/<int:id>",get_question),
   path("time/",get_time),
   path("detail/",get_detail),
   path("results/",get_results),
   path("vote/",get_vote)
]

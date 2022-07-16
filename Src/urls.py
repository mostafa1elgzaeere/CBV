from django.contrib import admin
from django.urls import path

# from Test.views import AddPlayer admin
from django.urls import path

from Test.views import AddPlayer





# from Test.views import PlayersListView
# from Test.views import PlayerDetail
# # from Test.views import PlayerTemplateView
# from Test.views import CreatePlayer
# from Test.views import UpdatePlayer
# from Test.views import DeletePlayer 



urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    # path('players/', PlayersListView.as_view(),name="players"),
    
    # path('player/<int:pk>/', PlayerDetail.as_view(),name="player_detail"),

    # path("player/<int:number>/",PlayerTemplateView.as_view(extra_context={"club":"madrid"}),name="player")
    
    # path("create/",CreatePlayer.as_view(),name="create"),
    
    # path("update/<int:pk>",UpdatePlayer.as_view(),name="update_player")
    
    # path("delete/<int:pk>",DeletePlayer.as_view(),name="delete_player")
    
    # path("add_player_by_django_forms/",AddPlayer.as_view(),name="add_player"),
    path("add_player_by_model_forms/",AddPlayer.as_view(),name="add_player"),

    

]

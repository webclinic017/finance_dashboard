# from worker.make_data import pick_progress
# from charts.forms import addToPortfolio
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='charts'),
    path('test', views.test, name='test'),
    path('addToIndex/<str:pk>/', views.addToIndex, name='addToIndex_'),
    path('rmFromIndex', views.rmFromIndex, name='rmFromIndex'),
    path('workers', views.workers, name='workers'),
    path('updateDb', views.updateDb, name='updateDb'),
    path('dwnldData', views.dwnldData, name='dwnldData'),
    path('updateCharts', views.updateCharts, name='updateCharts'),
    path('tracker/', views.tracker, name='tracker'),
    path('api/progress', views.progress, name='progress')
    # path('<int:stk_id>/', views.detail, name='detail')
]
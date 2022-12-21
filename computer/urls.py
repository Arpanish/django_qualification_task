from django.urls import path
from computer.views import ComputerList,ComputerCreate,ComputerDetail,ComputerDelete,ComputerInfoUpdate,Thanks
urlpatterns = [
    path('',ComputerList.as_view(),name='computerlist'),
    path('createlist/',ComputerCreate.as_view(),name='computercreate'),
    path('computerdetail/<int:id>',ComputerDetail.as_view(),name='computerdetail'),
    path('computerdelete/<int:id>', ComputerDelete.as_view(), name="computerdelete"),
    path('computerinfoupdate/<int:id>',ComputerInfoUpdate.as_view(),name='computerupdate'),
    path('thanks/',Thanks.as_view(),name='thanks'),

]
from django.urls import path
from book.views import (
    listbook,
    bookditale,
    creatcategory,
    createahoter,
    creatbook,
    edit_book,
)


urlpatterns = [
    path('list/', listbook , name='list'),
    path('bookditale/<str:id>/', bookditale , name='ditale'),
    path('new_category/',creatcategory, name='new_category' ),
    path('new_ahthor/', createahoter, name='new_ahthor'),
    path('newbook/', creatbook, name='new_book'),
    path('edit_book/<str:id>/', edit_book,name='editbook')
    


]
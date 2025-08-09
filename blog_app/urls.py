from django.urls import path
from.views import ArticleList,ArticleDetail,ArticleAdd,ArticleUpdate,ArticleDelete,ArticleFilter,HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', ArticleList.as_view(), name='article_list'),  # GET همه پست‌ها
    path('posts/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),  # GET یک پست
    path('posts/', ArticleAdd.as_view(), name='article_add'),  # POST ایجاد پست جدید
    path('posts/<int:pk>/', ArticleUpdate.as_view(), name='article_update'),  # PUT آپدیت
    path('posts/<int:pk>/', ArticleDelete.as_view(), name='article_delete'),  # DELETE حذف
    path('posts/search/<str:term>/', ArticleFilter.as_view(), name='article_filter'),  # جستجو
]

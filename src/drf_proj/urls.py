from django.urls import include, path
from rest_framework import routers

from drf_app import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('snippets', views.SnippetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('', include('drf_app.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

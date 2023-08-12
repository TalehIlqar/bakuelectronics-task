from django.urls import path

from .views import (
    GetUser,
    GetUsers,
    CreateUser,
    UpdateUser,
    DeleteUser,
    BlockedIPCreateAPIView,
)

urlpatterns = [
    # get users
    path("users/", GetUsers.as_view(), name="get_users"),
    # get user by id
    path("users/detail/<int:id>/", GetUser.as_view(), name="get_user_by_id"),
    # create user
    path("users/create/", CreateUser.as_view(), name="create_user"),
    path("users/add-ip", BlockedIPCreateAPIView.as_view(), name="add_ip"),
    # update user
    path("users/update/<int:id>/", UpdateUser.as_view(), name="update_user"),
    # delete user
    path("users/delete/<int:id>/", DeleteUser.as_view(), name="delete_user"),
]

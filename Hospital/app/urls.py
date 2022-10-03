



from unicodedata import name
from django.urls import path



from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    path("Hospital/dashboard/",views.Dashboard,name="dashboard"),
    path("",views.Signup,name="signup"),
    path("Hospital/login/",views.Login,name="login"),
    path("Hospital/logout/",views.logout,name="logout"),
    path("Hospital/blogpost/",views.blogPost,name="blogPost"),
    path("Hospital/update/blogpost/<int:id>",views.update_post,name="update_post"),
    path("Hospital/delete/blogpost/<int:id>",views.delete_post ,name="delete_post"),
    path("Hospital/bookAppointment/",views.bookAppointment,name="bookAppointment"),
    path("jsi18n", JavaScriptCatalog.as_view(),name="js-catlog"),
    path("Hospital/appointmentDetails/",views.appointmentDetails,name="appointmentDetails"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

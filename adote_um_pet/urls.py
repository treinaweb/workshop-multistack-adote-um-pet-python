from django.urls import path, include

urlpatterns = [
    path("api/pets", include("pet.urls")),
    path("api/adocoes", include("adocao.urls")),
]

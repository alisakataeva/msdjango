from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from lib.api.country import router as mslc_router
from lib.api.language import router as msll_router
from musicstation.api.artist import router as msa_router


#


nj_api = NinjaAPI()

nj_api.add_router("/music-station/lib/country", mslc_router)
nj_api.add_router("/music-station/lib/language", msll_router)
nj_api.add_router("/music-station/artist", msa_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", nj_api.urls),
]

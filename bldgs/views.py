from django.shortcuts import render
from bldgs.models import EnergyUsageLargeCommercialBuildingsReported2014


# Create your views here.
def index(request):
    bldg_list = EnergyUsageLargeCommercialBuildingsReported2014.get_bldg_data
    context = dict(Bldg_list=bldg_list)
    return render(request, 'bldgs/index.html', context)

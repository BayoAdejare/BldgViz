from django.contrib import admin
from .models import EnergyUsageLargeCommercialBuildingsReported2014


# Register your models here.
@admin.register(EnergyUsageLargeCommercialBuildingsReported2014)
class BldgAdmin(admin.ModelAdmin):
    @property
    def portfolio(self):
        my_bldg_data = EnergyUsageLargeCommercialBuildingsReported2014.get_bldg_data
        row = my_bldg_data.row()
        print(row)
        return my_bldg_data

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'
    pass


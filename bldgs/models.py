from __future__ import unicode_literals
from django.db import models
from django.db import connection


# Create your models here.
class EnergyUsageLargeCommercialBuildingsReported2014(models.Model):
    Portfolio_Manager_ID = models.CharField(max_length=200, null=True)
    Property_Name = models.CharField(max_length=200, null=True)
    Postal_Code = models.CharField(max_length=200, null=True)
    Primary_Property_Type_EPA_Calculated = models.CharField(max_length=200, null=True)
    Property_Floor_Area_Buildings_and_Parking = models.CharField(max_length=200, null=True)
    Year_Built = models.CharField(max_length=200, null=True)
    Number_of_Buildings = models.CharField(max_length=200, null=True)
    Philadelphia_Building_ID = models.CharField(max_length=200, null=True)
    Electricity_Use_Grid_from_Onsite_Renewable_Systems_kBtu = models.CharField(max_length=200,
                                                                                                      null=True)
    Natural_Gas_Use_kBtu = models.CharField(max_length=200, null=True)
    Fuel_Oil_2_Use_kBtu = models.CharField(max_length=200, null=True)
    District_Steam_Use_kBtu = models.CharField(max_length=200, null=True)
    ENERGY_STAR_Score = models.CharField(max_length=200, null=True)
    Site_EUI_kBtu_per_ftA_squared = models.CharField(max_length=200, null=True)
    Source_EUI_kBtu_per_ftA_squared = models.IntegerField(null=True)
    Water_Use_All_Water_Sources_kgal = models.IntegerField(null=True)
    Total_GHG_Emissions_MtCO2e = models.IntegerField(null=True)
    Notes = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Building Portfolio'
        verbose_name_plural = 'Building Portfolios'


    @property
    def get_bldg_data(self):
        """

        :rtype: object
        """
        cursor = connection.cursor()

        assert isinstance(cursor, object)
        row = EnergyUsageLargeCommercialBuildingsReported2014.objects.raw(
                                '''SELECT col_1 AS Portfolio_Manager_ID, col_2 AS Property_Name, col_3 AS Postal_Code,
                                col_4 AS Primary_Property_Type_EPA_Calculated,
                                col_5 AS Property_Floor_Area_Buildings_and_Parking, col_6 AS Year_Built,
                                col_7 AS Number_of_Buildings, col_8 AS Philadelphia_Building_ID,
                                col_9 AS Electricity_Use_Grid_Purchase_and_Generated_from_Onsite_Renewable_Systems_kBtu,
                                col_10 AS Natural_Gas_Use_kBtu, col_11 AS Fuel_Oil_2_Use_kBtu,
                                col_12 AS District_Steam_Use_kBtu, col_13 AS ENERGY_STAR_Score,
                                col_14  AS Site_EUI_kBtu_per_ftA_squared, col_15 AS Source_EUI_kBtu_per_ftA_squared,
                                col_16 AS Water_Use_All_Water_Sources_kgal, col_17 AS Total_GHG_Emissions_MtCO2e,
                                col_18 AS Notes, col_19 AS Location FROM
                                bldgs_EnergyUsageLargeCommercialBuildingsReported2014''')

        assert isinstance(row, object)
        return row


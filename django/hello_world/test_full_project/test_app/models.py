from django.db import models


# Create your models here.
class MarketData(models.Model):
    ticker = models.CharField(max_length=40, blank=False)
    data = models.CharField(max_length=40, blank=False)
    open_value = models.IntegerField(blank=False)
    close_value = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.ticker} {self.data} {self.open_value} {self.close_value}"

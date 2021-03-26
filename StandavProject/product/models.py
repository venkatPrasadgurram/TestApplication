from django.db import models
from django.contrib.auth.models import User

class UserProductList(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='altathera_formulary_user')
	product_name = models.CharField(max_length=100,null=True,blank=True)

	class Meta:
		db_table = 'user_product_list'
from django.db import models

# Create your models here.


class UserData(models.Model):
    uid  = models.CharField(max_length=300)
    username = models.TextField(max_length=255)
    email  = models.TextField(default=0.0)
    phone  = models.TextField(default=0.0)
    preferencelist  = models.TextField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uid} - {self.username} - created : {self.timestamp}"


class ProductData(models.Model):
    pid  = models.CharField(max_length=300)
    title = models.TextField(default="")
    description  = models.TextField(default="")
    img  = models.TextField(default="") # stored as base64
    price  = models.TextField(default="")
    tags  = models.TextField(default="")
    escore  = models.TextField(default="")
    ecoobj  = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pid} - {self.title} - price : {self.price} - escore: {self.escore} - tags : {self.tags}"
    


    








# class SensorData(models.Model):
#     # api_key = models.CharField(max_length=300)
#     nodename = models.CharField(max_length=255)
#     depth_1 = models.FloatField(default=0.0)
#     depth_2 = models.FloatField(default=0.0)
#     depth_3 = models.FloatField(default=0.0)
#     temperature = models.FloatField(default=0.0)
#     humidity = models.FloatField(default=0.0)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     # mode = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.nodename} - {self.timestamp}"


# class Nodedata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     node_name = models.CharField(max_length=255, default="")
#     Loc_lat = models.CharField(max_length=20, default="")
#     Loc_long = models.CharField(max_length=20, default="")
#     api_key = models.CharField(max_length=300, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.node_name}"


# class Clusterdata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     cluster_name = models.CharField(max_length=255, default="")
#     clust_data = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.cluster_name}"


# ------------------------------------
# Sample Code Below
# ------------------------------------

# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name

# # mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name

# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return self.name

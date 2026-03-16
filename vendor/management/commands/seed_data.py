from django.core.management.base import BaseCommand
from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification
from vendor_product_mapping.models import VendorProductMapping

class Command(BaseCommand):
    help = 'Seeds the database with sample Vendors, Products, Courses, and Mappings.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing old data...")
        VendorProductMapping.objects.all().delete()
        Vendor.objects.all().delete()
        Product.objects.all().delete()
        Course.objects.all().delete()
        Certification.objects.all().delete()

        self.stdout.write("Creating master entities...")
        
        v1 = Vendor.objects.create(name="TechCorp", code="V-TC-01", description="Global tech supplier")
        v2 = Vendor.objects.create(name="EduSolutions", code="V-ES-02", description="Education materials")

        p1 = Product.objects.create(name="Cloud Server Basic", code="P-CSB-01")
        p2 = Product.objects.create(name="Data Analytics Pro", code="P-DAP-02")

        c1 = Course.objects.create(name="Intro to Cloud", code="C-ITC-01")
        
        cert1 = Certification.objects.create(name="Cloud Associate", code="CERT-CA-01")

        self.stdout.write("Creating mappings...")
        
        VendorProductMapping.objects.create(
            vendor=v1, 
            product=p1, 
            primary_mapping=True
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
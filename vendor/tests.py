from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Vendor

class VendorAPITests(APITestCase):
    def setUp(self):
        """
        This method runs before every test. 
        We use it to set up initial data and URLs.
        """
        self.vendor = Vendor.objects.create(
            name="Tech Supplies Inc.",
            code="VEND001",
            description="Hardware supplier"
        )
        self.list_create_url = reverse('vendor-list-create')
        self.detail_url = reverse('vendor-detail', args=[self.vendor.id])

    def test_get_vendor_list(self):
        """Test retrieving the list of vendors."""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['code'], "VEND001")

    def test_create_vendor_success(self):
        """Test creating a new vendor with valid data."""
        data = {
            "name": "Software Solutions LLC",
            "code": "VEND002",
            "description": "Software vendor"
        }
        response = self.client.post(self.list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_create_vendor_duplicate_code(self):
        """Test validation: Code must be unique."""
        data = {
            "name": "Another Vendor",
            "code": "VEND001"
        }
        response = self.client.post(self.list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_vendor(self):
        """Test partially updating a vendor."""
        data = {"name": "Updated Tech Supplies"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, "Updated Tech Supplies")

    def test_delete_vendor(self):
        """Test deleting a vendor."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)
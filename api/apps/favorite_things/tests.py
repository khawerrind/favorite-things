from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import FavoriteThings, Categories, AuditLog


class BaseTestCaseHelper(object):

    def setUp(self):
        """Define the test client and other test variables."""
        self.title = "Bill Gates"
        self.category = Categories.objects.get_or_create(name='Person')[0]
        self.favorite_thing = FavoriteThings.objects.create(
            title=self.title,
            category=self.category,
            rank=1
        )


class FavoriteThingsListCreateAPIViewTestCase(BaseTestCaseHelper, TestCase):

    def test_api_can_create_a_favorite_thing_and_updates_ranks(self):
        """Test the api can create a favorite thing."""
        data = {
            'title': 'Steve Jobs',
            'category': self.category.id,
            'rank': 1
        }
        response = self.client.post(
            reverse('list-create-favorite'),
            data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.favorite_thing.refresh_from_db()
        self.assertEqual(self.favorite_thing.rank, 2)
        obj = FavoriteThings.objects.get(id=response.data['id'])
        self.assertEqual(obj.rank, 1)
        self.assertEqual(FavoriteThings.objects.count(), 2)

    def test_api_can_get_list_of_favorite_things(self):
        """Test the api can get list of favorite things."""
        response = self.client.get(
            reverse('list-create-favorite'),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        favorite_thing = response.data[0]
        self.assertEqual(favorite_thing['id'], self.favorite_thing.id)


class FavoriteThingsRetrieveUpdateDestroyAPIViewTestCase(BaseTestCaseHelper, TestCase): # noqa

    def test_api_can_get_a_favorite_thing(self):
        """Test the api can get a given favorite thing."""
        response = self.client.get(
            reverse('details-favorite', kwargs={'pk': self.favorite_thing.id}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), self.favorite_thing.id)

    def test_api_can_update_favorite_thing_and_update_ranks(self):
        """Test the api can update a given favorite thing."""
        change_favorite_thing = {
            'title': 'Something new',
            'category': self.category.id,
            'rank': 1
        }
        res = self.client.put(
            reverse('details-favorite', kwargs={'pk': self.favorite_thing.id}),
            change_favorite_thing,
            content_type='application/json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get('title'), change_favorite_thing['title'])
        self.assertEqual(res.data.get('category'), self.category.id)

    def test_api_can_delete_favorite_thing(self):
        """Test the api can delete a given favorite thing."""
        res = self.client.delete(
            reverse('details-favorite', kwargs={'pk': self.favorite_thing.id}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class CategoriesListCreateAPIViewTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.cat1 = Categories.objects.create(name='Person')
        self.cat2 = Categories.objects.create(name='Food')

    def test_api_can_get_list_of_categories(self):
        """Test the api can get list of categories."""
        response = self.client.get(
            reverse('list-create-category'),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        cat1 = response.data[1]
        cat2 = response.data[0]

        self.assertEqual(cat1['id'], self.cat1.id)
        self.assertEqual(cat2['id'], self.cat2.id)

    def test_api_can_create_a_category(self):
        """Test the api can create a category."""
        data = {'name': 'Place'}
        response = self.client.post(
            reverse('list-create-category'),
            data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        obj = Categories.objects.get(id=response.data['id'])
        self.assertEqual(obj.name, 'Place')


class AuditLogListCreateAPIViewTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.audit1 = AuditLog.objects.create(title='Test 1', action="created")
        self.audit2 = AuditLog.objects.create(title='Test 2', action="updated")

    def test_api_can_get_list_of_audit_logs(self):
        """Test the api can get list of audit logs."""
        response = self.client.get(
            reverse('list-audits'),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        audit1 = response.data[1]
        audit2 = response.data[0]

        self.assertEqual(audit1['id'], self.audit1.id)
        self.assertEqual(audit2['id'], self.audit2.id)

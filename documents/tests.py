from django.test import TestCase

from rest_framework.test import APITestCase
from documents.models import Document

class DocumentsListTestCase(APITestCase):
    fixtures = ['test_data.json']

    def test_list_view(self):
        count = Document.objects.count()
        self.assertEqual(
            4, 
            count
        )

        response = self.client.get('/documents/')

        self.assertEqual(
            response.data,
            [
                {'slug': 'doc_1'},
                {'slug': 'doc_2'},
                {'slug': 'doc_3'},
            ]
        )

    def test_create_view(self):
        initial_count = Document.objects.count()
        doc_data = {
            'slug': 'new_slug',
            'content': 'test text',
        }

        response = self.client.post('/documents/', doc_data)
        
        self.assertEqual(
            Document.objects.count(), 
            initial_count + 1,
        )

        self.assertEqual(
            response.data,
            doc_data
        )

    def test_create_view_errors(self):
        initial_count = Document.objects.count()
        doc_data_err_list = [
            {
                'slug': 'new slug',
                'content': 'test text',
            },
            {
                'slug': 'doc_1',
                'content': 'test text',
            },
            {
                'slug': '',
                'content': 'test text',
            }
        ]

        for err_data in doc_data_err_list:
            response = self.client.post('/documents/', err_data)

            self.assertEqual(
                Document.objects.count(), 
                initial_count,
            )

            self.assertEqual(
                response.status_code,
                400
            )

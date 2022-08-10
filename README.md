## Wiki test project
Test project to store and change small docs 

Prepare env
`pip install -r requirements.txt`

Run migrations
`./manage.py migrate`

Load test data 
`./manage.py loaddata documents/fixtures/test_data.json`

Run server
`./manage.py runserver`

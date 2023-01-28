from fastapi import FastAPI
from . import api


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Registration and authofication',
    },
    {
        'name': 'operations',
        'description': 'Create, view, update, delete',
    },
    {
        'name': 'reports',
        'description': 'Import/export cvs',
    },
]

app = FastAPI(
    title='Acco',
    description='Service of expense and income',
    version='0.0.1',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)

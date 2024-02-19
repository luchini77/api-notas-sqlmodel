import uvicorn

from api.app import create_app

api = create_app()

if __name__=='__main__':
    uvicorn.run('main:api',port=8000,reload=True)
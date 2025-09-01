from authlib.integrations.django_client import OAuth
from dotenv import load_dotenv
import os

oauth = OAuth()

oauth.register(
    name='suap',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url = 'https://suap.ifrn.edu.br/api/',
    request_token_url = None,
    access_token_method = 'POST',
    access_token_url = 'https://suap.ifrn.edu.br/o/token/',
    authorize_url = 'https://suap.ifrn.edu.br/o/authorize/',
    fetch_token = lambda request: request.session.get('suap_token')
)
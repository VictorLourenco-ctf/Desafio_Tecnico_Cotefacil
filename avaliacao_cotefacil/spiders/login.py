import base64
import json
from abc import abstractmethod

import scrapy
from scrapy import Request
from scrapy.exceptions import CloseSpider
from scrapy.http import Response
from scrapy.http.cookies import CookieJar
from scrapy.utils.defer import maybe_deferred_to_future

from avaliacao_cotefacil.suppliers.payloads import login


class LoginSpider(scrapy.Spider):
    name = 'login'
    site_url = 'https://pedidoeletronico.servimed.com.br/'
    api_url = 'peapi.servimed.com.br'

    def __init__(self, user: str, password: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.user = user
        self.password = password
        self.session_token = None
        self.access_token = None

    async def start(self):
        self.logger.info('Iniciando processo de Login')

        yield scrapy.Request(
            url='https://peapi.servimed.com.br/api/usuario/login',
            method='POST',
            body=json.dumps(login(self.user, self.password)),
            headers={'Content-Type': 'application/json'},
            callback=self.parse_login,
            meta={"handle_httpstatus_all": True}
        )

    def parse_login(self, response):
        self.logger.info('Validando resposta de login')

        if response.status > 300:
            raise CloseSpider('Falha ao realizar login')

        self.access_token = self.get_access_token(response)
        self.session_token = self.get_access_token_id()


        return self.post_login(response)

    def get_access_token(self, response: Response) -> str:
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        return cookie_jar._cookies['.servimed.com.br']["/"]["accesstoken"].value

    def get_access_token_id(self) -> str:
        header, jwt, signature = self.access_token.split(".")
        decoded = base64.urlsafe_b64decode(jwt + '=' * (4 - len(jwt) % 4))
        json_data = json.loads(decoded)
        return json_data["token"]

    async def inline_requests(self, request: Request) -> Response:
        deferred = self.crawler.engine.download(request=request)
        return await maybe_deferred_to_future(deferred)

    @abstractmethod
    async def post_login(self, response):
        raise NotImplementedError

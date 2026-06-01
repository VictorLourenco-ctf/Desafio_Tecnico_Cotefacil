import json

import scrapy

from avaliacao_cotefacil.spiders.login import LoginSpider
from avaliacao_cotefacil.suppliers.payloads import products


class ProductsSpider(LoginSpider):
    name = 'Products'
    product_url = 'https://peapi.servimed.com.br/api/carrinho/oculto?siteVersion=4.0.29'

    async def post_login(self, response):
        self.logger.info('Iniciando extracao dos produtos')
        user_response = response.json()
        page = 1
        total_pages = 1
        list_products = []


        while page <= total_pages:

            res = await self.inline_requests(scrapy.Request(
                url=self.product_url,
                method="POST",
                headers={
                    'Content-Type': 'application/json',
                    'accesstoken': self.get_access_token_id()
                },
                body=json.dumps(products(
                    page=page,
                    user_id=user_response['usuario']['codigoUsuario'],
                    user_external_id=user_response['usuario']['codigoExterno']
                )),
            ))

            if res.status < 300:
                parsed_body = res.json()

                if not parsed_body["lista"]:
                    break

                # total_pages = int(parsed_body["totalRegistros"] / parsed_body["registrosPorPagina"])
                page += 1
                list_products.extend(parsed_body["lista"])

        return self.parse_product(list_products)

    def parse_product(self, list_products):
        self.logger.info('Validando os produtos encontrados no fabricante')

        products = [{
            "gtin": product.get("codigoBarras", ""),
            "codigo": product.get("codigoExterno", ""),
            "descricao": product.get("descricao", ""),
            "preco_fabrica": product.get("valorBase", ""),
            "estoque": product.get("quantidadeEstoque", ""),
        } for product in list_products]

        with open ('produtos.json', 'w') as outfile:
            json.dump(products, outfile, indent=4, ensure_ascii=False)



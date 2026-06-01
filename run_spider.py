import argparse
import os

from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from avaliacao_cotefacil.spiders.products import ProductsSpider
from avaliacao_cotefacil.spiders.login import LoginSpider

load_dotenv()

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Executa o spider de produtos"
    )

    parser.add_argument(
        "--user",
        help="Usuário de acesso"
    )

    parser.add_argument(
        "--password",
        help="Senha de acesso"
    )

    args = parser.parse_args()

    if not os.getenv("USER") or not os.getenv("PASSWORD"):
        raise EnvironmentError()

    settings = get_project_settings()
    configure_logging(settings)
    process = CrawlerProcess(settings)
    process.crawl(
        ProductsSpider,
        user=args.user or os.getenv("USER"),
        password=args.password or os.getenv("PASSWORD")
    )
    process.start()

if __name__ == '__main__':
    main()

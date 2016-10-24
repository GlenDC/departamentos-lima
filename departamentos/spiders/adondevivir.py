# -*- coding: utf-8 -*-
import scrapy

from departamentos.items import Departamento


class DepartamentosAdondevivir(scrapy.Spider):
    name = 'adondevivir'
    start_urls = [
        'http://www.adondevivir.com/departamentos-en-alquiler-en-miraflores-con-1-habitacion-de-1500-a-2000-soles.html',
        'http://www.adondevivir.com/departamentos-en-alquiler-en-barranco-con-1-habitacion-de-1500-a-2000-soles.html'
    ]

    base = "http://www.adondevivir.com"
    start_page = 1

    def parse(self, response):
        for post in response.xpath("//*[@class='list-posts']/li"):
            yield Departamento(
                url = self.base + post.xpath('./@data-href').extract_first(),
                title = post.xpath('.//div[@class="post-text-desc"]/div/*[@class="post-title"]/a/text()').extract_first(),
            )

        next_page_url = response.xpath('//*[contains(@class, "pagination-action-next")]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

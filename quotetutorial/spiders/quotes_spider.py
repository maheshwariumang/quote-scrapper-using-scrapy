import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    """


    commands to run:
        scrapy crawl quotes --> variable=> name=quotes
        scrapy crawl quotes -o YOUR_JSON_FILENAME.json --> save output to file

        scrapy shell "http://quotes.toscrape.com/" --> open the debug mode on terminal

    """
    # Don't change the variable -> name and start_urls because scrapy.spider will search for it
    name = 'quotes'
    page_number = 1
    start_urls = [
        'http://quotes.toscrape.com/'
    ]  # list of urls

    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract_first()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items  # show what spider has extracted

        next_page = 'http://quotes.toscrape.com/page/{}/'.format(self.page_number)

        if self.page_number <= 11:
            self.page_number += 1
            print("****************************************************************************************************")
            yield response.follow(next_page, callback= self.parse)

    def parse_with_follow_page(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract_first()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items  # show what spider has extracted

        next_page = response.css('li.next a::attr(href)').get()  # scrapy automatic identify this

        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)

    def parse_without_page(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract_first()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items  # show what spider has extracted

    def parse_new_old(self, response):
        # title = response.css('title').extract()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tags::text').extract_first()
            # title = response.css('div').extract()
            yield {
                'title': title,
                'author': author,
                'tag': tag
            }  # show what spider has extracted

    def parse_old(self, response):
        """

        :param response:
        :return:


        response.css('title').extract() --> ['<title>Quotes to Scrape</title>']
        response.css('title::text').extract() --> ['Quotes to Scrape']  --> all title elements
        response.css('title::text').extract()[0] --> 'Quotes to Scrape'  --> can give an error if not present
        response.css('title::text')[0].extract() --> 'Quotes to Scrape'
        response.css('title::text').extract_first() --> 'Quotes to Scrape' -> if not present then provide None

        response.xpath('//span[@class="text"]/text()').extract() --> XPath

        response.css('a').xpath('@href').extract() --> combination of css and XPath

        """
        # title = response.css('title').extract()
        all_div_quotes = response.css('div.quote')
        title = all_div_quotes.css('span.text::text').extract_first()
        author = all_div_quotes.css('.author::text').extract_first()
        tag = all_div_quotes.css('.tags::text').extract_first()
        # title = response.css('div').extract()
        yield {
            'title': title,
            'author': author,
            'tag': tag
        }  # show what spider has extracted





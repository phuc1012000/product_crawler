from scrapy import Item, Field

class Product(Item):
    post_status = Field()
    product_type = Field()
    post_title = Field()
    post_content = Field()
    post_excerpt = Field()
    post_date = Field()
    sku = Field()
    regular_price = Field()
    attr_Size = Field()
    attribute_data_size = Field()
    product_url = Field()
    features = Field()
    model_note = Field()
    server_id = Field()
    collection = Field()
    name = Field()
    price_min = Field()
    price_max = Field()
    options = Field()
    images = Field()
    image_urls = Field()
    image_path_prefix = Field()
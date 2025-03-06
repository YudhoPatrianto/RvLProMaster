from telegraph import Telegraph


def CreatePagesTelegraph(
    title: str,
    short_name: str,
    content: str
):
    telegraph = Telegraph()
    telegraph.create_account(short_name=short_name)
    r = telegraph.create_page(
        title,
        html_content=content
    )
    return r['url']

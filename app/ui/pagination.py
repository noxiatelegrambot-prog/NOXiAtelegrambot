def paginate_items(items: list, page: int = 1, page_size: int = 5):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end], (end < len(items))

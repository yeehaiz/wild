import hashlib


def md5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


def paging_range(current, page_count, nav_count):
    if page_count <= nav_count:
        return range(1, page_count+1)

    start = current - nav_count/2
    end = start + nav_count

    if start < 1:
        return range(1, 1 + nav_count)

    if end > nav_count + 1:
        return range(page_count - nav_count + 1 , page_count + 1)

    return range(start, end)

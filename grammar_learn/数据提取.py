def get_title(annotations):
    title = []
    try:
        for item in annotations:
            if isinstance(item, str):
                if "title" == item:
                    if (
                        annotations["title"] is not None
                        and annotations["title"] not in title
                    ):
                        title.append(annotations["title"])
                continue
            if item is None:
                continue
            for key in item:
                if "title" == key:
                    if item[key] is not None and key not in title:
                        title.append(item[key])
                else:
                    info = item[key]
                    if isinstance(info, dict):
                        for key2 in info:
                            if "title" == key2:
                                if info[key2] is not None and key2 not in title:
                                    title.append(info[key2])
    except Exception as e:
        print(e)

    return title


mdict = {
    "annotations": [
        {
            "shooting": 1,
            "place": {"poiid": "8008632120000000000", "title": "泰州", "type": "checkin"},
            "client_mblogid": "06e53bc9-5b7d-40a2-9aac-139c79ef9bbf",
        },
        {"mapi_request": "true"},
    ]
}
print(get_title(mdict["annotations"]))

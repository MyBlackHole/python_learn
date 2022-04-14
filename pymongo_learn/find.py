from pymongo import MongoClient

# 服务链接
mongodb_link = MongoClient(host="127.0.0.1", port=27017, username="root", password="3edc#EDC")

# 集合选择
algorithm = mongodb_link['algorithm']

# 文档选择
teacher_text = algorithm['teacher_text']

data = {
    "sales_features": {
        "工作能力类型": "专业型",
    },
    "scenes_features": {
        "行业": "服装销售",
    },
    "_id": "41c872b09b6311ec860ee0d55eeff354"
}

find_map = {
    "工作能力类型": "全等",
    "行业": "全等",
}

# root = dict(data)

# def dict_parse(end, f_node, node_list):
#     for node in node_list:
#         end.append({node.title: f_node})
#         if node.child:
#             dict_parse(end, node, node.child)

# def dict_parse():
#     end = []
#     node_list = [] 
#     node_list_bat = []
#     for node in node_list:
#         child_list = node["child"]
#         if not child_list:
#             continue
#         for child in child_list:
#             end.append({child: node})
#             node_list_bat.append(child)
#         node_list = node_list_bat.copy()
#         node_list_bat = []
            
        
        
    

def data_map(_and:list, key:str, data:dict, find_map:dict):
    for key1 in data:
        value = data[key1]
        key_type = type(value)
        print(key_type)
        if key_type == str:
            find_type = find_map.get(key1, "全等")
            if find_type == "全等":
                _and.append({f"{key}{key1}": value})
            else:
                pass
            continue
        elif key_type != dict:
            continue
      
        data_map(_and, key = f"{key}{key1}.", data=value, find_map=find_map)


def find(link, data:dict, find_map:dict):
    _and = []
    data_map(_and, "", data, find_map)
    print(_and)
    return link.find({"$and":_and})



if __name__ == "__main__":
    print(list(find(teacher_text, data, find_map)))
    # sales_features = root["sales_features"]
    # print(id(sales_features))

    # sales_features = root["sales_features"]
    # print(id(sales_features))




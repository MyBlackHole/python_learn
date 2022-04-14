# from fastapi import FastAPI
# from elasticsearch import AsyncElasticsearch

# app = FastAPI()
# es = AsyncElasticsearch()


from elasticsearch import Elasticsearch

# from elasticsearch import AsyncElasticsearch

es = Elasticsearch(
    hosts=["http://192.168.1.59:9200"],
    basic_auth=("elastic", "sVi8O11xpp9q12v6l89Nn0om"),
)
# es = AsyncElasticsearch()

# # 创建 index
# es.indices.create(index = "test")
# # 删除 index
# es.indices.delete(index = 'test')


# # 插入数据
# es.index(index = "test", document={"id":1, "name":"小明"}, id = "1")
# # 可以不用指定id，create会自动添加id。
# es.create(index="test",id = "2", document={"id":2, "name":"小红"})


# # 删除指定数据
# es.delete(index='test', id="1")


# # 修改字段
# es.update(index = "test", id = "2", doc= {"name":"张三"})


# # 查询数据
# print(es.get(index = "test", id = "2"))
print(es.search(index="test", query={"match_all": {}}))
# 滚动分页的 func ，第四块部分 分页查询中 说明
# es.scroll(scroll_id = "scroll_id", scroll = "5m")

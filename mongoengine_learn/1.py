import datetime
import json

from mongoengine import (DateTimeField, Document, ListField, StringField,
                         connect)

connect("mydb", username="root", password="3edc#EDC")


class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {"collection": "BlogPost", "allow_inheritance": True}


class TextPost(BlogPost):
    content = StringField(required=True)
    # meta = {"collection": "TextPost", "allow_inheritance": True}


class LinkPost(BlogPost):
    url = StringField(required=True)


def add_test():
    post1 = TextPost(title="Using MongoEngine", content="See the tutorial")
    post1.tags = ["mongodb", "mongoengine"]
    post1.save()
    return post1.id


def first_test(_id):
    testpost = TextPost.objects(id=_id).first()
    print(testpost.to_mongo().to_dict())


def all_test():
    testpost_list = TextPost.objects().all()
    for testpost in testpost_list:
        testpost_dict = testpost.to_mongo().to_dict()
        print(testpost_dict)
        print(json.dumps(testpost_dict))


def update_test():
    pass


if __name__ == "__main__":
    # _id = add_test()
    # print(_id)
    # first_test(_id)

    all_test()

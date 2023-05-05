# -*- encoding:utf-8 -*-
# Author : Mr.Chen
# FileName : get_task.py
# Datetime : 2020/6/9  18:55
# FileDescribe :


import datetime
import json

from pymongo import MongoClient


class MongodbLink:
    def __init__(self):
        mongodb_link = MongoClient(host="192.168.100.148", port=27017)
        self.db = mongodb_link.gz_opinion


class GetTask:
    """
    获取任务

    result = [{'_id': ObjectId('5eddf8b701362a67de2f1461'), 'pattern': 1, 'target': 1,
           'taskLink': 'https://weibo.com/2002526824/J5HjOd0ag?ref=home&type=comment',
           'taskTitle': '关于留学的观点，请大家评论点赞转发', 'taskContent': '请按照各自阵营观点评论点赞转发', 'assessAmount': 40,
           'beginDate': '2020-06-08 16:37:00', 'signinMinute': 8, 'readyMinute': 3, 'battleMinute': 5,
           'assessRule2': {'_id': '5e76370a74ff173dab5b0c3d', 'create_user_node_id': '5e660ebd74ff177f4ec2edf5',
                           'ruleType': 2, 'created_user_id': '5e62490d74ff17559da433d6', 'checkWay': 2,
                           'created': '2020-03-21 15:47:22', 'updateon': '2020-06-08 03:21:29',
                           'company_id': '5e622ed274ff171d709e083a', 'create_date': '2020-03-21 23:47:22',
                           'disable': False, 'system_id': '5e622ed274ff171d709e0839', 'ruleName': '标准规格评分',
                           'create_user_name': 'hzwp_unit', 'user_node_id': '5e772cf774ff17611e738c16',
                           'user_alias': '测试账号', 'create_group_id': '5e6600da74ff177f4ec2ddca', 'isDefault': True},
           'ruleInfo': '{"ruleItems":[{"_id":"5eddaeb9b27617259d88e5bd","name":"热评","itemType":1,"settings":2,"score":4,"content":1,"_relation_":{"hzwpRule":"DBRef(\'hzwpRule\', ObjectId(\'5e76370a74ff173dab5b0c3d\'))"},"updateon":"2020-06-08 03:21:29","created":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","system_id":"5e622ed274ff171d709e0839","user_node_id":"5e9ec787fbf5c1adead8ca6a","user_alias":"管理员1","__parent_data__":{"hzwpRule":{"_id":"5e76370a74ff173dab5b0c3d","create_user_node_id":"5e660ebd74ff177f4ec2edf5","ruleType":2,"created_user_id":"5e62490d74ff17559da433d6","checkWay":2,"created":"2020-03-21 15:47:22","updateon":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","create_date":"2020-03-21 23:47:22","disable":false,"system_id":"5e622ed274ff171d709e0839","ruleName":"标准规格评分","create_user_name":"hzwp_unit","user_node_id":"5e772cf774ff17611e738c16","user_alias":"测试账号","create_group_id":"5e6600da74ff177f4ec2ddca","isDefault":true}}},{"_id":"5eddaeb9b27617259d88e5be","name":"评论","itemType":2,"settings":2,"score":3,"content":1,"_relation_":{"hzwpRule":"DBRef(\'hzwpRule\', ObjectId(\'5e76370a74ff173dab5b0c3d\'))"},"updateon":"2020-06-08 03:21:29","created":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","system_id":"5e622ed274ff171d709e0839","user_node_id":"5e9ec787fbf5c1adead8ca6a","user_alias":"管理员1","__parent_data__":{"hzwpRule":{"_id":"5e76370a74ff173dab5b0c3d","create_user_node_id":"5e660ebd74ff177f4ec2edf5","ruleType":2,"created_user_id":"5e62490d74ff17559da433d6","checkWay":2,"created":"2020-03-21 15:47:22","updateon":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","create_date":"2020-03-21 23:47:22","disable":false,"system_id":"5e622ed274ff171d709e0839","ruleName":"标准规格评分","create_user_name":"hzwp_unit","user_node_id":"5e772cf774ff17611e738c16","user_alias":"测试账号","create_group_id":"5e6600da74ff177f4ec2ddca","isDefault":true}}},{"_id":"5eddaeb9b27617259d88e5bf","name":"转发","itemType":3,"settings":2,"score":1,"content":1,"_relation_":{"hzwpRule":"DBRef(\'hzwpRule\', ObjectId(\'5e76370a74ff173dab5b0c3d\'))"},"updateon":"2020-06-08 03:21:29","created":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","system_id":"5e622ed274ff171d709e0839","user_node_id":"5e9ec787fbf5c1adead8ca6a","user_alias":"管理员1","__parent_data__":{"hzwpRule":{"_id":"5e76370a74ff173dab5b0c3d","create_user_node_id":"5e660ebd74ff177f4ec2edf5","ruleType":2,"created_user_id":"5e62490d74ff17559da433d6","checkWay":2,"created":"2020-03-21 15:47:22","updateon":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","create_date":"2020-03-21 23:47:22","disable":false,"system_id":"5e622ed274ff171d709e0839","ruleName":"标准规格评分","create_user_name":"hzwp_unit","user_node_id":"5e772cf774ff17611e738c16","user_alias":"测试账号","create_group_id":"5e6600da74ff177f4ec2ddca","isDefault":true}}},{"_id":"5eddaeb9b27617259d88e5c0","name":"点赞","itemType":4,"settings":2,"score":1,"content":1,"_relation_":{"hzwpRule":"DBRef(\'hzwpRule\', ObjectId(\'5e76370a74ff173dab5b0c3d\'))"},"updateon":"2020-06-08 03:21:29","created":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","system_id":"5e622ed274ff171d709e0839","user_node_id":"5e9ec787fbf5c1adead8ca6a","user_alias":"管理员1","__parent_data__":{"hzwpRule":{"_id":"5e76370a74ff173dab5b0c3d","create_user_node_id":"5e660ebd74ff177f4ec2edf5","ruleType":2,"created_user_id":"5e62490d74ff17559da433d6","checkWay":2,"created":"2020-03-21 15:47:22","updateon":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","create_date":"2020-03-21 23:47:22","disable":false,"system_id":"5e622ed274ff171d709e0839","ruleName":"标准规格评分","create_user_name":"hzwp_unit","user_node_id":"5e772cf774ff17611e738c16","user_alias":"测试账号","create_group_id":"5e6600da74ff177f4ec2ddca","isDefault":true}}},{"_id":"5eddaeb9b27617259d88e5c1","name":"出错","itemType":5,"settings":2,"score":0,"content":0,"itemIndex":0,"_relation_":{"hzwpRule":"DBRef(\'hzwpRule\', ObjectId(\'5e76370a74ff173dab5b0c3d\'))"},"updateon":"2020-06-08 03:21:29","created":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","system_id":"5e622ed274ff171d709e0839","user_node_id":"5e9ec787fbf5c1adead8ca6a","user_alias":"管理员1","__parent_data__":{"hzwpRule":{"_id":"5e76370a74ff173dab5b0c3d","create_user_node_id":"5e660ebd74ff177f4ec2edf5","ruleType":2,"created_user_id":"5e62490d74ff17559da433d6","checkWay":2,"created":"2020-03-21 15:47:22","updateon":"2020-06-08 03:21:29","company_id":"5e622ed274ff171d709e083a","create_date":"2020-03-21 23:47:22","disable":false,"system_id":"5e622ed274ff171d709e0839","ruleName":"标准规格评分","create_user_name":"hzwp_unit","user_node_id":"5e772cf774ff17611e738c16","user_alias":"测试账号","create_group_id":"5e6600da74ff177f4ec2ddca","isDefault":true}}}],"ruleName":"标准规格评分","ruleId":"5e76370a74ff173dab5b0c3d","checkWay":2}',
           'disable': False, 'type': 2, 'status': 4, 'isSend': 1, 'files': '[]',
           'assessRule': '5e76370a74ff173dab5b0c3d',
           '_relation_': {'hzwp_tasktype': DBRef('hzwp_tasktype', ObjectId('5e7b222f74ff177990cd7635'))},
           'updateon': datetime.datetime(2020, 6, 9, 8, 27, 34, 652000),
           'created': datetime.datetime(2020, 6, 9, 8, 27, 34, 652000), 'company_id': '5e622ed274ff171d709e083a',
           'system_id': '5e622ed274ff171d709e0839', 'user_node_id': '5eba6020ffd497875d5a0513', 'user_alias': '陶骥',
           'created_user_id': '5eba6020ffd497875d5a0511', 'create_group_id': '5e6600da74ff177f4ec2ddca',
           'create_user_name': 'hzwp_tj', 'create_user_node_id': '5eba6020ffd497875d5a0513',
           'create_date': '2020-06-08 16:37:11'}]
    """

    def __init__(self):
        self.db = MongodbLink().db

    def get_task_info(self, id, link, title, ruler, execute_time, process_time):
        join_war_nums = self.db.hzwpWariar.find({"task_id": str(id)})
        task_info_dict = {}
        task_info_dict["task_id"] = str(id)
        task_info_dict["link"] = link
        task_info_dict["title"] = title
        task_info_dict["usergroups"] = []
        temp_dict1 = {"red": []}
        temp_dict2 = {"blue": []}
        for join_war_num in join_war_nums:
            team = join_war_num.get("team")
            if team == "1":
                temp_dict1["red"].append(
                    str(json.loads(join_war_num["majia_info"])["uniqueid"])
                )
            elif team == "2":
                temp_dict2["blue"].append(
                    str(json.loads(join_war_num["majia_info"])["uniqueid"])
                )
        task_info_dict["usergroups"].append(temp_dict1)
        task_info_dict["usergroups"].append(temp_dict2)
        ruler_list = ruler["ruleItems"]
        task_info_dict["ruler"] = []

        temp_merge_data = {
            "hotlike": {},
            "reply": {},
            "forward": {},
            "like": {},
            "fault": [],
        }

        for per_ruler in ruler_list:
            ruler_dict = {}
            temp_dict3 = {}
            temp_dict4 = {}
            if per_ruler["itemType"] == 1:
                if per_ruler["settings"] == 1:
                    temp_dict4["min"] = per_ruler["gradientMin"]
                    temp_dict4["max"] = per_ruler["gradientMax"]
                    temp_dict4["grade"] = per_ruler["score"]
                    if not temp_merge_data["hotlike"]:
                        temp_dict3["type"] = "2"
                        temp_dict3["span"] = []
                        temp_dict3["span"].append(temp_dict4)
                        temp_merge_data["hotlike"] = temp_dict3
                    else:
                        temp_merge_data["hotlike"]["span"].append(temp_dict4)
                else:
                    temp_dict3["type"] = "1"
                    temp_dict3["score"] = per_ruler["score"]
                    ruler_dict["hotlike"] = temp_dict3
                    task_info_dict["ruler"].append(ruler_dict)
            elif per_ruler["itemType"] == 2:
                if per_ruler["settings"] == 1:
                    temp_dict4["min"] = per_ruler["gradientMin"]
                    temp_dict4["max"] = per_ruler["gradientMax"]
                    temp_dict4["grade"] = per_ruler["score"]
                    if not temp_merge_data["reply"]:
                        temp_dict3["type"] = "2"
                        temp_dict3["span"] = []
                        temp_dict3["span"].append(temp_dict4)
                        temp_merge_data["reply"] = temp_dict3
                    else:
                        temp_merge_data["reply"]["span"].append(temp_dict4)
                else:
                    temp_dict3["type"] = "1"
                    temp_dict3["score"] = per_ruler["score"]
                    ruler_dict["reply"] = temp_dict3
                task_info_dict["ruler"].append(ruler_dict)
            elif per_ruler["itemType"] == 3:
                if per_ruler["settings"] == 1:
                    temp_dict4["min"] = per_ruler["gradientMin"]
                    temp_dict4["max"] = per_ruler["gradientMax"]
                    temp_dict4["grade"] = per_ruler["score"]
                    if not temp_merge_data["forward"]:
                        temp_dict3["type"] = "2"
                        temp_dict3["span"] = []
                        temp_dict3["span"].append(temp_dict4)
                        temp_merge_data["forward"] = temp_dict3
                    else:
                        temp_merge_data["forward"]["span"].append(temp_dict4)
                else:
                    temp_dict3["type"] = "1"
                    temp_dict3["score"] = per_ruler["score"]
                    ruler_dict["forward"] = temp_dict3
                task_info_dict["ruler"].append(ruler_dict)
            elif per_ruler["itemType"] == 4:
                if per_ruler["settings"] == 1:
                    temp_dict4["min"] = per_ruler["gradientMin"]
                    temp_dict4["max"] = per_ruler["gradientMax"]
                    temp_dict4["grade"] = per_ruler["score"]
                    if not temp_merge_data["like"]:
                        temp_dict3["type"] = "2"
                        temp_dict3["span"] = []
                        temp_dict3["span"].append(temp_dict4)
                        temp_merge_data["like"] = temp_dict3
                    else:
                        temp_merge_data["like"]["span"].append(temp_dict4)
                else:
                    temp_dict3["type"] = "1"
                    temp_dict3["score"] = per_ruler["score"]
                    ruler_dict["like"] = temp_dict3
                task_info_dict["ruler"].append(ruler_dict)
            elif per_ruler["itemType"] == 5:
                if per_ruler["settings"] == 1:
                    temp_dict4["min"] = per_ruler["gradientMin"]
                    temp_dict4["max"] = per_ruler["gradientMax"]
                    temp_dict4["grade"] = abs(per_ruler["score"])
                    if not temp_merge_data["fault"]:
                        temp_dict3["type"] = "2"
                        temp_dict3["span"] = []
                        temp_dict3["span"].append(temp_dict4)
                        temp_dict3["fault_type"] = str(per_ruler["content"])
                        temp_merge_data["fault"] = [temp_dict3]
                    else:
                        for each in temp_merge_data["fault"]:
                            if each["type"] == "2":
                                each["span"].append(temp_dict4)
                else:
                    temp_dict3["type"] = "1"
                    temp_dict3["score"] = abs(per_ruler["score"])
                    temp_dict3["fault_type"] = str(per_ruler["content"])
                    temp_merge_data["fault"].append(temp_dict3)
                if ruler_dict:
                    task_info_dict["ruler"].append(ruler_dict)
        task_info_dict["execute_time"] = execute_time
        task_info_dict["process_time"] = process_time
        for key in temp_merge_data.keys():
            if temp_merge_data[key]:
                task_info_dict["ruler"].append({key: temp_merge_data[key]})
        return task_info_dict

    def query_task(self):
        now_time = (
            datetime.datetime.now()
            .replace(hour=0, minute=0, second=0)
            .strftime("%Y-%m-%d %H:%M:%S")
        )
        table_obj = self.db.hzwp_task
        res = table_obj.find({"create_date": {"$gt": now_time}}).sort(
            [("create_date", -1)]
        )
        task_list = list(res)
        task_info_list = []
        if task_list:
            for task_info in task_list:
                id = task_info["_id"]
                link = task_info.get("taskLink", "")
                title = task_info.get("taskTitle", "")
                ruler = task_info.get("ruleInfo")
                try:
                    ruler = json.loads(ruler)
                except Exception:
                    ruler = {}
                if ruler:
                    try:
                        # 抽取当前时间到开始时间的时间段
                        beginDate = task_info.get("beginDate", "")  # 任务发布时间
                        beginDate = datetime.datetime.strptime(
                            beginDate, "%Y-%m-%d %H:%M:%S"
                        )
                        current_time = datetime.datetime.today()  # 当前时间
                        # 抽取时长
                        signinMinute = task_info["signinMinute"]  # 签到时长
                        readyMinute = task_info["readyMinute"]  # 准备时长
                        battleMinute = task_info["battleMinute"]  # 比赛时长
                        # 设置区间，开启时间到当前时间的时长落到哪个区间
                        sign_max_time = beginDate + datetime.timedelta(
                            minutes=signinMinute
                        )
                        ready_max_time = sign_max_time + datetime.timedelta(
                            minutes=readyMinute
                        )
                        ongoing_max_time = ready_max_time + datetime.timedelta(
                            minutes=battleMinute
                        )
                        # 准备中:
                        if current_time.__gt__(
                            ready_max_time - datetime.timedelta(seconds=40)
                        ) and current_time.__le__(ongoing_max_time):
                            task_info = self.get_task_info(
                                id,
                                link,
                                title,
                                ruler,
                                str(ready_max_time),
                                str(ongoing_max_time),
                            )
                            task_info_list.append(task_info)
                    except Exception:
                        pass
        return task_info_list


if __name__ == "__main__":
    res = GetTask().query_task()
    if res:
        for i in res:
            print(i)
    else:
        print(res)
    # GetTask().test()

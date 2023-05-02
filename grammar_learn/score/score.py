#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          each_score
   Description:
   Author:             Black Hole
   date:               2020/7/27
-------------------------------------------------
   Change Activity:    2020/7/27:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from .entity.score_entity import MainForce


def count_all(task_id, count_list, request_time, ruler):
    """
    个人得分 -》 最后得分
    :return:total_score_list 最后要存入数据库的分数
    """
    team_dict = {}

    for each_person in count_list:
        res = count_source(data=each_person, request_time=request_time, ruler=ruler)
        team = res.get("team")
        # TODO 分组存储数据，计算分数
        team_list = team_dict.get(team)
        if team_list:
            team_list.append(res)
            team_dict[team] = team_list
        else:
            team_dict[team] = [res]

    total_score_list = structure(task_id, team_dict)
    return total_score_list


def count_leader(user_info, score_sum, people_num):
    """ 主力选手加分，给上 is_leader 标志 """
    score = user_info.get("score")
    uid = user_info.get("uid")
    if uid not in MainForce().main_force:
        if score > score_sum * 3 / people_num:
            user_info["score"] = score + 20
            user_info["is_leader"] = 1
            MainForce().main_force.append(uid)

            # # 记录插库
            # add_medal(self.task_id, self.request_time, uid, "MainForce", 1)

    else:
        user_info["score"] = score + 20
    return user_info


def structure(task_id, team_dict, over=1):
    total_score_list = []
    for k, v in team_dict.items():
        score_list = [i.get("score") for i in v]
        score_sum = sum(score_list)
        people_num = len(v)
        # 计算主力选手
        res_list = list(map(count_leader, v, [score_sum] * people_num, [people_num] * people_num))
        for each in res_list:
            task_id = task_id
            troop = each.get('team')
            unique_id = each.get('uid')
            timestamp = each.get('timestamp')
            reply = each.get('reply')
            comment = each.get('comment')
            forward = each.get('forward')
            like_comment = each.get('like_Comment')
            like_count = each.get('like_count')
            hot_like_count = each.get('hotlike_count')
            main_force = each.get('is_leader', 0)
            total_score = each.get('score')
            fault = each.get('fault_count')
            likegt50 = each.get('likegt50')
            firstlike = each.get('firstlike')
            firstcomment = each.get('firstcomment')
            firstforward = each.get('firstforward')
            value = (task_id, unique_id, troop, timestamp, like_comment, reply, comment,
                     forward, like_count, hot_like_count, main_force, total_score, fault, likegt50, firstlike,
                     firstcomment, firstforward, over)
            total_score_list.append(value)
    return total_score_list


def count_source(data, request_time, ruler):
    """
    统计个人分数
    """
    team = data.get("troop")
    uid = data.get("uniqueid")
    count_data = {
        "hotlike": data.get("hotlike_count"),
        "reply": data.get("comment_count") + data.get("reply"),
        "forward": data.get("forward_count"),
        "like_Comment": data.get("likeComment") + data.get("like_count"),
        "fault": (data.get("forward_count"), data.get("comment_count"), data.get("like_count"))
    }
    # TODO 根据规则计算的得分
    # 返回 错误数 和 个人分数
    error_count, res = RulerScore.check_type(ruler=ruler, count_data=count_data)

    res = res + data.get("medal_first_comment") * 10 + data.get("medal_first_forward") * 10 + data.get(
        "medal_first_like") * 10 + data.get("hotlike_count") * 10 + data.get("firsthotlike_count") * 20

    medal_data_info = {
        "team": team,
        "uid": uid,
        "timestamp": request_time,
        "score": res,
        "hotlike_count": data.get("hotlike_count"),
        "firsthotlike_count": data.get('firsthotlike_count'),
        "hotlike": data.get("hotlike_count"),
        "reply": data.get("reply"),
        "comment": data.get("comment_count"),
        "forward": data.get("forward_count"),
        "like_Comment": data.get("likeComment"),
        "like_count": data.get("like_count"),
        "fault_count": error_count,
        "likegt50": data.get('firsthotlike_count'),
        "firstlike": data.get('medal_first_like'),
        "firstcomment": data.get('medal_first_comment'),
        "firstforward": data.get('medal_first_forward')

    }
    return medal_data_info


class RulerScore:

    @staticmethod
    def check_type(ruler, count_data):
        fault_res, error_count = 0, 0
        hot_like_res, reply_res, forward_res, like_res = 0, 0, 0, 0
        # 获得每个相应规则的数量
        hot_like_data, reply_data, forward_data, like_data, fault_data = RulerScore.per_count(count_data=count_data)
        # 获得每个相应的规则
        hot_like_rule, reply_rule, forward_rule, like_rule, fault_rule = RulerScore.per_ruler(ruler=ruler)
        if hot_like_data:
            # 返回 错误数 和 分数
            error_hot_like, hot_like_res = RulerScore.count_method(hot_like_data, hot_like_rule)
        if reply_data:
            error_reply, reply_res = RulerScore.count_method(reply_data, reply_rule)
        if forward_data:
            error_forward, forward_res = RulerScore.count_method(forward_data, forward_rule)
        if like_data:
            error_like, like_res = RulerScore.count_method(like_data, like_rule)
        if fault_data:
            for each_ruler in fault_rule:
                per_error_count, per_fault_res = RulerScore.count_method(fault_data, each_ruler)
                fault_res += per_fault_res
                error_count += per_error_count
        result = hot_like_res + reply_res + forward_res + like_res - fault_res
        return error_count, result

    @staticmethod
    def count_method(data, rule_info):
        # TODO 传送改变
        type_ = rule_info.get("type")
        span = rule_info.get("span")
        score = rule_info.get("score")
        fault_type = rule_info.get("fault_type")
        if type_ == "1":
            error_count, res = RulerScore.fix_score(fault_type=fault_type, data=data, score=score)
        else:
            error_count, res = RulerScore.span_score(fault_type=fault_type, data=data, span=span)
        return error_count, res

    @staticmethod
    def per_count(count_data):
        hot_like_data = count_data.get("hotlike")
        reply_data = count_data.get("reply")
        forward_data = count_data.get("forward")
        like_data = count_data.get("like_Comment")
        fault_data = count_data.get("fault")
        return hot_like_data, reply_data, forward_data, like_data, fault_data

    @staticmethod
    def per_ruler(ruler):
        hot_like_rule = ruler[0].get("hotlike")
        reply_rule = ruler[1].get("reply")
        forward_rule = ruler[2].get("forward")
        like_rule = ruler[3].get("like")
        fault_rule = ruler[4].get("fault")
        return hot_like_rule, reply_rule, forward_rule, like_rule, fault_rule

    @staticmethod
    def fix_score(fault_type, data, score):
        error_count, res = 0, 0
        if fault_type:
            if fault_type == "1":
                res = data[-1] * score
                error_count = data[-1]
            elif fault_type == "2":
                res = data[1] * score
                error_count = data[1]
            elif fault_type == "3":
                res = data[0] * score
                error_count = data[0]
        else:
            res = data * score
        return error_count, res

    @staticmethod
    def span_score(fault_type, data, span):
        error_count, res = 0, 0
        if fault_type:
            count = 0
            if fault_type == "1":
                count = data[-1]
            elif fault_type == "2":
                count = data[1]
            elif fault_type == "3":
                count = data[0]
            error_count = count
        else:
            count = data
        for _dict in span:
            if count >= _dict['min']:
                calculate_count = _dict['max'] if count >= _dict['max'] else count
                res += _dict['grade'] * (calculate_count - _dict['min'] + 1)
        return error_count, res

# def add_medal(task_id, timestamp, unique_id, medal, value):
#     sql = 'INSERT INTO ' \
#           'battle_medal(taskid,`timing`,bloggerid, %s)' \
#           'values("%s",%s,%s,%s)' % (medal, task_id, timestamp, unique_id, value)
#     try:
#         execute(sql)
#         logger.info(f'{task_id}{medal}勋章sql数据添加成功')
#     except Exception as e:
#         logger.info('勋章存储数据错误，原因： %s' % e)
#         raise Exception('勋章存储数据错误，原因： %s' % e)

#!/user/bin/env python
# -*- coding: utf-8 -*-

import random


# 以模拟一个战斗角色为例。首先，创建游戏角色
class GameCharacter:
    def __init__(self):
        self.vitality = 0
        self.attack = 0
        self.defense = 0

    def display_state(self):
        print('Current Values:')
        print('Life:%d' % self.vitality)
        print('Attack:%d' % self.attack)
        print('Defence:%d' % self.defense)

    def init_state(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense

    def save_state(self):
        return Memento(self.vitality, self.attack, self.defense)

    def recover_state(self, mt):
        self.vitality = mt.vitality
        self.attack = mt.attack
        self.defense = mt.defense


class FightCt(GameCharacter):
    def fight(self):
        self.vitality -= random.randint(1, 10)


# GameCharacter定义了基本的生命值、攻击值、防御值以及实现角色状态控制的方法，FightCt实现具体的“战斗”接口。
# 为实现保存进度的细节，还需要一个备忘录，来保存进度。
class Memento:
    vitality = 0
    attack = 0
    defense = 0

    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense


# 业务逻辑中可以进行类的调度了
if __name__ == "__main__":
    game_ct = FightCt()
    game_ct.init_state(100, 79, 60)
    game_ct.display_state()
    memento = game_ct.save_state()
    game_ct.fight()
    game_ct.display_state()
    game_ct.recover_state(memento)
    game_ct.display_state()

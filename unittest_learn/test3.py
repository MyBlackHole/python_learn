import unittest


class TestLegion(unittest.TestCase):
    def setUp(self) -> None:
        print('WeiBoSpider 开始测试!!!')

    def tearDown(self) -> None:
        print('WeiBoSpider 测试结束!!!')
        print('*' * 30)

    def test_1_create_legion(self):
        # """
        # 创建军团
        # :return:
        # """
        # self.assertEqual(1, 1)
        print('创建军团')

    def test_2_bless(self):
        # """
        # 公会祈福
        # :return:
        # """
        # self.assertEqual(1, 1)
        print('公会祈福')

    def test_3_receive_bless_box(self):
        # """
        # 领取祈福宝箱
        # :return:
        # """
        # self.assertEqual(1, 1)
        print('领取祈福宝箱')

    def test_4_quit_legion(self):
        # """
        # 退出军团
        # :return:
        # """
        # self.assertEqual(1, 1)
        print('退出军团')


if __name__ == '__main__':
    unittest.main()

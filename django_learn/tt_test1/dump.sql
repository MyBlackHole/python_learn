-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Dong
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.19.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'商家用户权限'),(2,'用户权限');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,21),(2,1,22),(3,1,23),(4,1,24),(5,1,25),(6,1,26),(7,1,27),(8,1,28),(13,1,33),(14,1,34),(15,1,35),(16,1,36),(17,1,37),(18,1,38),(19,1,39),(20,1,40),(24,1,44),(29,2,45),(30,2,46),(31,2,47),(32,2,48),(33,2,53),(34,2,54),(35,2,55),(36,2,56);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 商品SPU',6,'add_goods'),(22,'Can change 商品SPU',6,'change_goods'),(23,'Can delete 商品SPU',6,'delete_goods'),(24,'Can view 商品SPU',6,'view_goods'),(25,'Can add 商品',7,'add_goodssku'),(26,'Can change 商品',7,'change_goodssku'),(27,'Can delete 商品',7,'delete_goodssku'),(28,'Can view 商品',7,'view_goodssku'),(29,'Can add 商品种类',8,'add_goodstype'),(30,'Can change 商品种类',8,'change_goodstype'),(31,'Can delete 商品种类',8,'delete_goodstype'),(32,'Can view 商品种类',8,'view_goodstype'),(33,'Can add 首页轮播商品',9,'add_indexgoodsbanner'),(34,'Can change 首页轮播商品',9,'change_indexgoodsbanner'),(35,'Can delete 首页轮播商品',9,'delete_indexgoodsbanner'),(36,'Can view 首页轮播商品',9,'view_indexgoodsbanner'),(37,'Can add 主页促销活动',10,'add_indexpromotionbanner'),(38,'Can change 主页促销活动',10,'change_indexpromotionbanner'),(39,'Can delete 主页促销活动',10,'delete_indexpromotionbanner'),(40,'Can view 主页促销活动',10,'view_indexpromotionbanner'),(41,'Can add 订单商品',11,'add_ordergoods'),(42,'Can change 订单商品',11,'change_ordergoods'),(43,'Can delete 订单商品',11,'delete_ordergoods'),(44,'Can view 订单商品',11,'view_ordergoods'),(45,'Can add 订单',12,'add_orderinfo'),(46,'Can change 订单',12,'change_orderinfo'),(47,'Can delete 订单',12,'delete_orderinfo'),(48,'Can view 订单',12,'view_orderinfo'),(49,'Can add 用户',13,'add_user'),(50,'Can change 用户',13,'change_user'),(51,'Can delete 用户',13,'delete_user'),(52,'Can view 用户',13,'view_user'),(53,'Can add 地址',14,'add_address'),(54,'Can change 地址',14,'change_address'),(55,'Can delete 地址',14,'delete_address'),(56,'Can view 地址',14,'view_address'),(57,'Can add task result',15,'add_taskresult'),(58,'Can change task result',15,'change_taskresult'),(59,'Can delete task result',15,'delete_taskresult'),(60,'Can view task result',15,'view_taskresult');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_address`
--

DROP TABLE IF EXISTS `df_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `receiver` varchar(20) NOT NULL,
  `addr` varchar(256) NOT NULL,
  `zip_code` varchar(6) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_address_user_id_5e6a5c8a_fk_df_user_id` (`user_id`),
  CONSTRAINT `df_address_user_id_5e6a5c8a_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_address`
--

LOCK TABLES `df_address` WRITE;
/*!40000 ALTER TABLE `df_address` DISABLE KEYS */;
INSERT INTO `df_address` VALUES (1,'2019-05-22 03:59:07.963101','2019-05-22 03:59:07.963303',0,'add','高冲街163-1号','543100','15077459464',1,1),(6,'2019-05-22 05:19:48.864013','2019-05-22 05:19:48.864051',0,'fffadd','高冲街163-1号','543100','15077459464',0,1),(7,'2019-05-25 06:48:58.242960','2019-05-25 06:48:58.243002',0,'add','高冲街163-1号','543100','15077459464',1,3),(8,'2019-05-27 11:10:04.639953','2019-05-27 11:10:04.639989',0,'add','高冲街163-1号','543100','15077459464',1,5);
/*!40000 ALTER TABLE `df_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_goods`
--

DROP TABLE IF EXISTS `df_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `detail` longtext NOT NULL,
  `merchant_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_goods_merchant_id_ce8b92ca_fk_df_user_id` (`merchant_id`),
  KEY `df_goods_type_id_81775372_fk_df_goods_type_id` (`type_id`),
  CONSTRAINT `df_goods_merchant_id_ce8b92ca_fk_df_user_id` FOREIGN KEY (`merchant_id`) REFERENCES `df_user` (`id`),
  CONSTRAINT `df_goods_type_id_81775372_fk_df_goods_type_id` FOREIGN KEY (`type_id`) REFERENCES `df_goods_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_goods`
--

LOCK TABLES `df_goods` WRITE;
/*!40000 ALTER TABLE `df_goods` DISABLE KEYS */;
INSERT INTO `df_goods` VALUES (1,'2019-05-22 02:18:39.873521','2019-05-27 09:51:35.297698',0,'苹果6','<p>六个苹果</p>',3,1,'group1/M00/00/00/wKgfBVzksM-AElQxAADN80inxaQ2161419'),(2,'2019-05-30 10:13:29.584957','2019-06-05 09:10:13.209422',0,'荔枝','<p>红色</p>',3,2,'group1/M00/00/00/wKgqMlz3hvWAW1TdAAAUOXKL9ao1667424');
/*!40000 ALTER TABLE `df_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_goods_sku`
--

DROP TABLE IF EXISTS `df_goods_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_goods_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `desc` varchar(256) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `unite` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `sales` int(11) NOT NULL,
  `status` smallint(6) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `merchant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_goods_sku_goods_id_31622280_fk_df_goods_id` (`goods_id`),
  KEY `df_goods_sku_merchant_id_2fd9fc1d_fk_df_user_id` (`merchant_id`),
  CONSTRAINT `df_goods_sku_goods_id_31622280_fk_df_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `df_goods` (`id`),
  CONSTRAINT `df_goods_sku_merchant_id_2fd9fc1d_fk_df_user_id` FOREIGN KEY (`merchant_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_goods_sku`
--

LOCK TABLES `df_goods_sku` WRITE;
/*!40000 ALTER TABLE `df_goods_sku` DISABLE KEYS */;
INSERT INTO `df_goods_sku` VALUES (6,'2019-05-22 03:41:59.269974','2019-06-05 01:20:17.347913',0,'黑色苹果6','朝昂贵的手机',6000.00,'1','group1/M00/00/00/wKgqMlz3GNGABeDWAAAT1MF3gjE1478114',36,4,1,1,3),(7,'2019-05-22 05:31:41.958184','2019-06-05 01:20:56.524031',0,'白色苹果6','朝昂贵的手机',6000.00,'1','group1/M00/00/00/wKgqMlz3GPiAJNA1AAAZG9TP4h47371904',14,1,1,1,3),(8,'2019-05-22 05:35:41.961782','2019-06-05 08:19:50.116439',0,'Black Hole','朝昂贵的手机',400.00,'1','group1/M00/00/00/wKgqMlz3eyaACQdLAAAhMyP_zn45867568',100,1,1,1,3),(9,'2019-05-22 05:36:51.573085','2019-06-05 08:20:08.113434',0,'Black Hole','朝昂贵的手机',5555.00,'1','group1/M00/00/00/wKgqMlz3eziAXZFcAAAJWdpcwV49229758',50,1,1,1,3),(10,'2019-05-26 08:50:26.399588','2019-06-05 01:17:40.622339',0,'苹果10','8个苹果',50.00,'1','group1/M00/00/00/wKgqMlz3GDSAdtQsAAASVS3KkA00982257',799,1,1,1,3),(11,'2019-05-30 10:14:48.016769','2019-06-05 01:17:02.182203',0,'梧州荔枝','果大核小',40.00,'1','group1/M00/00/00/wKgqMlz3GA6ADzm4AAAgQfrK7-88336220',122222,0,1,2,3);
/*!40000 ALTER TABLE `df_goods_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_goods_type`
--

DROP TABLE IF EXISTS `df_goods_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_goods_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `logo` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_goods_type`
--

LOCK TABLES `df_goods_type` WRITE;
/*!40000 ALTER TABLE `df_goods_type` DISABLE KEYS */;
INSERT INTO `df_goods_type` VALUES (1,'2019-05-22 02:15:43.755871','2019-06-05 01:05:07.209368',0,'手机','电子','group1/M00/00/00/wKgqMlz3FUOACDjWAAAO7phc2A87012745'),(2,'2019-05-30 10:12:15.074888','2019-06-05 01:04:54.597630',0,'水果','生鲜','group1/M00/00/00/wKgqMlz3FTaAQr94AAAgBAJA26w3679848'),(3,'2019-06-05 01:07:47.561527','2019-06-05 01:07:47.561566',0,'电子','不知道','group1/M00/00/00/wKgqMlz3FeOABSCHAAA0orhbY_I2476459');
/*!40000 ALTER TABLE `df_goods_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_index_banner`
--

DROP TABLE IF EXISTS `df_index_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_index_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `merchant_id` int(11) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_index_banner_merchant_id_4fff1887_fk_df_user_id` (`merchant_id`),
  KEY `df_index_banner_sku_id_57f2798e_fk_df_goods_sku_id` (`sku_id`),
  CONSTRAINT `df_index_banner_merchant_id_4fff1887_fk_df_user_id` FOREIGN KEY (`merchant_id`) REFERENCES `df_user` (`id`),
  CONSTRAINT `df_index_banner_sku_id_57f2798e_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_index_banner`
--

LOCK TABLES `df_index_banner` WRITE;
/*!40000 ALTER TABLE `df_index_banner` DISABLE KEYS */;
INSERT INTO `df_index_banner` VALUES (1,'2019-05-22 03:50:30.476900','2019-06-04 23:04:28.606417',0,'group1/M00/00/00/wKgqMlz2-PyAKoryAAAiLOQgXj85794785',3,6),(2,'2019-06-04 23:04:49.103987','2019-06-04 23:04:49.104017',0,'group1/M00/00/00/wKgqMlz2-RGAEg5AAAAnEYJk9ss8252791',3,7),(3,'2019-06-04 23:04:58.076220','2019-06-04 23:04:58.076271',0,'group1/M00/00/00/wKgqMlz2-RqAVvnNAAAwk6XWvxI4257227',3,8),(4,'2019-06-04 23:35:15.450865','2019-06-04 23:35:15.450906',0,'group1/M00/00/00/wKgqMlz3ADOAPBPuAAAnEYJk9ss9349828',3,10);
/*!40000 ALTER TABLE `df_index_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_index_promotion`
--

DROP TABLE IF EXISTS `df_index_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_index_promotion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `merchant_id` int(11) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_index_promotion_merchant_id_e8accbe0_fk_df_user_id` (`merchant_id`),
  KEY `df_index_promotion_sku_id_b1877aa9_fk_df_goods_sku_id` (`sku_id`),
  CONSTRAINT `df_index_promotion_merchant_id_e8accbe0_fk_df_user_id` FOREIGN KEY (`merchant_id`) REFERENCES `df_user` (`id`),
  CONSTRAINT `df_index_promotion_sku_id_b1877aa9_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_index_promotion`
--

LOCK TABLES `df_index_promotion` WRITE;
/*!40000 ALTER TABLE `df_index_promotion` DISABLE KEYS */;
INSERT INTO `df_index_promotion` VALUES (1,'2019-06-05 08:43:49.160980','2019-06-05 08:43:49.161014',0,'s123','group1/M00/00/00/wKgqMlz3gMWAOZVNAAAOilwtZbQ5280332',3,6);
/*!40000 ALTER TABLE `df_index_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_order_goods`
--

DROP TABLE IF EXISTS `df_order_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_order_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `count` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `comment` varchar(256) NOT NULL,
  `order_id` varchar(128) NOT NULL,
  `sku_id` int(11) NOT NULL,
  `order_status` smallint(6) NOT NULL,
  `merchant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_order_goods_order_id_6958ee23_fk_df_order_info_order_id` (`order_id`),
  KEY `df_order_goods_sku_id_b7d6e04e_fk_df_goods_sku_id` (`sku_id`),
  KEY `df_order_goods_merchant_id_5158c626_fk_df_user_id` (`merchant_id`),
  CONSTRAINT `df_order_goods_merchant_id_5158c626_fk_df_user_id` FOREIGN KEY (`merchant_id`) REFERENCES `df_user` (`id`),
  CONSTRAINT `df_order_goods_order_id_6958ee23_fk_df_order_info_order_id` FOREIGN KEY (`order_id`) REFERENCES `df_order_info` (`order_id`),
  CONSTRAINT `df_order_goods_sku_id_b7d6e04e_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_order_goods`
--

LOCK TABLES `df_order_goods` WRITE;
/*!40000 ALTER TABLE `df_order_goods` DISABLE KEYS */;
INSERT INTO `df_order_goods` VALUES (1,'2019-05-25 08:10:17.778477','2019-05-30 02:21:11.998681',0,2,6000.00,'123','201905251610173',6,1,3),(2,'2019-05-25 08:10:17.781461','2019-05-30 02:21:18.925687',0,1,400.00,'123','201905251610173',8,1,3),(3,'2019-05-25 08:10:17.785424','2019-05-30 02:21:49.888857',0,1,5555.00,'123','201905251610173',9,1,3),(4,'2019-05-26 02:21:32.964460','2019-05-30 02:21:43.738106',0,1,6000.00,'123','201905261021323',6,2,3),(5,'2019-05-26 08:26:14.641068','2019-05-30 02:21:35.941210',0,1,6000.00,'jkjfkajhdsfkgaskld和夫斯基的和罚款空间和罚款的和健康三等奖哈佛','201905261626143',7,5,3),(7,'2019-05-26 08:51:24.247398','2019-05-26 10:02:30.891139',0,1,50.00,'','201905261651241',10,4,3),(8,'2019-05-27 11:22:19.152060','2019-05-30 02:21:25.246185',0,1,6000.00,'123','201905271922195',6,2,3);
/*!40000 ALTER TABLE `df_order_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_order_info`
--

DROP TABLE IF EXISTS `df_order_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_order_info` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `order_id` varchar(128) NOT NULL,
  `pay_method` smallint(6) NOT NULL,
  `total_count` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `transit_price` decimal(10,2) NOT NULL,
  `trade_no` varchar(128) NOT NULL,
  `addr_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `pay_status` smallint(6) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `df_order_info_addr_id_70c3726e_fk_df_address_id` (`addr_id`),
  KEY `df_order_info_user_id_ac1e5bf5_fk_df_user_id` (`user_id`),
  CONSTRAINT `df_order_info_addr_id_70c3726e_fk_df_address_id` FOREIGN KEY (`addr_id`) REFERENCES `df_address` (`id`),
  CONSTRAINT `df_order_info_user_id_ac1e5bf5_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_order_info`
--

LOCK TABLES `df_order_info` WRITE;
/*!40000 ALTER TABLE `df_order_info` DISABLE KEYS */;
INSERT INTO `df_order_info` VALUES ('2019-05-25 08:10:17.766461','2019-05-26 01:21:56.613169',0,'201905251610173',1,4,17955.00,10.00,'1',7,3,1),('2019-05-26 02:21:32.958679','2019-05-26 07:37:26.147501',0,'201905261021323',1,1,6000.00,10.00,'1',7,3,2),('2019-05-26 08:26:14.606079','2019-05-26 09:13:28.035093',0,'201905261626143',1,1,6000.00,10.00,'1',7,3,2),('2019-05-26 08:51:24.242634','2019-05-26 09:59:03.497133',0,'201905261651241',1,1,50.00,10.00,'1',1,1,2),('2019-05-27 11:22:19.146229','2019-05-27 11:48:39.541990',0,'201905271922195',1,1,6000.00,10.00,'1',8,5,2);
/*!40000 ALTER TABLE `df_order_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user`
--

DROP TABLE IF EXISTS `df_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `is_merchant` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user`
--

LOCK TABLES `df_user` WRITE;
/*!40000 ALTER TABLE `df_user` DISABLE KEYS */;
INSERT INTO `df_user` VALUES (1,'pbkdf2_sha256$120000$cc2Rrr2ZGHOe$xHHfUmYuoCNtKtkFNK9RIbto0xmu8uR9G55C+Uh91Sk=','2019-06-05 01:00:58.780256',1,'admin','','','1358244533@qq.com',1,1,'2019-05-21 23:12:43.644840','2019-05-21 23:12:43.713515','2019-05-21 23:12:43.713537',0,0),(3,'pbkdf2_sha256$120000$aLC1bE7vwHp5$xe+r12RdkWzTIsAWp8uak7dfMrfJCNrXOurNVy/lnks=','2019-06-05 08:43:23.822466',0,'king','','','1358244533@qq.com',1,1,'2019-05-23 07:27:06.583608','2019-05-23 07:27:06.653142','2019-05-23 07:27:06.667873',0,1),(4,'pbkdf2_sha256$120000$mql55JwLvOYg$vyR3ZVS1dTTvLrLvG5fDPegSvrc7Sn1zDzAu/hD6NbU=','2019-05-26 09:57:17.883450',0,'kings','','','1358244533@qq.com',0,1,'2019-05-26 08:52:41.180737','2019-05-26 08:52:41.249729','2019-05-26 08:52:41.263652',0,0),(5,'pbkdf2_sha256$120000$YoGsKzhk2bKj$ckUhshzuOdoyXS+CMHN4JGh6HOtAdC23e4byrbfXIzA=','2019-05-31 07:35:17.018118',0,'测试一','','','1358244533@qq.com',0,1,'2019-05-27 07:37:38.658216','2019-05-27 07:37:38.727656','2019-05-27 07:37:38.744644',0,0),(7,'pbkdf2_sha256$120000$mg8bRxP7nNeF$aRy2knqbGUx7HGAJ2IwT0VcG3vUPwoml52PQF0t5gJg=','2019-05-27 11:50:28.300392',0,'测试五','','','1358244533@qq.com',0,1,'2019-05-27 08:26:17.522835','2019-05-27 08:26:17.595642','2019-05-27 08:26:17.610570',0,1),(8,'pbkdf2_sha256$120000$0TtiYvkwNwoD$LEkd43+wvezssf+IIr0Ta3SlL+smVkRBZkwQfvmK3TE=',NULL,0,'测试二','','','1358244533@qq.com',0,0,'2019-05-27 09:01:08.598948','2019-05-27 09:01:08.669920','2019-05-27 09:01:08.685011',0,0),(9,'pbkdf2_sha256$120000$Nl5HQX1mbafD$TRiGnBA6wpphP4pnKzjXLhwP+y9WPKmz2/487boq8NU=',NULL,0,'测试六','','','1358244533@qq.com',0,0,'2019-05-27 09:01:26.202470','2019-05-27 09:01:26.273495','2019-05-27 09:01:26.279250',0,1),(11,'pbkdf2_sha256$120000$T4rYzw3zyh97$Or+MwV2juZBU6OOq/GmasinVzthfBgtWThRksxRXpF4=',NULL,0,'kingss','','','1358244533@qq.com',0,0,'2019-05-28 02:18:03.561053','2019-05-28 02:18:03.630199','2019-05-28 02:18:03.645691',0,0);
/*!40000 ALTER TABLE `df_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user_groups`
--

DROP TABLE IF EXISTS `df_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `df_user_groups_user_id_group_id_80e5ab91_uniq` (`user_id`,`group_id`),
  KEY `df_user_groups_group_id_36f24e94_fk_auth_group_id` (`group_id`),
  CONSTRAINT `df_user_groups_group_id_36f24e94_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `df_user_groups_user_id_a816b098_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user_groups`
--

LOCK TABLES `df_user_groups` WRITE;
/*!40000 ALTER TABLE `df_user_groups` DISABLE KEYS */;
INSERT INTO `df_user_groups` VALUES (1,3,1);
/*!40000 ALTER TABLE `df_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user_user_permissions`
--

DROP TABLE IF EXISTS `df_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `df_user_user_permissions_user_id_permission_id_b22997de_uniq` (`user_id`,`permission_id`),
  KEY `df_user_user_permiss_permission_id_40a6cb2d_fk_auth_perm` (`permission_id`),
  CONSTRAINT `df_user_user_permiss_permission_id_40a6cb2d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `df_user_user_permissions_user_id_b5f6551b_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user_user_permissions`
--

LOCK TABLES `df_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `df_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_df_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-05-22 02:06:07.116082','2','black',1,'[{\"added\": {}}]',13,1),(2,'2019-05-22 02:15:43.829977','1','手机',1,'[{\"added\": {}}]',8,1),(3,'2019-05-22 02:18:39.904108','1','Goods object (1)',1,'[{\"added\": {}}]',6,1),(4,'2019-05-22 03:41:59.352667','6','GoodsSKU object (6)',1,'[{\"added\": {}}]',7,1),(5,'2019-05-22 03:50:30.563715','1','IndexGoodsBanner object (1)',1,'[{\"added\": {}}]',9,1),(6,'2019-05-22 05:31:42.657817','7','GoodsSKU object (7)',1,'[{\"added\": {}}]',7,1),(7,'2019-05-22 05:35:42.687961','8','GoodsSKU object (8)',1,'[{\"added\": {}}]',7,1),(8,'2019-05-22 05:36:51.589097','9','GoodsSKU object (9)',1,'[{\"added\": {}}]',7,1),(9,'2019-05-26 08:50:27.178509','10','苹果8',1,'[{\"added\": {}}]',7,1),(10,'2019-05-27 09:45:07.880517','1','手机',2,'[{\"changed\": {\"fields\": [\"logo\"]}}]',8,1),(11,'2019-05-27 09:51:35.300266','1','苹果6',2,'[{\"changed\": {\"fields\": [\"detail\"]}}]',6,1),(12,'2019-05-30 02:19:24.929280','9','Black Hole',2,'[{\"changed\": {\"fields\": [\"merchant\"]}}]',7,1),(13,'2019-05-30 02:19:32.070267','8','Black Hole',2,'[{\"changed\": {\"fields\": [\"merchant\"]}}]',7,1),(14,'2019-05-30 02:19:40.528277','9','Black Hole',2,'[{\"changed\": {\"fields\": [\"stock\"]}}]',7,1),(15,'2019-05-30 02:19:48.019482','8','Black Hole',2,'[{\"changed\": {\"fields\": [\"stock\"]}}]',7,1),(16,'2019-05-30 02:19:58.220287','7','白色苹果6',2,'[{\"changed\": {\"fields\": [\"merchant\"]}}]',7,1),(17,'2019-05-30 02:20:03.664924','6','黑色苹果6',2,'[{\"changed\": {\"fields\": [\"merchant\"]}}]',7,1),(18,'2019-05-30 02:20:46.938654','1','king',2,'[{\"changed\": {\"fields\": [\"merchant\"]}}]',9,1),(19,'2019-05-30 02:21:12.000416','1','OrderGoods object (1)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(20,'2019-05-30 02:21:18.928046','2','OrderGoods object (2)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(21,'2019-05-30 02:21:25.247885','8','OrderGoods object (8)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(22,'2019-05-30 02:21:35.942936','5','OrderGoods object (5)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(23,'2019-05-30 02:21:43.740203','4','OrderGoods object (4)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(24,'2019-05-30 02:21:49.890746','3','OrderGoods object (3)',2,'[{\"changed\": {\"fields\": [\"merchant\", \"comment\"]}}]',11,1),(25,'2019-05-30 02:22:20.877143','2','black',3,'',13,1),(26,'2019-05-30 02:38:42.669016','1','商家用户权限',1,'[{\"added\": {}}]',3,1),(27,'2019-05-30 02:39:45.672937','1','商家用户权限',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(28,'2019-05-30 02:40:31.563650','2','用户权限',1,'[{\"added\": {}}]',3,1),(29,'2019-05-30 10:12:15.120138','2','水果',1,'[{\"added\": {}}]',8,1),(30,'2019-05-30 10:13:29.588123','2','荔枝',1,'[{\"added\": {}}]',6,1),(31,'2019-05-30 10:14:48.717783','11','梧州荔枝',1,'[{\"added\": {}}]',7,1),(32,'2019-05-31 09:32:27.927821','1','商家用户权限',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(33,'2019-05-31 11:03:35.291694','10','苹果10',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',7,3),(34,'2019-06-04 23:04:28.650837','1','king',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',9,3),(35,'2019-06-04 23:04:49.108169','2','king',1,'[{\"added\": {}}]',9,3),(36,'2019-06-04 23:04:58.080482','3','king',1,'[{\"added\": {}}]',9,3),(37,'2019-06-04 23:35:15.606293','4','king',1,'[{\"added\": {}}]',9,3),(38,'2019-06-05 01:04:54.603628','2','水果',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',8,1),(39,'2019-06-05 01:05:07.328887','1','手机',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',8,1),(40,'2019-06-05 01:07:47.598369','3','电子',1,'[{\"added\": {}}]',8,1),(41,'2019-06-05 01:17:03.081911','11','梧州荔枝',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(42,'2019-06-05 01:17:40.635977','10','苹果10',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(43,'2019-06-05 01:20:17.378056','6','黑色苹果6',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(44,'2019-06-05 01:20:56.535966','7','白色苹果6',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(45,'2019-06-05 08:17:05.689856','9','Black Hole',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(46,'2019-06-05 08:19:50.130737','8','Black Hole',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(47,'2019-06-05 08:20:08.123730','9','Black Hole',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',7,1),(48,'2019-06-05 08:43:49.164871','1','s123',1,'[{\"added\": {}}]',10,3),(49,'2019-06-05 09:10:13.213741','2','荔枝',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',6,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_results_taskresult`
--

DROP TABLE IF EXISTS `django_celery_results_taskresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_results_taskresult` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  `task_args` longtext,
  `task_kwargs` longtext,
  `task_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `django_celery_results_taskresult_hidden_cd77412f` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_results_taskresult`
--

LOCK TABLES `django_celery_results_taskresult` WRITE;
/*!40000 ALTER TABLE `django_celery_results_taskresult` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_results_taskresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(15,'django_celery_results','taskresult'),(6,'goods','goods'),(7,'goods','goodssku'),(8,'goods','goodstype'),(9,'goods','indexgoodsbanner'),(10,'goods','indexpromotionbanner'),(11,'order','ordergoods'),(12,'order','orderinfo'),(5,'sessions','session'),(14,'user','address'),(13,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-05-21 23:08:48.102048'),(2,'contenttypes','0002_remove_content_type_name','2019-05-21 23:08:48.146904'),(3,'auth','0001_initial','2019-05-21 23:08:48.297921'),(4,'auth','0002_alter_permission_name_max_length','2019-05-21 23:08:48.327562'),(5,'auth','0003_alter_user_email_max_length','2019-05-21 23:08:48.332673'),(6,'auth','0004_alter_user_username_opts','2019-05-21 23:08:48.338510'),(7,'auth','0005_alter_user_last_login_null','2019-05-21 23:08:48.344004'),(8,'auth','0006_require_contenttypes_0002','2019-05-21 23:08:48.346696'),(9,'auth','0007_alter_validators_add_error_messages','2019-05-21 23:08:48.351770'),(10,'auth','0008_alter_user_username_max_length','2019-05-21 23:08:48.357482'),(11,'auth','0009_alter_user_last_name_max_length','2019-05-21 23:08:48.363395'),(12,'user','0001_initial','2019-05-21 23:08:48.618044'),(13,'admin','0001_initial','2019-05-21 23:08:48.705031'),(14,'admin','0002_logentry_remove_auto_add','2019-05-21 23:08:48.718361'),(15,'admin','0003_logentry_add_action_flag_choices','2019-05-21 23:08:48.727514'),(16,'django_celery_results','0001_initial','2019-05-21 23:08:48.760954'),(17,'django_celery_results','0002_add_task_name_args_kwargs','2019-05-21 23:08:48.841444'),(18,'django_celery_results','0003_auto_20181106_1101','2019-05-21 23:08:48.848116'),(19,'goods','0001_initial','2019-05-21 23:08:48.948553'),(20,'goods','0002_auto_20190522_0708','2019-05-21 23:08:49.396835'),(21,'order','0001_initial','2019-05-21 23:08:49.435616'),(22,'order','0002_auto_20190522_0708','2019-05-21 23:08:49.731493'),(23,'sessions','0001_initial','2019-05-21 23:08:49.753818'),(24,'goods','0003_remove_indexgoodsbanner_index','2019-05-22 03:50:04.756310'),(25,'user','0002_auto_20190522_1149','2019-05-22 03:50:04.775063'),(26,'goods','0004_remove_goodssku_merchant','2019-05-24 12:46:29.660234'),(27,'goods','0005_goodssku_merchant','2019-05-24 04:52:19.459322'),(28,'order','0003_remove_orderinfo_merchant','2019-05-24 04:53:42.143402'),(29,'order','0004_ordergoods_order_status','2019-05-26 02:18:37.452857'),(30,'order','0005_remove_orderinfo_order_status','2019-05-26 02:19:09.395205'),(31,'order','0006_orderinfo_pay_status','2019-05-26 02:30:16.200105'),(32,'order','0007_ordergoods_merchant','2019-05-26 07:59:52.173740'),(33,'goods','0006_auto_20190527_1729','2019-05-27 09:29:31.953321'),(34,'goods','0007_goods_image','2019-05-27 16:10:09.188181');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-07  8:04:54

-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: test6
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.10.2-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group`
(
  `id`   int(11)     NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group`
  DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions`
(
  `id`            int(11) NOT NULL AUTO_INCREMENT,
  `group_id`      int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`, `permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions`
  DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission`
(
  `id`              int(11)      NOT NULL AUTO_INCREMENT,
  `name`            varchar(255) NOT NULL,
  `content_type_id` int(11)      NOT NULL,
  `codename`        varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`, `codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 33
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission`
  DISABLE KEYS */;
INSERT INTO `auth_permission`
VALUES (1, 'Can add log entry', 1, 'add_logentry'),
       (2, 'Can change log entry', 1, 'change_logentry'),
       (3, 'Can delete log entry', 1, 'delete_logentry'),
       (4, 'Can view log entry', 1, 'view_logentry'),
       (5, 'Can add permission', 2, 'add_permission'),
       (6, 'Can change permission', 2, 'change_permission'),
       (7, 'Can delete permission', 2, 'delete_permission'),
       (8, 'Can view permission', 2, 'view_permission'),
       (9, 'Can add group', 3, 'add_group'),
       (10, 'Can change group', 3, 'change_group'),
       (11, 'Can delete group', 3, 'delete_group'),
       (12, 'Can view group', 3, 'view_group'),
       (13, 'Can add user', 4, 'add_user'),
       (14, 'Can change user', 4, 'change_user'),
       (15, 'Can delete user', 4, 'delete_user'),
       (16, 'Can view user', 4, 'view_user'),
       (17, 'Can add content type', 5, 'add_contenttype'),
       (18, 'Can change content type', 5, 'change_contenttype'),
       (19, 'Can delete content type', 5, 'delete_contenttype'),
       (20, 'Can view content type', 5, 'view_contenttype'),
       (21, 'Can add session', 6, 'add_session'),
       (22, 'Can change session', 6, 'change_session'),
       (23, 'Can delete session', 6, 'delete_session'),
       (24, 'Can view session', 6, 'view_session'),
       (25, 'Can add good info', 7, 'add_goodinfo'),
       (26, 'Can change good info', 7, 'change_goodinfo'),
       (27, 'Can delete good info', 7, 'delete_goodinfo'),
       (28, 'Can view good info', 7, 'view_goodinfo'),
       (29, 'Can add goods info', 7, 'add_goodsinfo'),
       (30, 'Can change goods info', 7, 'change_goodsinfo'),
       (31, 'Can delete goods info', 7, 'delete_goodsinfo'),
       (32, 'Can view goods info', 7, 'view_goodsinfo');
/*!40000 ALTER TABLE `auth_permission`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user`
(
  `id`           int(11)      NOT NULL AUTO_INCREMENT,
  `password`     varchar(128) NOT NULL,
  `last_login`   datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1)   NOT NULL,
  `username`     varchar(150) NOT NULL,
  `first_name`   varchar(30)  NOT NULL,
  `last_name`    varchar(150) NOT NULL,
  `email`        varchar(254) NOT NULL,
  `is_staff`     tinyint(1)   NOT NULL,
  `is_active`    tinyint(1)   NOT NULL,
  `date_joined`  datetime(6)  NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 2
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user`
  DISABLE KEYS */;
INSERT INTO `auth_user`
VALUES (1, 'pbkdf2_sha256$120000$TFWatbUVuWLg$SI2a3GtRnurY32bRf0GdaR8BVw6L0la+sXQm2V2+W+E=',
        '2019-03-15 02:24:03.725739', 1, 'black', '', '', '1358244533@qq.com', 1, 1, '2019-03-15 02:23:14.790637');
/*!40000 ALTER TABLE `auth_user`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups`
(
  `id`       int(11) NOT NULL AUTO_INCREMENT,
  `user_id`  int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`, `group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups`
  DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions`
(
  `id`            int(11) NOT NULL AUTO_INCREMENT,
  `user_id`       int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`, `permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions`
  DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_goodsinfo`
--

DROP TABLE IF EXISTS `booktest_goodsinfo`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_goodsinfo`
(
  `id`       int(11)  NOT NULL AUTO_INCREMENT,
  `gcontent` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 5
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_goodsinfo`
--

LOCK TABLES `booktest_goodsinfo` WRITE;
/*!40000 ALTER TABLE `booktest_goodsinfo`
  DISABLE KEYS */;
INSERT INTO `booktest_goodsinfo`
VALUES (1, '<p>我爱中国</p>\r\n<p>中国爱我</p>'),
       (2, '<p>爱我中华</p>'),
       (3, '<p>中华爱我，国家</p>'),
       (4, '<p>ghjgh</p>\r\n<p>fhgf国家和</p>\r\n<p><img src=\"456456\" alt=\"\" /></p>');
/*!40000 ALTER TABLE `booktest_goodsinfo`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log`
(
  `id`              int(11)              NOT NULL AUTO_INCREMENT,
  `action_time`     datetime(6)          NOT NULL,
  `object_id`       longtext,
  `object_repr`     varchar(200)         NOT NULL,
  `action_flag`     smallint(5) unsigned NOT NULL,
  `change_message`  longtext             NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id`         int(11)              NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 6
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log`
  DISABLE KEYS */;
INSERT INTO `django_admin_log`
VALUES (1, '2019-03-15 02:24:37.370514', '1', 'GoodsInfo object (1)', 1, '[{\"added\": {}}]', 7, 1),
       (2, '2019-03-15 02:24:52.245790', '2', 'GoodsInfo object (2)', 1, '[{\"added\": {}}]', 7, 1),
       (3, '2019-03-15 02:25:02.725939', '3', 'GoodsInfo object (3)', 1, '[{\"added\": {}}]', 7, 1),
       (4, '2019-03-15 02:30:30.812359', '4', 'GoodsInfo object (4)', 1, '[{\"added\": {}}]', 7, 1),
       (5, '2019-03-15 02:31:19.942991', '3', 'GoodsInfo object (3)', 2,
        '[{\"changed\": {\"fields\": [\"gcontent\"]}}]', 7, 1);
/*!40000 ALTER TABLE `django_admin_log`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type`
(
  `id`        int(11)      NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model`     varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`, `model`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 8
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type`
  DISABLE KEYS */;
INSERT INTO `django_content_type`
VALUES (1, 'admin', 'logentry'),
       (3, 'auth', 'group'),
       (2, 'auth', 'permission'),
       (4, 'auth', 'user'),
       (7, 'booktest', 'goodsinfo'),
       (5, 'contenttypes', 'contenttype'),
       (6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations`
(
  `id`      int(11)      NOT NULL AUTO_INCREMENT,
  `app`     varchar(255) NOT NULL,
  `name`    varchar(255) NOT NULL,
  `applied` datetime(6)  NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 18
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations`
  DISABLE KEYS */;
INSERT INTO `django_migrations`
VALUES (1, 'contenttypes', '0001_initial', '2019-03-15 02:20:56.950171'),
       (2, 'auth', '0001_initial', '2019-03-15 02:20:57.286170'),
       (3, 'admin', '0001_initial', '2019-03-15 02:20:57.362097'),
       (4, 'admin', '0002_logentry_remove_auto_add', '2019-03-15 02:20:57.373552'),
       (5, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-15 02:20:57.382475'),
       (6, 'contenttypes', '0002_remove_content_type_name', '2019-03-15 02:20:57.441708'),
       (7, 'auth', '0002_alter_permission_name_max_length', '2019-03-15 02:20:57.476620'),
       (8, 'auth', '0003_alter_user_email_max_length', '2019-03-15 02:20:57.516978'),
       (9, 'auth', '0004_alter_user_username_opts', '2019-03-15 02:20:57.528143'),
       (10, 'auth', '0005_alter_user_last_login_null', '2019-03-15 02:20:57.555091'),
       (11, 'auth', '0006_require_contenttypes_0002', '2019-03-15 02:20:57.558463'),
       (12, 'auth', '0007_alter_validators_add_error_messages', '2019-03-15 02:20:57.572091'),
       (13, 'auth', '0008_alter_user_username_max_length', '2019-03-15 02:20:57.606683'),
       (14, 'auth', '0009_alter_user_last_name_max_length', '2019-03-15 02:20:57.645072'),
       (15, 'booktest', '0001_initial', '2019-03-15 02:20:57.659977'),
       (16, 'sessions', '0001_initial', '2019-03-15 02:20:57.684943'),
       (17, 'booktest', '0002_auto_20190315_1021', '2019-03-15 02:22:14.498921');
/*!40000 ALTER TABLE `django_migrations`
  ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session`
(
  `session_key`  varchar(40) NOT NULL,
  `session_data` longtext    NOT NULL,
  `expire_date`  datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session`
  DISABLE KEYS */;
INSERT INTO `django_session`
VALUES ('fohn71lts2hhxw09arys9vux4bremtcc',
        'NmFjNzQwZDViZWQyMGFkZjNiZjU4ZjZhZTAxYjI5MjY4YzhjNmViYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTFiYjM0YzdiMmNiNDExMzFkOTExMzFkZjFhMzRkNTRkZTU5YTUyIn0=',
        '2019-03-29 02:24:03.729107');
/*!40000 ALTER TABLE `django_session`
  ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;

-- Dump completed on 2019-03-15 10:57:55

CREATE DATABASE  IF NOT EXISTS `blog` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `blog`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `posts` (
  `title` varchar(45) NOT NULL,
  `time_post` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post` varchar(13000) NOT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES ('bakir','2019-06-23 14:44:56',16,'jasklasjaklas,,sklka'),('bakir','2019-06-23 14:57:01',17,'sdfsfdfsdf'),('nemanja','2019-06-23 14:57:24',18,',as.d,as.d,.asd,a,sds'),('nemanja','2019-06-25 13:27:52',19,'askd;laskdkas'),('timur','2019-06-25 13:27:59',20,'asdkd;laskd;lka'),('timur','2019-06-25 13:28:06',21,'asdjasldklasjdkljas'),('amra','2019-06-25 13:28:14',22,'sdaldaskd;askd;l'),('amra','2019-06-25 13:28:27',23,'dasdjasjdklasdkljas'),('milica','2019-06-25 13:28:37',24,'dsldlasdlkasdk;las'),('milica','2019-06-25 13:28:46',25,'ksdjklasjdasdjklasjdkl'),('bakirsdasd','2019-06-25 13:38:53',26,'saddasdasdas'),('milica','2019-06-25 14:45:48',27,'dasjlkasdkljaskdjklas'),('amar','2019-06-25 14:46:06',28,'dkaskldas,,,sadasda'),('bakir','2019-06-26 13:11:32',29,'kjklkljkl;;;;tgjhgh'),('bakir','2019-06-30 23:30:30',30,'dsadasdas'),('bakir','2019-06-30 23:30:36',31,'sdasdasdas'),('bakir','2019-06-30 23:30:42',32,'sdasdasdasd');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-01  2:22:06

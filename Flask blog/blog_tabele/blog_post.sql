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
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES ('sddadas','2019-08-04 14:27:10',99,'bakir'),('sddadas','2019-08-04 14:27:12',100,'bakir'),('sddadas','2019-08-04 14:27:12',101,'bakir'),('sddadas','2019-08-04 14:27:12',102,'bakir'),('ivana prica o hrani','2019-08-06 20:56:15',103,'sdkjdjasjdljasdjasjdasjdkl'),('sdad','2019-08-06 20:57:00',104,'sadasdasdas'),('asdasd','2019-08-06 20:57:16',105,'asdsadasdas'),('sdadasas','2019-08-06 20:57:32',106,'asddasdas'),('bakir','2019-08-12 22:50:27',107,'s'),('bakir','2019-08-12 22:50:57',108,'dsadad'),('bakir','2019-08-12 22:51:12',109,'sadasdas'),('nemanja','2019-08-14 12:00:35',110,'dasdsads\r\n'),('bakir','2019-08-18 17:31:24',111,'kkkkk'),('timur','2019-08-18 17:34:46',112,'s'),('bakir','2019-08-18 17:36:32',113,'sss'),('amra','2019-08-18 17:39:38',114,'sdsdasd'),('nemanja','2019-08-18 17:46:23',115,'n'),('timur','2019-08-19 21:46:18',116,'sdasdasda\r\n'),('bakir','2019-08-19 21:51:32',117,'jjjjj'),('jlkjljljlkjkklkljkj','2019-08-21 22:40:23',118,'iyiuyuiyuiyuiyuiyuiuiyui'),('fetrsrftrtrd','2019-08-21 22:46:42',119,'ui423353466897');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'bakir','car'),(3,'amra','carica'),(5,'milica','carica'),(8,'nemanja','car'),(12,'s','bakir'),(13,'bbbb','123'),(14,'q','3333'),(41,'tiki','car'),(42,'r','r'),(43,'riki','r');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-27  1:36:43

-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: biblioteka1
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
-- Table structure for table `history_book`
--

DROP TABLE IF EXISTS `history_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `history_book` (
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `date_rent` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `return_date` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_book`
--

LOCK TABLES `history_book` WRITE;
/*!40000 ALTER TABLE `history_book` DISABLE KEYS */;
INSERT INTO `history_book` VALUES (39,20,'2019-04-12 22:06:08','2019-04-15 15:34:08'),(39,20,'2019-04-12 22:06:24','2019-04-15 15:34:08'),(40,21,'2019-04-12 22:06:43','2019-04-15 15:35:38'),(41,22,'2019-04-12 22:06:54','0000-00-00 00:00:00'),(42,23,'2019-04-15 14:18:09','0000-00-00 00:00:00'),(42,23,'2019-04-15 14:20:34','0000-00-00 00:00:00'),(44,23,'2019-04-15 14:26:41','0000-00-00 00:00:00'),(44,23,'2019-04-15 14:28:08','0000-00-00 00:00:00'),(41,22,'2019-04-15 14:54:18','0000-00-00 00:00:00'),(41,22,'2019-04-15 14:55:03','0000-00-00 00:00:00'),(41,22,'2019-04-15 14:55:08','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `history_book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-28 16:40:19
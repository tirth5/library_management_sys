-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: world
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `library`
--
USE world;

DROP TABLE IF EXISTS `librar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tirth` (
  `Member` varchar(40) NOT NULL,
  `PRN_NO` varchar(45) NOT NULL,
  `ID` varchar(45) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Address1` varchar(45) DEFAULT NULL,
  `Address2` varchar(45) DEFAULT NULL,
  `Postid` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `Bookid` varchar(45) DEFAULT NULL,
  `booktitle` varchar(45) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `databorrowed` varchar(45) DEFAULT NULL,
  `datedue` varchar(45) DEFAULT NULL,
  `daysonbook` varchar(45) DEFAULT NULL,
  `lateratefine` varchar(45) DEFAULT NULL,
  `dateoverdue` varchar(45) DEFAULT NULL,
  `finallprice` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PRN_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('Student','','','','','','','','','','','','','','','','',''),('Student','123','1','TIRTH','af','sdv','srb','25','5324209135','BKID361','Train to Pakistan','Khushwant singh','2023-07-01','2023-07-21','8','Rs.60','NO','Rs. 700'),('Student','125','3','ERGEW','','','','','','BKID728','The Great Indian Novel','Shashi Tharoor','2023-07-01','2023-07-21','14','Rs.70','NO','Rs. 600'),('Student','P1001','I15','Tirth','Chavda','asdf','nmg','2451','9913696057','BKID560','Excerpt knowledge','Salman Rushdie','2022-04-29','2022-05-19','15','Rs.70','NO','Rs. 400'),('Student','P1007','I23','Tanmay','Chaudhary','mjhn','lkfwg','2904','1340456934','BKID720','The Palace of Illusions','Draupadi','2022-04-29','2022-05-19','10','Rs.40','NO','Rs. 500');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-02 22:45:10

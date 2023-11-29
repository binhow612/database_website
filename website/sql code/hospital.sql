-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `contains`
--

DROP TABLE IF EXISTS `contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contains` (
  `Doc_code` char(9) NOT NULL,
  `Outpat_code` char(9) NOT NULL,
  `Treatment_no` int NOT NULL,
  `Med_code` varchar(10) NOT NULL,
  PRIMARY KEY (`Doc_code`,`Outpat_code`,`Treatment_no`,`Med_code`),
  KEY `fk_med_contain` (`Med_code`),
  CONSTRAINT `fk_doc_contain` FOREIGN KEY (`Doc_code`, `Outpat_code`, `Treatment_no`) REFERENCES `out_detail` (`Doc_code`, `Outpat_code`, `Treatment_no`) ON DELETE CASCADE,
  CONSTRAINT `fk_med_contain` FOREIGN KEY (`Med_code`) REFERENCES `medication` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contains`
--

LOCK TABLES `contains` WRITE;
/*!40000 ALTER TABLE `contains` DISABLE KEYS */;
/*!40000 ALTER TABLE `contains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `Code` int NOT NULL,
  `Title` varchar(15) NOT NULL,
  `Dean_code` char(9) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `Title` (`Title`),
  KEY `fk_dept_dean` (`Dean_code`),
  CONSTRAINT `fk_dept_dean` FOREIGN KEY (`Dean_code`) REFERENCES `doctor` (`Code`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `Fname` varchar(10) NOT NULL,
  `Lname` varchar(10) NOT NULL,
  `Code` char(9) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Start_date` date NOT NULL,
  `Specialty_name` varchar(30) NOT NULL,
  `Year_of_degree` int NOT NULL,
  `Dept_code` int DEFAULT NULL,
  PRIMARY KEY (`Code`),
  KEY `fk_doc_dept` (`Dept_code`),
  CONSTRAINT `fk_doc_dept` FOREIGN KEY (`Dept_code`) REFERENCES `department` (`Code`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_phone_number`
--

DROP TABLE IF EXISTS `doctor_phone_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_phone_number` (
  `Code` char(9) NOT NULL,
  `Phone_number` char(10) NOT NULL,
  PRIMARY KEY (`Code`,`Phone_number`),
  CONSTRAINT `fk_doc_phone` FOREIGN KEY (`Code`) REFERENCES `doctor` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_phone_number`
--

LOCK TABLES `doctor_phone_number` WRITE;
/*!40000 ALTER TABLE `doctor_phone_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor_phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `in_detail`
--

DROP TABLE IF EXISTS `in_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `in_detail` (
  `Doc_code` char(9) NOT NULL,
  `Inpat_code` char(9) NOT NULL,
  `Treatment_no` int NOT NULL,
  `Record_no` int NOT NULL,
  `Start_date` date DEFAULT NULL,
  `End_date` date DEFAULT NULL,
  `Result` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Doc_code`,`Inpat_code`,`Treatment_no`,`Record_no`),
  KEY `fk_inpat_in_detail` (`Inpat_code`),
  KEY `fk_record_in_detail` (`Record_no`),
  CONSTRAINT `fk_doc_in_detail` FOREIGN KEY (`Doc_code`) REFERENCES `doctor` (`Code`) ON DELETE CASCADE,
  CONSTRAINT `fk_inpat_in_detail` FOREIGN KEY (`Inpat_code`) REFERENCES `patient` (`Code`) ON DELETE CASCADE,
  CONSTRAINT `fk_record_in_detail` FOREIGN KEY (`Record_no`) REFERENCES `inpatient_record` (`Record_no`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `in_detail`
--

LOCK TABLES `in_detail` WRITE;
/*!40000 ALTER TABLE `in_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `in_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inpatient`
--

DROP TABLE IF EXISTS `inpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inpatient` (
  `Code` char(9) NOT NULL,
  PRIMARY KEY (`Code`),
  CONSTRAINT `inpat` FOREIGN KEY (`Code`) REFERENCES `patient` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inpatient`
--

LOCK TABLES `inpatient` WRITE;
/*!40000 ALTER TABLE `inpatient` DISABLE KEYS */;
/*!40000 ALTER TABLE `inpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inpatient_record`
--

DROP TABLE IF EXISTS `inpatient_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inpatient_record` (
  `Code` char(9) NOT NULL,
  `Record_no` int NOT NULL,
  `Admission_date` date DEFAULT NULL,
  `Discharge_date` date DEFAULT NULL,
  `Diagnosis` varchar(30) DEFAULT NULL,
  `Fee` varchar(15) DEFAULT NULL,
  `Room` int DEFAULT NULL,
  `Nurse_Code` char(9) DEFAULT NULL,
  PRIMARY KEY (`Code`,`Record_no`),
  KEY `fk_inpat_rec_nurse` (`Nurse_Code`),
  KEY `idx_reocrd_no` (`Record_no`),
  CONSTRAINT `fk_inpat_pat` FOREIGN KEY (`Code`) REFERENCES `patient` (`Code`) ON DELETE CASCADE,
  CONSTRAINT `fk_inpat_rec_nurse` FOREIGN KEY (`Nurse_Code`) REFERENCES `nurse` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inpatient_record`
--

LOCK TABLES `inpatient_record` WRITE;
/*!40000 ALTER TABLE `inpatient_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `inpatient_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_contained_in`
--

DROP TABLE IF EXISTS `is_contained_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_contained_in` (
  `Doc_code` char(9) NOT NULL,
  `Inpat_code` char(9) NOT NULL,
  `Treatment_no` int NOT NULL,
  `Med_code` varchar(10) NOT NULL,
  PRIMARY KEY (`Doc_code`,`Inpat_code`,`Treatment_no`,`Med_code`),
  KEY `fk_med_in_contain` (`Med_code`),
  CONSTRAINT `fk_in_contain` FOREIGN KEY (`Doc_code`, `Inpat_code`, `Treatment_no`) REFERENCES `in_detail` (`Doc_code`, `Inpat_code`, `Treatment_no`) ON DELETE CASCADE,
  CONSTRAINT `fk_med_in_contain` FOREIGN KEY (`Med_code`) REFERENCES `medication` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_contained_in`
--

LOCK TABLES `is_contained_in` WRITE;
/*!40000 ALTER TABLE `is_contained_in` DISABLE KEYS */;
/*!40000 ALTER TABLE `is_contained_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_provided_by`
--

DROP TABLE IF EXISTS `is_provided_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_provided_by` (
  `Med_code` varchar(10) NOT NULL,
  `Pro_code` int NOT NULL,
  `Provide_date` date DEFAULT NULL,
  `Price` varchar(15) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  PRIMARY KEY (`Med_code`,`Pro_code`),
  KEY `pro_provide` (`Pro_code`),
  CONSTRAINT `med_provided` FOREIGN KEY (`Med_code`) REFERENCES `medication` (`Code`) ON DELETE CASCADE,
  CONSTRAINT `pro_provide` FOREIGN KEY (`Pro_code`) REFERENCES `provider` (`Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_provided_by`
--

LOCK TABLES `is_provided_by` WRITE;
/*!40000 ALTER TABLE `is_provided_by` DISABLE KEYS */;
/*!40000 ALTER TABLE `is_provided_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `med_effect`
--

DROP TABLE IF EXISTS `med_effect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `med_effect` (
  `Med_code` varchar(10) NOT NULL,
  `Effect` varchar(30) NOT NULL,
  PRIMARY KEY (`Med_code`,`Effect`),
  CONSTRAINT `fk_med_eff` FOREIGN KEY (`Med_code`) REFERENCES `medication` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `med_effect`
--

LOCK TABLES `med_effect` WRITE;
/*!40000 ALTER TABLE `med_effect` DISABLE KEYS */;
/*!40000 ALTER TABLE `med_effect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medication`
--

DROP TABLE IF EXISTS `medication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication` (
  `Code` varchar(10) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Price` varchar(15) DEFAULT NULL,
  `State` char(1) DEFAULT NULL,
  `Expiration_date` date DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication`
--

LOCK TABLES `medication` WRITE;
/*!40000 ALTER TABLE `medication` DISABLE KEYS */;
/*!40000 ALTER TABLE `medication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurse`
--

DROP TABLE IF EXISTS `nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nurse` (
  `Fname` varchar(10) NOT NULL,
  `Lname` varchar(10) NOT NULL,
  `Code` char(9) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Start_date` date NOT NULL,
  `Specialty_name` varchar(30) DEFAULT NULL,
  `Year_of_degree` int DEFAULT NULL,
  `Dept_code` int DEFAULT NULL,
  PRIMARY KEY (`Code`),
  KEY `fk_nurse_dept` (`Dept_code`),
  CONSTRAINT `fk_nurse_dept` FOREIGN KEY (`Dept_code`) REFERENCES `department` (`Code`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurse`
--

LOCK TABLES `nurse` WRITE;
/*!40000 ALTER TABLE `nurse` DISABLE KEYS */;
/*!40000 ALTER TABLE `nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurse_phone_number`
--

DROP TABLE IF EXISTS `nurse_phone_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nurse_phone_number` (
  `Code` char(9) NOT NULL,
  `Phone_number` char(10) NOT NULL,
  PRIMARY KEY (`Code`,`Phone_number`),
  CONSTRAINT `fk_nurse_phone` FOREIGN KEY (`Code`) REFERENCES `nurse` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurse_phone_number`
--

LOCK TABLES `nurse_phone_number` WRITE;
/*!40000 ALTER TABLE `nurse_phone_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `nurse_phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `out_detail`
--

DROP TABLE IF EXISTS `out_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `out_detail` (
  `Doc_code` char(9) NOT NULL,
  `Outpat_code` char(9) NOT NULL,
  `Treatment_no` int NOT NULL,
  `Time` timestamp NULL DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Next_date` date DEFAULT NULL,
  `Fee` varchar(15) DEFAULT NULL,
  `Diagnosis` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Doc_code`,`Outpat_code`,`Treatment_no`),
  KEY `fk_outpat_out_detail` (`Outpat_code`),
  CONSTRAINT `fk_doc_out_detail` FOREIGN KEY (`Doc_code`) REFERENCES `doctor` (`Code`) ON DELETE CASCADE,
  CONSTRAINT `fk_outpat_out_detail` FOREIGN KEY (`Outpat_code`) REFERENCES `patient` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `out_detail`
--

LOCK TABLES `out_detail` WRITE;
/*!40000 ALTER TABLE `out_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `out_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outpatient`
--

DROP TABLE IF EXISTS `outpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outpatient` (
  `Code` char(9) NOT NULL,
  PRIMARY KEY (`Code`),
  CONSTRAINT `outpat` FOREIGN KEY (`Code`) REFERENCES `patient` (`Code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outpatient`
--

LOCK TABLES `outpatient` WRITE;
/*!40000 ALTER TABLE `outpatient` DISABLE KEYS */;
/*!40000 ALTER TABLE `outpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `Code` char(9) NOT NULL,
  `Patient_type` char(2) DEFAULT NULL,
  `Fname` varchar(10) NOT NULL,
  `Lname` varchar(10) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Phone_number` char(10) DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `Number` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Phone_number` char(10) DEFAULT NULL,
  PRIMARY KEY (`Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-26  0:30:09

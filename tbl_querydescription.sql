-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2023 at 05:17 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_chatbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_querydescription`
--

CREATE TABLE `tbl_querydescription` (
  `id` int(12) NOT NULL,
  `query` text NOT NULL,
  `type` varchar(250) DEFAULT NULL,
  `tag` varchar(250) DEFAULT NULL,
  `subject` varchar(250) DEFAULT NULL,
  `predicate` varchar(250) DEFAULT NULL,
  `object` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_querydescription`
--

INSERT INTO `tbl_querydescription` (`id`, `query`, `type`, `tag`, `subject`, `predicate`, `object`) VALUES
(1, 'reetings teacher, I want to ask .., what kind of password, is Nur Alma Batrisya? Can you please share again', 'gr,gr', 'VBZ,NNP,NNP,PRP,NNP,NNP,.', 'kind,password, Nur,Alma, Batrisya, share', 'please, please, please, please, please', 'again, again, again, again, again'),
(2, 'Selamat Malam', '[\'gr\']', NULL, NULL, NULL, NULL),
(3, 'Selamat Malam', '[\'gr\']', NULL, 'Subject:night', 'Predicate:', 'Object: Good'),
(4, 'Selamat Malam', '[\'gr\']', '[(\'Good\', \'JJ\'), (\'night\', \'NN\')]', 'Subject:night', 'Predicate:', 'Object: Good');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_querydescription`
--
ALTER TABLE `tbl_querydescription`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_querydescription`
--
ALTER TABLE `tbl_querydescription`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

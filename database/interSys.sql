-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 02, 2020 at 06:29 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `interSys`
--
CREATE DATABASE IF NOT EXISTS `interSys` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `interSys`;

-- --------------------------------------------------------

--
-- Table structure for table `actions`
--

CREATE TABLE `actions` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `attributes`
--

CREATE TABLE `attributes` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attributes`
--

INSERT INTO `attributes` (`id`, `version_id`, `value`) VALUES
(24, 10, 'breathe'),
(25, 10, 'animal'),
(26, 10, 'tail');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `version_id`, `value`) VALUES
(24, 10, 'animal'),
(25, 10, 'dog');

-- --------------------------------------------------------

--
-- Table structure for table `domains`
--

CREATE TABLE `domains` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `domains`
--

INSERT INTO `domains` (`id`, `version_id`, `value`) VALUES
(24, 10, 'animals'),
(25, 10, 'dogs'),
(27, 10, 'cats');

-- --------------------------------------------------------

--
-- Table structure for table `environment`
--

CREATE TABLE `environment` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `domain` text NOT NULL,
  `item` text NOT NULL,
  `value` text NOT NULL,
  `persist_time` int(11) NOT NULL,
  `categories` text NOT NULL,
  `types` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `environment`
--

INSERT INTO `environment` (`id`, `version_id`, `domain`, `item`, `value`, `persist_time`, `categories`, `types`, `attributes`) VALUES
(1, 10, 'animals', 'fact', 'animal can breathe', 20, 'animal', 'can', 'breathe'),
(2, 10, 'animals', 'question', 'can animal breathe?', 20, 'can', 'animal', 'breathe'),
(6, 10, 'dogs', 'question', 'can dog breathe?', 14, 'dog', 'can', 'breathe'),
(9, 10, 'dogs', 'fact', 'dog can breathe', 20, 'dog', 'can', 'breathe');

-- --------------------------------------------------------

--
-- Table structure for table `facts`
--

CREATE TABLE `facts` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL,
  `categories` text NOT NULL,
  `types` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `facts`
--

INSERT INTO `facts` (`id`, `version_id`, `value`, `categories`, `types`, `attributes`) VALUES
(28, 10, 'animal can breathe', 'animal', 'can', 'breathe'),
(32, 10, 'dog can breathe', 'dog', 'can', 'breathe'),
(33, 10, 'dog is a animal', 'dog', 'is a', 'animal');

-- --------------------------------------------------------

--
-- Table structure for table `perceptions`
--

CREATE TABLE `perceptions` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `short_descr` text NOT NULL,
  `long_descr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `name`, `short_descr`, `long_descr`) VALUES
(5, 'test', 'testetsetset', 'setestssssssssssssssssssssssss'),
(6, 'My project', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa'),
(8, 'test2', 'test', 'testing'),
(12, 'Animal', 'short', 'long');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL,
  `types` text NOT NULL,
  `categories` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `version_id`, `value`, `types`, `categories`, `attributes`) VALUES
(31, 10, 'can animal breathe?', 'can', 'animal', 'breathe'),
(34, 10, 'can dog breathe?', 'can', 'dog', 'breathe'),
(35, 10, 'is a dog animal?', 'is a', 'dog', 'animal');

-- --------------------------------------------------------

--
-- Table structure for table `sem_mem`
--

CREATE TABLE `sem_mem` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `domain` text NOT NULL,
  `fact` text NOT NULL,
  `retr_time` int(11) NOT NULL,
  `categories` text NOT NULL,
  `types` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sem_mem`
--

INSERT INTO `sem_mem` (`id`, `version_id`, `domain`, `fact`, `retr_time`, `categories`, `types`, `attributes`) VALUES
(34, 10, 'cats', 'cat can breathe', 1, 'cat', 'can', 'breathe'),
(35, 10, 'animals', 'animal can breathe', 1, 'animal', 'can', 'breathe'),
(36, 10, 'cats', 'cat is a animal', 1, 'cat', 'is a', 'animal');

-- --------------------------------------------------------

--
-- Table structure for table `short_term_mem`
--

CREATE TABLE `short_term_mem` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `domain` text NOT NULL,
  `item` text NOT NULL,
  `value` text NOT NULL,
  `decay` int(11) NOT NULL,
  `categories` text NOT NULL,
  `types` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `short_term_mem`
--

INSERT INTO `short_term_mem` (`id`, `version_id`, `domain`, `item`, `value`, `decay`, `categories`, `types`, `attributes`) VALUES
(28, 10, 'cats', 'fact', 'cat is a animal', 15, 'cat', 'is a', 'animal'),
(29, 10, 'dogs', 'question', 'can dog breathe?', 20, 'dog', 'can', 'breathe'),
(30, 10, 'dogs', 'fact', 'dog can breathe', 20, 'dog', 'can', 'breathe');

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `version_id`, `value`) VALUES
(24, 10, 'can'),
(25, 10, 'is a'),
(26, 10, 'has');

-- --------------------------------------------------------

--
-- Table structure for table `versions`
--

CREATE TABLE `versions` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `project_name` varchar(200) NOT NULL,
  `numb` double NOT NULL,
  `short_descr` text NOT NULL,
  `long_descr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `versions`
--

INSERT INTO `versions` (`id`, `name`, `project_name`, `numb`, `short_descr`, `long_descr`) VALUES
(10, 'old', 'My project', 1, 'bbb', 'ddddddd'),
(14, 'old', 'test', 1.2, 'bbb', 'ddddddd'),
(21, 'old New', 'test', 3, 'bbb', 'ddddddd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actions`
--
ALTER TABLE `actions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attributes`
--
ALTER TABLE `attributes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `domains`
--
ALTER TABLE `domains`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `environment`
--
ALTER TABLE `environment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `facts`
--
ALTER TABLE `facts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `perceptions`
--
ALTER TABLE `perceptions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sem_mem`
--
ALTER TABLE `sem_mem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `short_term_mem`
--
ALTER TABLE `short_term_mem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `versions`
--
ALTER TABLE `versions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actions`
--
ALTER TABLE `actions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `attributes`
--
ALTER TABLE `attributes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `environment`
--
ALTER TABLE `environment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `facts`
--
ALTER TABLE `facts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `perceptions`
--
ALTER TABLE `perceptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `sem_mem`
--
ALTER TABLE `sem_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `short_term_mem`
--
ALTER TABLE `short_term_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `versions`
--
ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

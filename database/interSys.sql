-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 02, 2021 at 08:57 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

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
(121, 14, 'breath'),
(122, 14, 'animal'),
(124, 14, 'dog'),
(125, 14, 'basenji'),
(126, 14, 'hound'),
(127, 14, 'track'),
(128, 14, 'bark'),
(129, 14, 'lay'),
(130, 14, 'move'),
(131, 24, 'breath'),
(132, 24, 'animal'),
(134, 24, 'dog'),
(135, 24, 'basenji'),
(136, 24, 'hound'),
(137, 24, 'track'),
(138, 24, 'bark'),
(139, 24, 'lay'),
(140, 24, 'move'),
(141, 10, 'breath'),
(142, 10, 'animal'),
(144, 10, 'dog'),
(145, 10, 'basenji'),
(146, 10, 'hound'),
(147, 10, 'track'),
(148, 10, 'bark'),
(149, 10, 'lay'),
(150, 10, 'move'),
(151, 26, 'breath'),
(152, 26, 'animal'),
(154, 26, 'dog'),
(155, 26, 'basenji'),
(156, 26, 'hound'),
(157, 26, 'track'),
(158, 26, 'bark'),
(159, 26, 'lay'),
(160, 26, 'move');

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
(75, 14, 'animal'),
(76, 14, 'dog'),
(77, 14, 'hound'),
(78, 14, 'basenji'),
(79, 14, 'bobby'),
(80, 24, 'animal'),
(81, 24, 'dog'),
(82, 24, 'hound'),
(83, 24, 'basenji'),
(84, 24, 'bobby'),
(85, 24, 'cat'),
(86, 10, 'animal'),
(87, 10, 'dog'),
(88, 10, 'hound'),
(89, 10, 'basenji'),
(90, 10, 'bobby'),
(91, 26, 'animal'),
(92, 26, 'dog'),
(93, 26, 'hound'),
(94, 26, 'basenji'),
(95, 26, 'bobby');

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
(54, 14, 'animals'),
(55, 14, 'dogs'),
(57, 24, 'animals'),
(58, 24, 'dogs'),
(60, 10, 'animals'),
(61, 10, 'dogs'),
(63, 26, 'animals'),
(64, 26, 'dogs');

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
(2, 10, 'dogs', 'question', 'can dog track?', 20, 'dog', 'can', 'track'),
(6, 10, 'dogs', 'question', 'can basenji breath?', 3, 'basenji', 'can', 'breath'),
(9, 10, 'dogs', 'fact', 'dog can lay', 20, 'dog', 'can', 'lay');

-- --------------------------------------------------------

--
-- Table structure for table `experiment`
--

DROP TABLE IF EXISTS `experiment`;
CREATE TABLE `experiment` (
  `id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `domain` text NOT NULL,
  `item` text NOT NULL,
  `value` text NOT NULL,
  `future_time` int(11) NOT NULL,
  `persist_time` int(11) NOT NULL,
  `categories` text NOT NULL,
  `types` text NOT NULL,
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `experiment`
--

INSERT INTO `experiment` (`id`, `version_id`, `domain`, `item`, `value`, `future_time`, `persist_time`, `categories`, `types`, `attributes`) VALUES
(1, 10, 'animals', 'fact', 'animal can breathe', 10, 15, 'animal', 'can', 'breathe'),
(7, 10, 'cats', 'fact', 'cat can breathe', 2, 14, 'cat', 'can', 'breathe'),
(9, 10, 'cats', 'question', 'is a cat animal?', 30, 15, 'cat', 'is a', 'animal');

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
(37, 14, 'animal can breath', 'animal', 'can', 'breath'),
(38, 14, 'dog can breath', 'dog', 'can', 'breath'),
(39, 14, 'dog is a animal', 'dog', 'is a', 'animal'),
(40, 24, 'animal can breath', 'animal', 'can', 'breath'),
(41, 24, 'dog can breath', 'dog', 'can', 'breath'),
(42, 24, 'dog is a animal', 'dog', 'is a', 'animal'),
(43, 10, 'animal can breath', 'animal', 'can', 'breath'),
(44, 10, 'dog can breath', 'dog', 'can', 'breath'),
(45, 10, 'dog is a animal', 'dog', 'is a', 'animal'),
(46, 26, 'animal can breath', 'animal', 'can', 'breath'),
(47, 26, 'dog can breath', 'dog', 'can', 'breath'),
(48, 26, 'dog is a animal', 'dog', 'is a', 'animal');

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
(6, 'Animal-Dog', 'This project shows the animals-dogs relation. The main categories \"animals\" and \"dogs\" are presented.', 'aaaaaaaaaaaaaaaaaaaa'),
(8, 'test2', 'test', 'testing'),
(12, 'Animal', 'short', 'long'),
(22, 'Cats', 'Added cats', 'Information about cats is added to the semantic memory');

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
(41, 14, 'can animal breath?', 'can', 'animal', 'breath'),
(42, 14, 'can dog breath?', 'can', 'dog', 'breath'),
(43, 14, 'is a dog animal?', 'is a', 'dog', 'animal'),
(44, 14, 'can dog track?', 'can', 'dog', 'track'),
(45, 24, 'can animal breath?', 'can', 'animal', 'breath'),
(46, 24, 'can dog breath?', 'can', 'dog', 'breath'),
(47, 24, 'is a dog animal?', 'is a', 'dog', 'animal'),
(48, 24, 'can dog track?', 'can', 'dog', 'track'),
(49, 10, 'can animal breath?', 'can', 'animal', 'breath'),
(50, 10, 'can dog breath?', 'can', 'dog', 'breath'),
(51, 10, 'is a dog animal?', 'is a', 'dog', 'animal'),
(52, 10, 'can dog track?', 'can', 'dog', 'track'),
(53, 26, 'can animal breath?', 'can', 'animal', 'breath'),
(54, 26, 'can dog breath?', 'can', 'dog', 'breath'),
(55, 26, 'is a dog animal?', 'is a', 'dog', 'animal'),
(56, 26, 'can dog track?', 'can', 'dog', 'track'),
(63, 10, 'can hound move?', 'can', 'hound', 'move');

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
(35, 10, 'animals', 'animal can breath', 1, 'animal', 'can', 'breath'),
(37, 10, 'animals', 'animal can move', 1, 'animal', 'can', 'move'),
(38, 10, 'dogs', 'dog is a animal', 2, 'dog', 'is a', 'animal'),
(39, 10, 'dogs', 'dog can bark', 1, 'dog', 'can', 'bark'),
(41, 10, 'dogs', 'hound can track', 1, 'hound', 'can', 'track'),
(42, 10, 'dogs', 'basenji is a hound', 2, 'basenji', 'is a', 'hound'),
(44, 10, 'dogs', 'bobby is a basenji', 2, 'bobby', 'is a', 'basenji'),
(46, 24, 'animals', 'animal can breath', 1, 'animal', 'can', 'breath'),
(48, 10, 'dogs', 'basenji cannot bark', 3, 'basenji', 'cannot', 'bark'),
(49, 10, 'dogs', 'hound is a dog', 2, 'hound', 'is a', 'dog'),
(54, 10, 'dogs', 'bobby can lay', 1, 'bobby', 'can', 'lay');

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
(29, 10, 'dogs', 'question', 'can animal breath?', 100, 'animal', 'can', 'breath'),
(30, 10, 'dogs', 'fact', 'animal can breath', 100, 'animal', 'can', 'breath'),
(32, 24, 'animals', 'fact', 'animal can breath', 100, 'animal', 'can', 'breath');

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
(61, 14, 'can'),
(62, 14, 'is a'),
(63, 14, 'has'),
(64, 14, 'cannot'),
(65, 24, 'can'),
(66, 24, 'is a'),
(67, 24, 'has'),
(68, 24, 'cannot'),
(69, 10, 'can'),
(70, 10, 'is a'),
(71, 10, 'has'),
(72, 10, 'cannot'),
(73, 26, 'can'),
(74, 26, 'is a'),
(75, 26, 'has'),
(76, 26, 'cannot');

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
(10, 'Old', 'Animal-Dog', 1, 'This is the test version', 'ddddddd'),
(14, 'Old', 'test', 1.2, 'This is the test version', 'ddddddd'),
(21, 'old New', 'test', 3, 'bbb', 'ddddddd'),
(26, 'New', 'Animal-Dog', 2, 'More information added', ''),
(35, 'First', 'Cats', 1, 'Very first version', '');

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
-- Indexes for table `experiment`
--
ALTER TABLE `experiment`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=167;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=96;

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `environment`
--
ALTER TABLE `environment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `experiment`
--
ALTER TABLE `experiment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `facts`
--
ALTER TABLE `facts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `perceptions`
--
ALTER TABLE `perceptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `sem_mem`
--
ALTER TABLE `sem_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `short_term_mem`
--
ALTER TABLE `short_term_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `versions`
--
ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

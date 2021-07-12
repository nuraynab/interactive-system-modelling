-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 29, 2021 at 09:28 PM
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
(160, 26, 'move'),
(167, 36, 'skin'),
(168, 36, 'move'),
(169, 36, 'eat'),
(170, 36, 'breathe'),
(171, 36, 'wings'),
(173, 36, 'feathers'),
(174, 36, 'fins'),
(175, 36, 'swim'),
(176, 36, 'gills'),
(177, 36, 'sing'),
(178, 36, 'yellow'),
(180, 36, 'tall'),
(182, 36, 'bite'),
(183, 36, 'dangerous'),
(184, 36, 'pink'),
(185, 36, 'edible'),
(186, 36, 'fly'),
(187, 36, 'canary'),
(188, 36, 'ostrich'),
(189, 36, 'shark'),
(190, 36, 'salmon'),
(191, 36, 'bird'),
(192, 36, 'fish'),
(193, 36, 'animal'),
(194, 37, 'skin'),
(195, 37, 'move'),
(196, 37, 'eat'),
(197, 37, 'breathe'),
(198, 37, 'wings'),
(199, 37, 'feathers'),
(200, 37, 'fins'),
(201, 37, 'swim'),
(202, 37, 'gills'),
(203, 37, 'sing'),
(204, 37, 'yellow'),
(205, 37, 'tall'),
(206, 37, 'bite'),
(207, 37, 'dangerous'),
(208, 37, 'pink'),
(209, 37, 'edible'),
(210, 37, 'fly'),
(211, 37, 'canary'),
(212, 37, 'ostrich'),
(213, 37, 'shark'),
(214, 37, 'salmon'),
(215, 37, 'bird'),
(216, 37, 'fish'),
(217, 37, 'animal'),
(218, 38, 'skin'),
(219, 38, 'move'),
(220, 38, 'eat'),
(221, 38, 'breathe'),
(222, 38, 'wings'),
(223, 38, 'feathers'),
(224, 38, 'fins'),
(225, 38, 'swim'),
(226, 38, 'gills'),
(227, 38, 'sing'),
(228, 38, 'yellow'),
(229, 38, 'tall'),
(230, 38, 'bite'),
(231, 38, 'dangerous'),
(232, 38, 'pink'),
(233, 38, 'edible'),
(234, 38, 'fly'),
(235, 38, 'canary'),
(236, 38, 'ostrich'),
(237, 38, 'shark'),
(238, 38, 'salmon'),
(239, 38, 'bird'),
(240, 38, 'fish'),
(241, 38, 'animal');

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
(95, 26, 'bobby'),
(96, 36, 'animal'),
(97, 36, 'bird'),
(98, 36, 'fish'),
(99, 36, 'canary'),
(100, 36, 'ostrich'),
(101, 36, 'shark'),
(102, 36, 'salmon'),
(103, 37, 'animal'),
(104, 37, 'bird'),
(105, 37, 'fish'),
(106, 37, 'canary'),
(107, 37, 'ostrich'),
(108, 37, 'shark'),
(109, 37, 'salmon'),
(110, 38, 'animal'),
(111, 38, 'bird'),
(112, 38, 'fish'),
(113, 38, 'canary'),
(114, 38, 'ostrich'),
(115, 38, 'shark'),
(116, 38, 'salmon');

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
(64, 26, 'dogs'),
(66, 36, 'Animals'),
(67, 36, 'Birds'),
(68, 36, 'Fish'),
(69, 37, 'Animals'),
(70, 37, 'Birds'),
(71, 37, 'Fish'),
(72, 38, 'Animals'),
(73, 38, 'Birds'),
(74, 38, 'Fish');

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

-- --------------------------------------------------------

--
-- Table structure for table `experiment`
--

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
  `attributes` text NOT NULL,
  `repeat_num` int(11) DEFAULT NULL,
  `in_time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `experiment`
--

INSERT INTO `experiment` (`id`, `version_id`, `domain`, `item`, `value`, `future_time`, `persist_time`, `categories`, `types`, `attributes`, `repeat_num`, `in_time`) VALUES
(27, 10, 'animals', 'question', 'can hound move?', 3, 3, 'hound', 'can', 'move', 5, 4),
(33, 36, 'Birds', 'question', 'is a canary fish?', 0, 2, 'canary', 'is a', 'fish', 0, 0),
(34, 36, 'Birds', 'question', 'is a ostrich ostrich?', 4, 2, 'ostrich', 'is a', 'ostrich', 0, 0),
(35, 36, 'Fish', 'question', 'is a shark shark?', 8, 2, 'shark', 'is a', 'shark', 0, 0),
(36, 36, 'Fish', 'question', 'is a salmon salmon?', 12, 2, 'salmon', 'is a', 'salmon', 0, 0),
(37, 36, 'Birds', 'question', 'is a bird bird?', 16, 2, 'bird', 'is a', 'bird', 0, 0),
(38, 36, 'Fish', 'question', 'is a fish fish?', 20, 2, 'fish', 'is a', 'fish', 0, 0),
(39, 36, 'Animals', 'question', 'is a animal animal?', 24, 2, 'animal', 'is a', 'animal', 0, 0),
(40, 36, 'Birds', 'question', 'is a canary bird?', 28, 2, 'canary', 'is a', 'bird', 0, 0),
(41, 36, 'Birds', 'question', 'is a ostrich bird?', 32, 2, 'ostrich', 'is a', 'bird', 0, 0),
(42, 36, 'Fish', 'question', 'is a shark fish?', 36, 2, 'shark', 'is a', 'fish', 0, 0),
(43, 36, 'Fish', 'question', 'is a salmon fish?', 40, 2, 'salmon', 'is a', 'fish', 0, 0),
(44, 36, 'Birds', 'question', 'is a bird animal?', 44, 2, 'bird', 'is a', 'animal', 0, 0),
(45, 36, 'Fish', 'question', 'is a fish animal?', 48, 2, 'fish', 'is a', 'animal', 0, 0),
(46, 36, 'Birds', 'question', 'is a canary animal?', 52, 2, 'canary', 'is a', 'animal', 0, 0),
(47, 36, 'Birds', 'question', 'is a ostrich animal?', 56, 2, 'ostrich', 'is a', 'animal', 0, 0),
(48, 36, 'Fish', 'question', 'is a shark animal?', 60, 2, 'shark', 'is a', 'animal', 0, 0),
(49, 36, 'Fish', 'question', 'is a salmon animal?', 64, 2, 'salmon', 'is a', 'animal', 0, 0),
(50, 36, 'Birds', 'question', 'can canary sing?', 68, 2, 'canary', 'can', 'sing', 0, 0),
(51, 36, 'Birds', 'question', 'is ostrich tall?', 72, 2, 'ostrich', 'is', 'tall', 0, 0),
(52, 36, 'Fish', 'question', 'is shark dangerous?', 76, 2, 'shark', 'is', 'dangerous', 0, 0),
(53, 36, 'Fish', 'question', 'is salmon edible?', 80, 2, 'salmon', 'is', 'edible', 0, 0),
(54, 36, 'Birds', 'question', 'can bird fly?', 84, 2, 'bird', 'can', 'fly', 0, 0),
(55, 36, 'Fish', 'question', 'can fish swim?', 88, 2, 'fish', 'can', 'swim', 0, 0),
(56, 36, 'Animals', 'question', 'can animal move?', 92, 2, 'animal', 'can', 'move', 0, 0),
(57, 36, 'Birds', 'question', 'can canary fly?', 96, 2, 'canary', 'can', 'fly', 0, 0),
(58, 36, 'Birds', 'question', 'has canary wings?', 100, 2, 'canary', 'has', 'wings', 0, 0),
(59, 36, 'Birds', 'question', 'has canary feathers?', 104, 2, 'canary', 'has', 'feathers', 0, 0),
(60, 36, 'Fish', 'question', 'has shark fins?', 108, 2, 'shark', 'has', 'fins', 0, 0),
(61, 36, 'Fish', 'question', 'can shark swim?', 112, 2, 'shark', 'can', 'swim', 0, 0),
(62, 36, 'Fish', 'question', 'has shark gills?', 116, 2, 'shark', 'has', 'gills', 0, 0),
(63, 36, 'Birds', 'question', 'has canary skin?', 120, 2, 'canary', 'has', 'skin', 0, 0),
(64, 36, 'Birds', 'question', 'can ostrich move?', 124, 2, 'ostrich', 'can', 'move', 0, 0),
(65, 36, 'Fish', 'question', 'can shark eat?', 128, 2, 'shark', 'can', 'eat', 0, 0),
(66, 36, 'Fish', 'question', 'can shark breathe?', 132, 2, 'shark', 'can', 'breathe', 0, 0),
(77, 10, 'animals', 'fact', 'animal can breath', 1, 2, 'animal', 'can', 'breath', 20, 3),
(79, 10, 'animals', 'question', 'can animal breath?', 5, 5, 'animal', 'can', 'breath', NULL, NULL),
(81, 10, 'dogs', 'question', 'is a dog animal?', 1, 10, 'dog', 'is a', 'animal', NULL, NULL),
(82, 10, 'animals', 'fact', 'dog is a animal', 4, 2, 'dog', 'is a', 'animal', 20, 2),
(83, 37, 'Birds', 'fact', 'bird is a animal', 2, 2, 'bird', 'is a', 'animal', 20, 2),
(84, 37, 'Birds', 'fact', 'bird has wings', 4, 2, 'bird', 'has', 'wings', 20, 2),
(85, 37, 'Birds', 'fact', 'bird can fly', 6, 2, 'bird', 'can', 'fly', 20, 2),
(86, 37, 'Birds', 'fact', 'bird has feathers', 8, 2, 'bird', 'has', 'feathers', 20, 2),
(87, 37, 'Fish', 'fact', 'fish is a animal', 10, 2, 'fish', 'is a', 'animal', 20, 2),
(88, 37, 'Fish', 'fact', 'fish has fins', 12, 2, 'fish', 'has', 'fins', 20, 2),
(89, 37, 'Fish', 'fact', 'fish can swim', 14, 2, 'fish', 'can', 'swim', 20, 2),
(90, 37, 'Fish', 'fact', 'fish has gills', 16, 2, 'fish', 'has', 'gills', 20, 2),
(91, 37, 'Birds', 'fact', 'canary can sing', 18, 2, 'canary', 'can', 'sing', 20, 2),
(92, 37, 'Birds', 'fact', 'canary is yellow', 20, 2, 'canary', 'is', 'yellow', 20, 2),
(93, 37, 'Birds', 'fact', 'ostrich is tall', 22, 2, 'ostrich', 'is', 'tall', 20, 2),
(94, 37, 'Birds', 'fact', 'ostrich cannot fly', 24, 2, 'ostrich', 'cannot', 'fly', 20, 2),
(95, 37, 'Fish', 'fact', 'shark can bite', 26, 2, 'shark', 'can', 'bite', 20, 2),
(96, 37, 'Fish', 'fact', 'shark is dangerous', 28, 2, 'shark', 'is', 'dangerous', 20, 2),
(97, 37, 'Fish', 'fact', 'salmon is pink', 30, 2, 'salmon', 'is', 'pink', 20, 2),
(98, 37, 'Fish', 'fact', 'salmon is edible', 32, 2, 'salmon', 'is', 'edible', 20, 2),
(99, 37, 'Birds', 'fact', 'canary is a bird', 34, 2, 'canary', 'is a', 'bird', 20, 2),
(100, 37, 'Birds', 'fact', 'ostrich is a bird', 36, 2, 'ostrich', 'is a', 'bird', 20, 2),
(101, 37, 'Fish', 'fact', 'shark is a fish', 38, 2, 'shark', 'is a', 'fish', 20, 2),
(102, 37, 'Fish', 'fact', 'salmon is a fish', 40, 2, 'salmon', 'is a', 'fish', 20, 2),
(103, 38, 'Birds', 'fact', 'bird is a animal', 10, 10, 'bird', 'is a', 'animal', 20, 2),
(104, 38, 'Birds', 'fact', 'bird has wings', 20, 10, 'bird', 'has', 'wings', 20, 2),
(105, 38, 'Birds', 'fact', 'bird can fly', 30, 10, 'bird', 'can', 'fly', 20, 2),
(106, 38, 'Birds', 'fact', 'bird has feathers', 40, 10, 'bird', 'has', 'feathers', 20, 2),
(107, 38, 'Fish', 'fact', 'fish is a animal', 50, 10, 'fish', 'is a', 'animal', 20, 2),
(108, 38, 'Fish', 'fact', 'fish has fins', 60, 10, 'fish', 'has', 'fins', 20, 2),
(109, 38, 'Fish', 'fact', 'fish can swim', 70, 10, 'fish', 'can', 'swim', 20, 2),
(110, 38, 'Fish', 'fact', 'fish has gills', 80, 10, 'fish', 'has', 'gills', 20, 2),
(111, 38, 'Birds', 'fact', 'canary can sing', 90, 10, 'canary', 'can', 'sing', 20, 2),
(112, 38, 'Birds', 'fact', 'canary is yellow', 100, 10, 'canary', 'is', 'yellow', 20, 2),
(113, 38, 'Birds', 'fact', 'ostrich is tall', 110, 10, 'ostrich', 'is', 'tall', 20, 2),
(114, 38, 'Birds', 'fact', 'ostrich cannot fly', 120, 10, 'ostrich', 'cannot', 'fly', 20, 2),
(115, 38, 'Fish', 'fact', 'shark can bite', 130, 10, 'shark', 'can', 'bite', 20, 2),
(116, 38, 'Fish', 'fact', 'shark is dangerous', 140, 10, 'shark', 'is', 'dangerous', 20, 2),
(117, 38, 'Fish', 'fact', 'salmon is pink', 150, 10, 'salmon', 'is', 'pink', 20, 2),
(118, 38, 'Fish', 'fact', 'salmon is edible', 160, 10, 'salmon', 'is', 'edible', 20, 2),
(119, 38, 'Birds', 'fact', 'canary is a bird', 170, 10, 'canary', 'is a', 'bird', 20, 2),
(120, 38, 'Birds', 'fact', 'ostrich is a bird', 180, 10, 'ostrich', 'is a', 'bird', 20, 2),
(121, 38, 'Fish', 'fact', 'shark is a fish', 190, 10, 'shark', 'is a', 'fish', 20, 2),
(122, 38, 'Fish', 'fact', 'salmon is a fish', 200, 10, 'salmon', 'is a', 'fish', 20, 2),
(123, 37, 'Birds', 'question', 'is a canary fish?', 0, 2, 'canary', 'is a', 'fish', 0, 0),
(124, 37, 'Birds', 'question', 'is a ostrich ostrich?', 4, 2, 'ostrich', 'is a', 'ostrich', 0, 0),
(125, 37, 'Fish', 'question', 'is a shark shark?', 8, 2, 'shark', 'is a', 'shark', 0, 0),
(126, 37, 'Fish', 'question', 'is a salmon salmon?', 12, 2, 'salmon', 'is a', 'salmon', 0, 0),
(127, 37, 'Birds', 'question', 'is a bird bird?', 16, 2, 'bird', 'is a', 'bird', 0, 0),
(128, 37, 'Fish', 'question', 'is a fish fish?', 20, 2, 'fish', 'is a', 'fish', 0, 0),
(129, 37, 'Animals', 'question', 'is a animal animal?', 24, 2, 'animal', 'is a', 'animal', 0, 0),
(130, 37, 'Birds', 'question', 'is a canary bird?', 28, 2, 'canary', 'is a', 'bird', 0, 0),
(131, 37, 'Birds', 'question', 'is a ostrich bird?', 32, 2, 'ostrich', 'is a', 'bird', 0, 0),
(132, 37, 'Fish', 'question', 'is a shark fish?', 36, 2, 'shark', 'is a', 'fish', 0, 0),
(133, 37, 'Fish', 'question', 'is a salmon fish?', 40, 2, 'salmon', 'is a', 'fish', 0, 0),
(134, 37, 'Birds', 'question', 'is a bird animal?', 44, 2, 'bird', 'is a', 'animal', 0, 0),
(135, 37, 'Fish', 'question', 'is a fish animal?', 48, 2, 'fish', 'is a', 'animal', 0, 0),
(136, 37, 'Birds', 'question', 'is a canary animal?', 52, 2, 'canary', 'is a', 'animal', 0, 0),
(137, 37, 'Birds', 'question', 'is a ostrich animal?', 56, 2, 'ostrich', 'is a', 'animal', 0, 0),
(138, 37, 'Fish', 'question', 'is a shark animal?', 60, 2, 'shark', 'is a', 'animal', 0, 0),
(139, 37, 'Fish', 'question', 'is a salmon animal?', 64, 2, 'salmon', 'is a', 'animal', 0, 0),
(140, 37, 'Birds', 'question', 'can canary sing?', 68, 2, 'canary', 'can', 'sing', 0, 0),
(141, 37, 'Birds', 'question', 'is ostrich tall?', 72, 2, 'ostrich', 'is', 'tall', 0, 0),
(142, 37, 'Fish', 'question', 'is shark dangerous?', 76, 2, 'shark', 'is', 'dangerous', 0, 0),
(143, 37, 'Fish', 'question', 'is salmon edible?', 80, 2, 'salmon', 'is', 'edible', 0, 0),
(144, 37, 'Birds', 'question', 'can bird fly?', 84, 2, 'bird', 'can', 'fly', 0, 0),
(145, 37, 'Fish', 'question', 'can fish swim?', 88, 2, 'fish', 'can', 'swim', 0, 0),
(146, 37, 'Animals', 'question', 'can animal move?', 92, 2, 'animal', 'can', 'move', 0, 0),
(147, 37, 'Birds', 'question', 'can canary fly?', 96, 2, 'canary', 'can', 'fly', 0, 0),
(148, 37, 'Birds', 'question', 'has canary wings?', 100, 2, 'canary', 'has', 'wings', 0, 0),
(149, 37, 'Birds', 'question', 'has canary feathers?', 104, 2, 'canary', 'has', 'feathers', 0, 0),
(150, 37, 'Fish', 'question', 'has shark fins?', 108, 2, 'shark', 'has', 'fins', 0, 0),
(151, 37, 'Fish', 'question', 'can shark swim?', 112, 2, 'shark', 'can', 'swim', 0, 0),
(152, 37, 'Fish', 'question', 'has shark gills?', 116, 2, 'shark', 'has', 'gills', 0, 0),
(153, 37, 'Birds', 'question', 'has canary skin?', 120, 2, 'canary', 'has', 'skin', 0, 0),
(154, 37, 'Birds', 'question', 'can ostrich move?', 124, 2, 'ostrich', 'can', 'move', 0, 0),
(155, 37, 'Fish', 'question', 'can shark eat?', 128, 2, 'shark', 'can', 'eat', 0, 0),
(156, 37, 'Fish', 'question', 'can shark breathe?', 132, 2, 'shark', 'can', 'breathe', 0, 0),
(190, 38, 'Birds', 'question', 'is a canary fish?', 0, 2, 'canary', 'is a', 'fish', 0, 0),
(157, 38, 'Birds', 'question', 'is a ostrich ostrich?', 4, 2, 'ostrich', 'is a', 'ostrich', 0, 0),
(158, 38, 'Fish', 'question', 'is a shark shark?', 8, 2, 'shark', 'is a', 'shark', 0, 0),
(159, 38, 'Fish', 'question', 'is a salmon salmon?', 12, 2, 'salmon', 'is a', 'salmon', 0, 0),
(160, 38, 'Birds', 'question', 'is a bird bird?', 16, 2, 'bird', 'is a', 'bird', 0, 0),
(161, 38, 'Fish', 'question', 'is a fish fish?', 20, 2, 'fish', 'is a', 'fish', 0, 0),
(162, 38, 'Animals', 'question', 'is a animal animal?', 24, 2, 'animal', 'is a', 'animal', 0, 0),
(163, 38, 'Birds', 'question', 'is a canary bird?', 28, 2, 'canary', 'is a', 'bird', 0, 0),
(164, 38, 'Birds', 'question', 'is a ostrich bird?', 32, 2, 'ostrich', 'is a', 'bird', 0, 0),
(165, 38, 'Fish', 'question', 'is a shark fish?', 36, 2, 'shark', 'is a', 'fish', 0, 0),
(166, 38, 'Fish', 'question', 'is a salmon fish?', 40, 2, 'salmon', 'is a', 'fish', 0, 0),
(167, 38, 'Birds', 'question', 'is a bird animal?', 44, 2, 'bird', 'is a', 'animal', 0, 0),
(168, 38, 'Fish', 'question', 'is a fish animal?', 48, 2, 'fish', 'is a', 'animal', 0, 0),
(169, 38, 'Birds', 'question', 'is a canary animal?', 52, 2, 'canary', 'is a', 'animal', 0, 0),
(170, 38, 'Birds', 'question', 'is a ostrich animal?', 56, 2, 'ostrich', 'is a', 'animal', 0, 0),
(171, 38, 'Fish', 'question', 'is a shark animal?', 60, 2, 'shark', 'is a', 'animal', 0, 0),
(172, 38, 'Fish', 'question', 'is a salmon animal?', 64, 2, 'salmon', 'is a', 'animal', 0, 0),
(173, 38, 'Birds', 'question', 'can canary sing?', 68, 2, 'canary', 'can', 'sing', 0, 0),
(174, 38, 'Birds', 'question', 'is ostrich tall?', 72, 2, 'ostrich', 'is', 'tall', 0, 0),
(175, 38, 'Fish', 'question', 'is shark dangerous?', 76, 2, 'shark', 'is', 'dangerous', 0, 0),
(176, 38, 'Fish', 'question', 'is salmon edible?', 80, 2, 'salmon', 'is', 'edible', 0, 0),
(177, 38, 'Birds', 'question', 'can bird fly?', 84, 2, 'bird', 'can', 'fly', 0, 0),
(178, 38, 'Fish', 'question', 'can fish swim?', 88, 2, 'fish', 'can', 'swim', 0, 0),
(179, 38, 'Animals', 'question', 'can animal move?', 92, 2, 'animal', 'can', 'move', 0, 0),
(180, 38, 'Birds', 'question', 'can canary fly?', 96, 2, 'canary', 'can', 'fly', 0, 0),
(181, 38, 'Birds', 'question', 'has canary wings?', 100, 2, 'canary', 'has', 'wings', 0, 0),
(182, 38, 'Birds', 'question', 'has canary feathers?', 104, 2, 'canary', 'has', 'feathers', 0, 0),
(183, 38, 'Fish', 'question', 'has shark fins?', 108, 2, 'shark', 'has', 'fins', 0, 0),
(184, 38, 'Fish', 'question', 'can shark swim?', 112, 2, 'shark', 'can', 'swim', 0, 0),
(185, 38, 'Fish', 'question', 'has shark gills?', 116, 2, 'shark', 'has', 'gills', 0, 0),
(186, 38, 'Birds', 'question', 'has canary skin?', 120, 2, 'canary', 'has', 'skin', 0, 0),
(187, 38, 'Birds', 'question', 'can ostrich move?', 124, 2, 'ostrich', 'can', 'move', 0, 0),
(188, 38, 'Fish', 'question', 'can shark eat?', 128, 2, 'shark', 'can', 'eat', 0, 0),
(189, 38, 'Fish', 'question', 'can shark breathe?', 132, 2, 'shark', 'can', 'breathe', 0, 0);

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
(48, 26, 'dog is a animal', 'dog', 'is a', 'animal'),
(49, 36, 'animal has skin', 'animal', 'has', 'skin'),
(50, 36, 'animal can move', 'animal', 'can', 'move'),
(51, 36, 'animal can eat', 'animal', 'can', 'eat'),
(52, 36, 'animal can breathe', 'animal', 'can', 'breathe'),
(53, 36, 'bird has wings', 'bird', 'has', 'wings'),
(54, 36, 'bird can fly', 'bird', 'can', 'fly'),
(55, 36, 'bird has feathers', 'bird', 'has', 'feathers'),
(56, 36, 'fish has fins', 'fish', 'has', 'fins'),
(57, 36, 'fish can swim', 'fish', 'can', 'swim'),
(58, 36, 'fish has gills', 'fish', 'has', 'gills'),
(59, 36, 'canary can sing', 'canary', 'can', 'sing'),
(60, 36, 'canary is yellow', 'canary', 'is', 'yellow'),
(61, 36, 'ostrich is tall', 'ostrich', 'is', 'tall'),
(62, 36, 'ostrich cannot fly', 'ostrich', 'cannot', 'fly'),
(63, 36, 'shark can bite', 'shark', 'can', 'bite'),
(64, 36, 'shark is dangerous', 'shark', 'is', 'dangerous'),
(65, 36, 'salmon is pink', 'salmon', 'is', 'pink'),
(66, 36, 'salmon is edible', 'salmon', 'is', 'edible'),
(67, 36, 'bird is a animal', 'bird', 'is a', 'animal'),
(68, 36, 'fish is a animal', 'fish', 'is a', 'animal'),
(69, 36, 'canary is a bird', 'canary', 'is a', 'bird'),
(70, 36, 'ostrich is a bird', 'ostrich', 'is a', 'bird'),
(71, 36, 'shark is a fish', 'shark', 'is a', 'fish'),
(72, 36, 'salmon is a fish', 'salmon', 'is a', 'fish'),
(73, 37, 'animal has skin', 'animal', 'has', 'skin'),
(74, 37, 'animal can move', 'animal', 'can', 'move'),
(75, 37, 'animal can eat', 'animal', 'can', 'eat'),
(76, 37, 'animal can breathe', 'animal', 'can', 'breathe'),
(77, 37, 'bird has wings', 'bird', 'has', 'wings'),
(78, 37, 'bird can fly', 'bird', 'can', 'fly'),
(79, 37, 'bird has feathers', 'bird', 'has', 'feathers'),
(80, 37, 'fish has fins', 'fish', 'has', 'fins'),
(81, 37, 'fish can swim', 'fish', 'can', 'swim'),
(82, 37, 'fish has gills', 'fish', 'has', 'gills'),
(83, 37, 'canary can sing', 'canary', 'can', 'sing'),
(84, 37, 'canary is yellow', 'canary', 'is', 'yellow'),
(85, 37, 'ostrich is tall', 'ostrich', 'is', 'tall'),
(86, 37, 'ostrich cannot fly', 'ostrich', 'cannot', 'fly'),
(87, 37, 'shark can bite', 'shark', 'can', 'bite'),
(88, 37, 'shark is dangerous', 'shark', 'is', 'dangerous'),
(89, 37, 'salmon is pink', 'salmon', 'is', 'pink'),
(90, 37, 'salmon is edible', 'salmon', 'is', 'edible'),
(91, 37, 'bird is a animal', 'bird', 'is a', 'animal'),
(92, 37, 'fish is a animal', 'fish', 'is a', 'animal'),
(93, 37, 'canary is a bird', 'canary', 'is a', 'bird'),
(94, 37, 'ostrich is a bird', 'ostrich', 'is a', 'bird'),
(95, 37, 'shark is a fish', 'shark', 'is a', 'fish'),
(96, 37, 'salmon is a fish', 'salmon', 'is a', 'fish'),
(97, 38, 'animal has skin', 'animal', 'has', 'skin'),
(98, 38, 'animal can move', 'animal', 'can', 'move'),
(99, 38, 'animal can eat', 'animal', 'can', 'eat'),
(100, 38, 'animal can breathe', 'animal', 'can', 'breathe'),
(101, 38, 'bird has wings', 'bird', 'has', 'wings'),
(102, 38, 'bird can fly', 'bird', 'can', 'fly'),
(103, 38, 'bird has feathers', 'bird', 'has', 'feathers'),
(104, 38, 'fish has fins', 'fish', 'has', 'fins'),
(105, 38, 'fish can swim', 'fish', 'can', 'swim'),
(106, 38, 'fish has gills', 'fish', 'has', 'gills'),
(107, 38, 'canary can sing', 'canary', 'can', 'sing'),
(108, 38, 'canary is yellow', 'canary', 'is', 'yellow'),
(109, 38, 'ostrich is tall', 'ostrich', 'is', 'tall'),
(110, 38, 'ostrich cannot fly', 'ostrich', 'cannot', 'fly'),
(111, 38, 'shark can bite', 'shark', 'can', 'bite'),
(112, 38, 'shark is dangerous', 'shark', 'is', 'dangerous'),
(113, 38, 'salmon is pink', 'salmon', 'is', 'pink'),
(114, 38, 'salmon is edible', 'salmon', 'is', 'edible'),
(115, 38, 'bird is a animal', 'bird', 'is a', 'animal'),
(116, 38, 'fish is a animal', 'fish', 'is a', 'animal'),
(117, 38, 'canary is a bird', 'canary', 'is a', 'bird'),
(118, 38, 'ostrich is a bird', 'ostrich', 'is a', 'bird'),
(119, 38, 'shark is a fish', 'shark', 'is a', 'fish'),
(120, 38, 'salmon is a fish', 'salmon', 'is a', 'fish');

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
(22, 'Cats', 'Added cats', 'Information about cats is added to the semantic memory'),
(23, 'Birds-Fish-Exp', 'This project is aimed at answering questions and based on two categories of animals: bird and fish', 'The formal model has to contain a semantic network that contains superordinate-subordinate category relations, such as a an Animal being a Living Thing, a Mammal being an Animal, and Dog being a Mammal. The network also must contain properties which are specific to entries, i.e., attributes, such as Dog –Barks, Animal – Breathes. But these are recorded at the highest superordinate level. So, it may be recorded that Animal – Breathes. It is not therefore necessary to have an attribute than Mammal – Breathes. Exceptions also have to be recorded as attributes. A Penguin is a Bird, and a Birds Fly are both represented as facts. But A penguin must have an attribute that it Cannot Fly. '),
(24, 'Birds-Fish-Learn', 'This project is aimed at learning facts and based on two categories of animals: bird and fish', '');

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
(63, 10, 'can hound move?', 'can', 'hound', 'move'),
(64, 36, 'is a canary canary?', 'is a', 'canary', 'canary'),
(66, 36, 'is a ostrich ostrich?', 'is a', 'ostrich', 'ostrich'),
(67, 36, 'is a shark shark?', 'is a', 'shark', 'shark'),
(68, 36, 'is a salmon salmon?', 'is a', 'salmon', 'salmon'),
(69, 36, 'is a bird bird?', 'is a', 'bird', 'bird'),
(70, 36, 'is a fish fish?', 'is a', 'fish', 'fish'),
(71, 36, 'is a animal animal?', 'is a', 'animal', 'animal'),
(72, 36, 'is a canary bird?', 'is a', 'canary', 'bird'),
(73, 36, 'is a ostrich bird?', 'is a', 'ostrich', 'bird'),
(74, 36, 'is a shark fish?', 'is a', 'shark', 'fish'),
(75, 36, 'is a salmon fish?', 'is a', 'salmon', 'fish'),
(76, 36, 'is a bird animal?', 'is a', 'bird', 'animal'),
(77, 36, 'is a fish animal?', 'is a', 'fish', 'animal'),
(78, 36, 'is a canary animal?', 'is a', 'canary', 'animal'),
(79, 36, 'is a ostrich animal?', 'is a', 'ostrich', 'animal'),
(80, 36, 'is a shark animal?', 'is a', 'shark', 'animal'),
(81, 36, 'is a salmon animal?', 'is a', 'salmon', 'animal'),
(82, 36, 'can canary sing?', 'can', 'canary', 'sing'),
(83, 36, 'is ostrich tall?', 'is', 'ostrich', 'tall'),
(84, 36, 'is shark dangerous?', 'is', 'shark', 'dangerous'),
(85, 36, 'is salmon edible?', 'is', 'salmon', 'edible'),
(86, 36, 'can bird fly?', 'can', 'bird', 'fly'),
(87, 36, 'can fish swim?', 'can', 'fish', 'swim'),
(88, 36, 'can animal move?', 'can', 'animal', 'move'),
(89, 36, 'can canary fly?', 'can', 'canary', 'fly'),
(96, 36, 'has canary wings?', 'has', 'canary', 'wings'),
(97, 36, 'has canary feathers?', 'has', 'canary', 'feathers'),
(98, 36, 'has shark fins?', 'has', 'shark', 'fins'),
(99, 36, 'can shark swim?', 'can', 'shark', 'swim'),
(100, 36, 'has shark gills?', 'has', 'shark', 'gills'),
(101, 36, 'has canary skin?', 'has', 'canary', 'skin'),
(102, 36, 'can ostrich move?', 'can', 'ostrich', 'move'),
(103, 36, 'can shark eat?', 'can', 'shark', 'eat'),
(104, 36, 'can shark breathe?', 'can', 'shark', 'breathe'),
(105, 37, 'is a canary canary?', 'is a', 'canary', 'canary'),
(106, 37, 'is a ostrich ostrich?', 'is a', 'ostrich', 'ostrich'),
(107, 37, 'is a shark shark?', 'is a', 'shark', 'shark'),
(108, 37, 'is a salmon salmon?', 'is a', 'salmon', 'salmon'),
(109, 37, 'is a bird bird?', 'is a', 'bird', 'bird'),
(110, 37, 'is a fish fish?', 'is a', 'fish', 'fish'),
(111, 37, 'is a animal animal?', 'is a', 'animal', 'animal'),
(112, 37, 'is a canary bird?', 'is a', 'canary', 'bird'),
(113, 37, 'is a ostrich bird?', 'is a', 'ostrich', 'bird'),
(114, 37, 'is a shark fish?', 'is a', 'shark', 'fish'),
(115, 37, 'is a salmon fish?', 'is a', 'salmon', 'fish'),
(116, 37, 'is a bird animal?', 'is a', 'bird', 'animal'),
(117, 37, 'is a fish animal?', 'is a', 'fish', 'animal'),
(118, 37, 'is a canary animal?', 'is a', 'canary', 'animal'),
(119, 37, 'is a ostrich animal?', 'is a', 'ostrich', 'animal'),
(120, 37, 'is a shark animal?', 'is a', 'shark', 'animal'),
(121, 37, 'is a salmon animal?', 'is a', 'salmon', 'animal'),
(122, 37, 'can canary sing?', 'can', 'canary', 'sing'),
(123, 37, 'is ostrich tall?', 'is', 'ostrich', 'tall'),
(124, 37, 'is shark dangerous?', 'is', 'shark', 'dangerous'),
(125, 37, 'is salmon edible?', 'is', 'salmon', 'edible'),
(126, 37, 'can bird fly?', 'can', 'bird', 'fly'),
(127, 37, 'can fish swim?', 'can', 'fish', 'swim'),
(128, 37, 'can animal move?', 'can', 'animal', 'move'),
(129, 37, 'can canary fly?', 'can', 'canary', 'fly'),
(130, 37, 'has canary wings?', 'has', 'canary', 'wings'),
(131, 37, 'has canary feathers?', 'has', 'canary', 'feathers'),
(132, 37, 'has shark fins?', 'has', 'shark', 'fins'),
(133, 37, 'can shark swim?', 'can', 'shark', 'swim'),
(134, 37, 'has shark gills?', 'has', 'shark', 'gills'),
(135, 37, 'has canary skin?', 'has', 'canary', 'skin'),
(136, 37, 'can ostrich move?', 'can', 'ostrich', 'move'),
(137, 37, 'can shark eat?', 'can', 'shark', 'eat'),
(138, 37, 'can shark breathe?', 'can', 'shark', 'breathe'),
(139, 36, 'is a bird fish?', 'is a', 'bird', 'fish'),
(140, 38, 'is a canary canary?', 'is a', 'canary', 'canary'),
(141, 38, 'is a ostrich ostrich?', 'is a', 'ostrich', 'ostrich'),
(142, 38, 'is a shark shark?', 'is a', 'shark', 'shark'),
(143, 38, 'is a salmon salmon?', 'is a', 'salmon', 'salmon'),
(144, 38, 'is a bird bird?', 'is a', 'bird', 'bird'),
(145, 38, 'is a fish fish?', 'is a', 'fish', 'fish'),
(146, 38, 'is a animal animal?', 'is a', 'animal', 'animal'),
(147, 38, 'is a canary bird?', 'is a', 'canary', 'bird'),
(148, 38, 'is a ostrich bird?', 'is a', 'ostrich', 'bird'),
(149, 38, 'is a shark fish?', 'is a', 'shark', 'fish'),
(150, 38, 'is a salmon fish?', 'is a', 'salmon', 'fish'),
(151, 38, 'is a bird animal?', 'is a', 'bird', 'animal'),
(152, 38, 'is a fish animal?', 'is a', 'fish', 'animal'),
(153, 38, 'is a canary animal?', 'is a', 'canary', 'animal'),
(154, 38, 'is a ostrich animal?', 'is a', 'ostrich', 'animal'),
(155, 38, 'is a shark animal?', 'is a', 'shark', 'animal'),
(156, 38, 'is a salmon animal?', 'is a', 'salmon', 'animal'),
(157, 38, 'can canary sing?', 'can', 'canary', 'sing'),
(158, 38, 'is ostrich tall?', 'is', 'ostrich', 'tall'),
(159, 38, 'is shark dangerous?', 'is', 'shark', 'dangerous'),
(160, 38, 'is salmon edible?', 'is', 'salmon', 'edible'),
(161, 38, 'can bird fly?', 'can', 'bird', 'fly'),
(162, 38, 'can fish swim?', 'can', 'fish', 'swim'),
(163, 38, 'can animal move?', 'can', 'animal', 'move'),
(164, 38, 'can canary fly?', 'can', 'canary', 'fly'),
(165, 38, 'has canary wings?', 'has', 'canary', 'wings'),
(166, 38, 'has canary feathers?', 'has', 'canary', 'feathers'),
(167, 38, 'has shark fins?', 'has', 'shark', 'fins'),
(168, 38, 'can shark swim?', 'can', 'shark', 'swim'),
(169, 38, 'has shark gills?', 'has', 'shark', 'gills'),
(170, 38, 'has canary skin?', 'has', 'canary', 'skin'),
(171, 38, 'can ostrich move?', 'can', 'ostrich', 'move'),
(172, 38, 'can shark eat?', 'can', 'shark', 'eat'),
(173, 38, 'can shark breathe?', 'can', 'shark', 'breathe');

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
(9135, 36, 'Animals', 'animal can breathe', 1, 'animal', 'can', 'breathe'),
(9136, 36, 'Animals', 'animal can eat', 1, 'animal', 'can', 'eat'),
(9137, 36, 'Animals', 'animal can move', 1, 'animal', 'can', 'move'),
(9138, 36, 'Animals', 'animal has skin', 1, 'animal', 'has', 'skin'),
(9139, 36, 'Birds', 'bird can fly', 1, 'bird', 'can', 'fly'),
(9140, 36, 'Birds', 'bird has feathers', 1, 'bird', 'has', 'feathers'),
(9141, 36, 'Birds', 'bird has wings', 1, 'bird', 'has', 'wings'),
(9142, 36, 'Birds', 'bird is a animal', 1, 'bird', 'is a', 'animal'),
(9143, 36, 'Birds', 'canary can sing', 1, 'canary', 'can', 'sing'),
(9144, 36, 'Birds', 'canary is yellow', 1, 'canary', 'is', 'yellow'),
(9145, 36, 'Birds', 'canary is a bird', 1, 'canary', 'is a', 'bird'),
(9146, 36, 'Birds', 'ostrich cannot fly', 1, 'ostrich', 'cannot', 'fly'),
(9147, 36, 'Birds', 'ostrich is tall', 1, 'ostrich', 'is', 'tall'),
(9148, 36, 'Birds', 'ostrich is a bird', 1, 'ostrich', 'is a', 'bird'),
(9149, 36, 'Fish', 'fish can swim', 1, 'fish', 'can', 'swim'),
(9150, 36, 'Fish', 'fish has fins', 1, 'fish', 'has', 'fins'),
(9151, 36, 'Fish', 'fish has gills', 1, 'fish', 'has', 'gills'),
(9152, 36, 'Fish', 'fish is a animal', 1, 'fish', 'is a', 'animal'),
(9153, 36, 'Fish', 'salmon is edible', 1, 'salmon', 'is', 'edible'),
(9154, 36, 'Fish', 'salmon is pink', 1, 'salmon', 'is', 'pink'),
(9155, 36, 'Fish', 'salmon is a fish', 1, 'salmon', 'is a', 'fish'),
(9156, 36, 'Fish', 'shark is dangerous', 1, 'shark', 'is', 'dangerous'),
(9157, 36, 'Fish', 'shark can bite', 1, 'shark', 'can', 'bite'),
(9158, 36, 'Fish', 'shark is a fish', 1, 'shark', 'is a', 'fish'),
(9265, 10, 'animals', 'animal can breath', 1, 'animal', 'can', 'breath'),
(9266, 10, 'animals', 'animal can move', 1, 'animal', 'can', 'move'),
(9267, 10, 'animals', 'dog is a animal', 1, 'dog', 'is a', 'animal'),
(9268, 10, 'dogs', 'basenji cannot bark', 1, 'basenji', 'cannot', 'bark'),
(9269, 10, 'dogs', 'basenji is a hound', 1, 'basenji', 'is a', 'hound'),
(9270, 10, 'dogs', 'bobby can lay', 1, 'bobby', 'can', 'lay'),
(9271, 10, 'dogs', 'bobby is a basenji', 1, 'bobby', 'is a', 'basenji'),
(9272, 10, 'dogs', 'dog can bark', 1, 'dog', 'can', 'bark'),
(9273, 10, 'dogs', 'dog is a animal', 1, 'dog', 'is a', 'animal'),
(9274, 10, 'dogs', 'hound can track', 1, 'hound', 'can', 'track'),
(9481, 37, 'Animals', 'animal can breathe', 1, 'animal', 'can', 'breathe'),
(9482, 37, 'Animals', 'animal can eat', 1, 'animal', 'can', 'eat'),
(9483, 37, 'Animals', 'animal can move', 1, 'animal', 'can', 'move'),
(9484, 37, 'Animals', 'animal has skin', 1, 'animal', 'has', 'skin'),
(9485, 38, 'Animals', 'animal can breathe', 1, 'animal', 'can', 'breathe'),
(9486, 38, 'Animals', 'animal can eat', 1, 'animal', 'can', 'eat'),
(9487, 38, 'Animals', 'animal can move', 1, 'animal', 'can', 'move'),
(9488, 38, 'Animals', 'animal has skin', 1, 'animal', 'has', 'skin');

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
(76, 26, 'cannot'),
(77, 36, 'can'),
(78, 36, 'is'),
(79, 36, 'is a'),
(80, 36, 'has'),
(81, 36, 'cannot'),
(82, 37, 'can'),
(83, 37, 'is'),
(84, 37, 'is a'),
(85, 37, 'has'),
(86, 37, 'cannot'),
(87, 38, 'can'),
(88, 38, 'is'),
(89, 38, 'is a'),
(90, 38, 'has'),
(91, 38, 'cannot');

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
(35, 'First', 'Cats', 1, 'Very first version', ''),
(36, 'Full example', 'Birds-Fish-Exp', 1, 'This is the full version', 'This version is done with the basic example'),
(37, 'Fast addition', 'Birds-Fish-Learn', 1, 'In this version facts start every 2 sec', ''),
(38, 'Slow addition', 'Birds-Fish-Learn', 2, 'In this version facts start every 10 sec', '');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=242;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `environment`
--
ALTER TABLE `environment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `experiment`
--
ALTER TABLE `experiment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `facts`
--
ALTER TABLE `facts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT for table `perceptions`
--
ALTER TABLE `perceptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=174;

--
-- AUTO_INCREMENT for table `sem_mem`
--
ALTER TABLE `sem_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9518;

--
-- AUTO_INCREMENT for table `short_term_mem`
--
ALTER TABLE `short_term_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;

--
-- AUTO_INCREMENT for table `versions`
--
ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

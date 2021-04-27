-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 27, 2021 at 07:49 PM
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
(193, 36, 'animal');

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
(102, 36, 'salmon');

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
(68, 36, 'Fish');

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
  `attributes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `experiment`
--

INSERT INTO `experiment` (`id`, `version_id`, `domain`, `item`, `value`, `future_time`, `persist_time`, `categories`, `types`, `attributes`) VALUES
(27, 10, 'animals', 'question', 'can hound move?', 3, 3, 'hound', 'can', 'move'),
(28, 10, 'animals', 'question', 'can animal move?', 6, 2, 'animal', 'can', 'move'),
(29, 10, 'animals', 'question', 'can basenji breath?', 14, 50, 'basenji', 'can', 'breath'),
(32, 10, 'animals', 'fact', 'animal can breath', 10, 20, 'animal', 'can', 'breath'),
(33, 36, 'Birds', 'question', 'is a canary canary?', 0, 2, 'canary', 'is a', 'canary'),
(34, 36, 'Birds', 'question', 'is a ostrich ostrich?', 4, 2, 'ostrich', 'is a', 'ostrich'),
(35, 36, 'Fish', 'question', 'is a shark shark?', 8, 2, 'shark', 'is a', 'shark'),
(36, 36, 'Fish', 'question', 'is a salmon salmon?', 12, 2, 'salmon', 'is a', 'salmon'),
(37, 36, 'Birds', 'question', 'is a bird bird?', 16, 2, 'bird', 'is a', 'bird'),
(38, 36, 'Fish', 'question', 'is a fish fish?', 20, 2, 'fish', 'is a', 'fish'),
(39, 36, 'Animals', 'question', 'is a animal animal?', 24, 2, 'animal', 'is a', 'animal'),
(40, 36, 'Birds', 'question', 'is a canary bird?', 28, 2, 'canary', 'is a', 'bird'),
(41, 36, 'Birds', 'question', 'is a ostrich bird?', 32, 2, 'ostrich', 'is a', 'bird'),
(42, 36, 'Fish', 'question', 'is a shark fish?', 36, 2, 'shark', 'is a', 'fish'),
(43, 36, 'Fish', 'question', 'is a salmon fish?', 40, 2, 'salmon', 'is a', 'fish'),
(44, 36, 'Birds', 'question', 'is a bird animal?', 44, 2, 'bird', 'is a', 'animal'),
(45, 36, 'Fish', 'question', 'is a fish animal?', 48, 2, 'fish', 'is a', 'animal'),
(46, 36, 'Birds', 'question', 'is a canary animal?', 52, 2, 'canary', 'is a', 'animal'),
(47, 36, 'Birds', 'question', 'is a ostrich animal?', 56, 2, 'ostrich', 'is a', 'animal'),
(48, 36, 'Fish', 'question', 'is a shark animal?', 60, 2, 'shark', 'is a', 'animal'),
(49, 36, 'Fish', 'question', 'is a salmon animal?', 64, 2, 'salmon', 'is a', 'animal'),
(50, 36, 'Birds', 'question', 'can canary sing?', 68, 2, 'canary', 'can', 'sing'),
(51, 36, 'Birds', 'question', 'is ostrich tall?', 72, 2, 'ostrich', 'is', 'tall'),
(52, 36, 'Fish', 'question', 'is shark dangerous?', 76, 2, 'shark', 'is', 'dangerous'),
(53, 36, 'Fish', 'question', 'is salmon edible?', 80, 2, 'salmon', 'is', 'edible'),
(54, 36, 'Birds', 'question', 'can bird fly?', 84, 2, 'bird', 'can', 'fly'),
(55, 36, 'Fish', 'question', 'can fish swim?', 88, 2, 'fish', 'can', 'swim'),
(56, 36, 'Animals', 'question', 'can animal move?', 92, 2, 'animal', 'can', 'move'),
(57, 36, 'Birds', 'question', 'can canary fly?', 96, 2, 'canary', 'can', 'fly'),
(58, 36, 'Birds', 'question', 'has canary wings?', 100, 2, 'canary', 'has', 'wings'),
(59, 36, 'Birds', 'question', 'has canary feathers?', 104, 2, 'canary', 'has', 'feathers'),
(60, 36, 'Fish', 'question', 'has shark fins?', 108, 2, 'shark', 'has', 'fins'),
(61, 36, 'Fish', 'question', 'can shark swim?', 112, 2, 'shark', 'can', 'swim'),
(62, 36, 'Fish', 'question', 'has shark gills?', 116, 2, 'shark', 'has', 'gills'),
(63, 36, 'Birds', 'question', 'has canary skin?', 120, 2, 'canary', 'has', 'skin'),
(64, 36, 'Birds', 'question', 'can ostrich move?', 124, 2, 'ostrich', 'can', 'move'),
(65, 36, 'Fish', 'question', 'can shark eat?', 128, 2, 'shark', 'can', 'eat'),
(66, 36, 'Fish', 'question', 'can shark breathe?', 132, 2, 'shark', 'can', 'breathe'),
(71, 36, 'Fish', 'fact', 'salmon is pink', 0, 2, 'salmon', 'is', 'pink'),
(72, 36, 'Fish', 'fact', 'salmon is edible', 2, 2, 'salmon', 'is', 'edible'),
(73, 36, 'Fish', 'fact', 'shark can bite', 4, 2, 'shark', 'can', 'bite');

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
(72, 36, 'salmon is a fish', 'salmon', 'is a', 'fish');

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
(23, 'Animals_full', 'This project is based on two categories of animals: bird and fish', 'The formal model has to contain a semantic network that contains superordinate-subordinate category relations, such as a an Animal being a Living Thing, a Mammal being an Animal, and Dog being a Mammal. The network also must contain properties which are specific to entries, i.e., attributes, such as Dog –Barks, Animal – Breathes. But these are recorded at the highest superordinate level. So, it may be recorded that Animal – Breathes. It is not therefore necessary to have an attribute than Mammal – Breathes. Exceptions also have to be recorded as attributes. A Penguin is a Bird, and a Birds Fly are both represented as facts. But A penguin must have an attribute that it Cannot Fly. ');

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
(104, 36, 'can shark breathe?', 'can', 'shark', 'breathe');

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
(8852, 10, 'animals', 'animal can breath', 1, 'animal', 'can', 'breath'),
(8853, 10, 'animals', 'animal can move', 1, 'animal', 'can', 'move'),
(8854, 10, 'animals', 'hound can track', 1, 'hound', 'can', 'track'),
(8855, 10, 'dogs', 'basenji is a hound', 1, 'basenji', 'is a', 'hound'),
(8856, 10, 'dogs', 'basenji cannot bark', 1, 'basenji', 'cannot', 'bark'),
(8857, 10, 'dogs', 'bobby can lay', 1, 'bobby', 'can', 'lay'),
(8858, 10, 'dogs', 'bobby is a basenji', 1, 'bobby', 'is a', 'basenji'),
(8859, 10, 'dogs', 'dog can bark', 1, 'dog', 'can', 'bark'),
(8860, 10, 'dogs', 'dog is a animal', 1, 'dog', 'is a', 'animal'),
(8861, 10, 'dogs', 'hound can bark', 1, 'hound', 'can', 'bark'),
(8862, 10, 'dogs', 'hound is a dog', 1, 'hound', 'is a', 'dog'),
(9113, 36, 'Animals', 'animal can breathe', 1, 'animal', 'can', 'breathe'),
(9114, 36, 'Animals', 'animal can eat', 1, 'animal', 'can', 'eat'),
(9115, 36, 'Animals', 'animal can move', 1, 'animal', 'can', 'move'),
(9116, 36, 'Animals', 'animal has skin', 1, 'animal', 'has', 'skin'),
(9117, 36, 'Birds', 'bird is a animal', 1, 'bird', 'is a', 'animal'),
(9118, 36, 'Birds', 'bird can fly', 1, 'bird', 'can', 'fly'),
(9119, 36, 'Birds', 'bird has feathers', 1, 'bird', 'has', 'feathers'),
(9120, 36, 'Birds', 'bird has wings', 1, 'bird', 'has', 'wings'),
(9121, 36, 'Birds', 'canary is a bird', 1, 'canary', 'is a', 'bird'),
(9122, 36, 'Birds', 'canary can sing', 1, 'canary', 'can', 'sing'),
(9123, 36, 'Birds', 'canary is yellow', 1, 'canary', 'is', 'yellow'),
(9124, 36, 'Birds', 'ostrich is a bird', 1, 'ostrich', 'is a', 'bird'),
(9125, 36, 'Birds', 'ostrich is tall', 1, 'ostrich', 'is', 'tall'),
(9126, 36, 'Birds', 'ostrich cannot fly', 1, 'ostrich', 'cannot', 'fly'),
(9127, 36, 'Fish', 'fish is a animal', 1, 'fish', 'is a', 'animal'),
(9128, 36, 'Fish', 'fish can swim', 1, 'fish', 'can', 'swim'),
(9129, 36, 'Fish', 'fish has fins', 1, 'fish', 'has', 'fins'),
(9130, 36, 'Fish', 'fish has gills', 1, 'fish', 'has', 'gills'),
(9131, 36, 'Fish', 'salmon is edible', 1, 'salmon', 'is', 'edible'),
(9132, 36, 'Fish', 'salmon is a fish', 1, 'salmon', 'is a', 'fish'),
(9133, 36, 'Fish', 'shark is a fish', 1, 'shark', 'is a', 'fish'),
(9134, 36, 'Fish', 'shark is dangerous', 1, 'shark', 'is', 'dangerous');

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
(81, 36, 'cannot');

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
(36, 'Trial', 'Animals_full', 1, 'This is the first trial version', 'This version is done with the basic example');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=194;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `environment`
--
ALTER TABLE `environment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `experiment`
--
ALTER TABLE `experiment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `facts`
--
ALTER TABLE `facts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `perceptions`
--
ALTER TABLE `perceptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `sem_mem`
--
ALTER TABLE `sem_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9135;

--
-- AUTO_INCREMENT for table `short_term_mem`
--
ALTER TABLE `short_term_mem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `versions`
--
ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

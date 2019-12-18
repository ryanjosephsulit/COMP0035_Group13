-- phpMyAdmin SQL Dump
-- version 5.1.0-dev
-- https://www.phpmyadmin.net/
--
-- Host: 192.168.30.23
-- Generation Time: Dec 17, 2019 at 05:14 PM
-- Server version: 8.0.18
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zcecrjs`
--

-- --------------------------------------------------------

--
-- Table structure for table `bank_account`
--

CREATE TABLE `bank_account` (
  `learner_id` int(10) NOT NULL,
  `teacher_id` int(10) NOT NULL,
  `payment_type` enum('a','b') NOT NULL,
  `payment_details` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `forum_post`
--

CREATE TABLE `forum_post` (
  `post_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `content` varchar(10) NOT NULL,
  `likes` int(10) NOT NULL,
  `comment` varchar(10) NOT NULL,
  `posted_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `langcoin_wallet`
--

CREATE TABLE `langcoin_wallet` (
  `wallet_id` int(10) NOT NULL,
  `teacher_user_id` int(10) NOT NULL,
  `learner_user_id` int(10) NOT NULL,
  `langCoin_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `learner`
--

CREATE TABLE `learner` (
  `user_id` int(10) NOT NULL,
  `user_name` char(10) DEFAULT NULL,
  `languages_learning` enum('a','b') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

CREATE TABLE `lesson` (
  `lesson_id` int(10) NOT NULL,
  `learner_id` int(10) NOT NULL,
  `teacher_id` int(10) NOT NULL,
  `aim` varchar(10) NOT NULL,
  `format` enum('a','b','c') NOT NULL,
  `time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lesson_review`
--

CREATE TABLE `lesson_review` (
  `learner_id` int(10) NOT NULL,
  `lesson_no` int(10) NOT NULL,
  `rating` int(10) NOT NULL,
  `comment` varchar(10) NOT NULL,
  `reviewed_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `user_id` int(10) NOT NULL,
  `user_name` char(10) NOT NULL,
  `languages_teaching` enum('a','b') NOT NULL,
  `rating` int(10) NOT NULL,
  `reviews` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bank_account`
--
ALTER TABLE `bank_account`
  ADD KEY `learner_id` (`learner_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `forum_post`
--
ALTER TABLE `forum_post`
  ADD PRIMARY KEY (`post_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `langcoin_wallet`
--
ALTER TABLE `langcoin_wallet`
  ADD PRIMARY KEY (`wallet_id`),
  ADD KEY `teacher_user_id` (`teacher_user_id`),
  ADD KEY `learner_user_id` (`learner_user_id`);

--
-- Indexes for table `learner`
--
ALTER TABLE `learner`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`lesson_id`),
  ADD KEY `learner_id` (`learner_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `lesson_review`
--
ALTER TABLE `lesson_review`
  ADD KEY `learner_id` (`learner_id`),
  ADD KEY `lesson_no` (`lesson_no`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bank_account`
--
ALTER TABLE `bank_account`
  ADD CONSTRAINT `bank_account_ibfk_1` FOREIGN KEY (`learner_id`) REFERENCES `learner` (`user_id`);

--
-- Constraints for table `forum_post`
--
ALTER TABLE `forum_post`
  ADD CONSTRAINT `forum_post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `learner` (`user_id`);

--
-- Constraints for table `langcoin_wallet`
--
ALTER TABLE `langcoin_wallet`
  ADD CONSTRAINT `langcoin_wallet_ibfk_1` FOREIGN KEY (`teacher_user_id`) REFERENCES `teacher` (`user_id`),
  ADD CONSTRAINT `langcoin_wallet_ibfk_2` FOREIGN KEY (`learner_user_id`) REFERENCES `learner` (`user_id`);

--
-- Constraints for table `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `lesson_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`user_id`),
  ADD CONSTRAINT `lesson_ibfk_2` FOREIGN KEY (`learner_id`) REFERENCES `learner` (`user_id`);

--
-- Constraints for table `lesson_review`
--
ALTER TABLE `lesson_review`
  ADD CONSTRAINT `lesson_review_ibfk_1` FOREIGN KEY (`learner_id`) REFERENCES `learner` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


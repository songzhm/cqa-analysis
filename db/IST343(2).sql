/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 50716
 Source Host           : localhost
 Source Database       : IST343

 Target Server Type    : MySQL
 Target Server Version : 50716
 File Encoding         : utf-8

 Date: 11/16/2016 21:58:14 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `ANSWER`
-- ----------------------------
DROP TABLE IF EXISTS `ANSWER`;
CREATE TABLE `ANSWER` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ANSWER_ID` varchar(255) NOT NULL,
  `QUESTION_ID` varchar(255) NOT NULL,
  `USER_ID` varchar(255) NOT NULL,
  `CONTENT` varchar(255) NOT NULL,
  `ANSWER_HTML` varchar(255) NOT NULL,
  `USER_HAS_SUPPORTED` varchar(255) NOT NULL,
  `UPVOTING` int(11) NOT NULL,
  `DOWNVOTING` int(11) NOT NULL,
  `SUPPORTING_COUNT` int(11) NOT NULL,
  `DATA_CREATED` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DATA_MODIFIED` datetime NOT NULL,
  `ANSWER_URL` varchar(255) NOT NULL,
  `OPPOSING_COUNT` int(11) NOT NULL,
  `BURYING_COUNT` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `ANSWER_SUPPORT`
-- ----------------------------
DROP TABLE IF EXISTS `ANSWER_SUPPORT`;
CREATE TABLE `ANSWER_SUPPORT` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(255) NOT NULL,
  `ANSWER_ID` varchar(255) NOT NULL,
  `QUESTION_ID` varchar(255) NOT NULL,
  `DATA_CREATED` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `OPINION` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `QUESTION`
-- ----------------------------
DROP TABLE IF EXISTS `QUESTION`;
CREATE TABLE `QUESTION` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `QUESTION_ID` varchar(255) NOT NULL,
  `USER_ID` varchar(255) NOT NULL,
  `QUSETION` varchar(255) NOT NULL,
  `SUMMARY` varchar(255) NOT NULL,
  `ANSWER_COUNT` int(11) NOT NULL,
  `FOLLOWER_COUNT` int(11) NOT NULL,
  `ARCHIVE_COUNT` int(11) NOT NULL,
  `DATA_CREATED` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DATA_LAST_ANSWERED` datetime NOT NULL,
  `QUESTION_URL` varchar(255) NOT NULL,
  `REPLY_COUNT` int(11) DEFAULT NULL,
  `RECOMMEND_COUNT` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `QUESTION_TAG`
-- ----------------------------
DROP TABLE IF EXISTS `QUESTION_TAG`;
CREATE TABLE `QUESTION_TAG` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `QUESTION_ID` varchar(255) DEFAULT NULL,
  `TAG_NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `TAG`
-- ----------------------------
DROP TABLE IF EXISTS `TAG`;
CREATE TABLE `TAG` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TAG_NAME` varchar(255) NOT NULL,
  `SUMMARY` varchar(255) NOT NULL,
  `QUESTION_COUNT` int(11) NOT NULL,
  `FOLLOWER_COUNT` int(11) NOT NULL,
  `DATE_CREATED` datetime NOT NULL,
  `DATE_MODIFIED` datetime NOT NULL,
  `TAG_URL` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `USER_PROFILE`
-- ----------------------------
DROP TABLE IF EXISTS `USER_PROFILE`;
CREATE TABLE `USER_PROFILE` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(255) NOT NULL,
  `NICKNAME` varchar(255) NOT NULL,
  `GENDER` varchar(255) DEFAULT NULL,
  `CITY` varchar(255) DEFAULT NULL,
  `AREA` varchar(255) DEFAULT NULL,
  `INTRODUCTION` varchar(255) DEFAULT NULL,
  `MASTER_INTRODUCTION` varchar(255) DEFAULT NULL,
  `QUESTION_COUNT` int(11) NOT NULL,
  `ANSWER_COUNT` int(11) NOT NULL,
  `ANSWER_SUPPORT_COUNT` int(11) NOT NULL,
  `FOLLOWER_COUNT` int(11) NOT NULL,
  `FOLLOWING_COUNT` int(11) NOT NULL,
  `ACTIVITY_COUNT` int(11) NOT NULL,
  `POST_COUNT` int(11) NOT NULL,
  `DATE_CREATED` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `USER_URL` varchar(255) DEFAULT NULL,
  `RESOURCE_URL` varchar(255) NOT NULL,
  `BADGE_COPPER` int(11) DEFAULT NULL,
  `BADGE_SILVER` int(11) DEFAULT NULL,
  `BADGE_GOLD` int(11) DEFAULT NULL,
  `BADGE_TOTAL` int(11) DEFAULT NULL,
  `EVENT_VIDEO` int(11) DEFAULT NULL,
  `TITLE_AUTHORIED` varchar(255) DEFAULT NULL,
  `MASTER_CATEGORY` varchar(255) DEFAULT NULL,
  `AMENDED_RELIABILITY` varchar(255) DEFAULT NULL,
  `TITLE` varchar(255) DEFAULT NULL,
  `BLOG_TITLE` varchar(255) DEFAULT NULL,
  `TAGGING` varchar(255) DEFAULT NULL,
  `BLOG_COUNT` int(11) NOT NULL,
  `BLOG_URL` varchar(255) DEFAULT NULL,
  `BASKET_COUNT` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
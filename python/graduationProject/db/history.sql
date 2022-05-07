/*
 Navicat Premium Data Transfer

 Source Server         : 本地数据库
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 14/04/2022 16:18:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `history` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mid` varchar(0) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `userid` varchar(0) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` varchar(0) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

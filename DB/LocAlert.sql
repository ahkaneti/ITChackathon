DROP TABLE IF EXISTS `Report_Kinds`;
DROP TABLE IF EXISTS `Users`;
DROP TABLE IF EXISTS `Reports`;
DROP TABLE IF EXISTS `New_Groups`;
DROP TABLE IF EXISTS `User_Groups`;
DROP TABLE IF EXISTS `Positions`;
DROP TABLE IF EXISTS `Alerts`;

CREATE TABLE `Report_Kinds` (
  `report_kind` int PRIMARY KEY,
  `report_name` varchar(20),
  `report_description` varchar(100),
  `radius_dist` int
);


CREATE TABLE `Users`
(
  `user_id` int PRIMARY KEY,
  `user_name` varchar(20),
  `email` varchar(30),
  `address` varchar(30),
  `phone_numbers` varchar(20)
);

CREATE TABLE `New_Groups` (
  `group_id` int PRIMARY KEY,
  `group_name` varchar(30)
);

CREATE TABLE `User_Groups` (
  `group_id` int,
  `user_id` int,
  FOREIGN KEY (`group_id`) REFERENCES New_Groups(`group_id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`user_id`)
);

CREATE TABLE `Positions` (
  `position_id` int PRIMARY KEY,
  `longitude` int,
  `latitude` int
);

CREATE TABLE `Reports` (
  `report_id` int PRIMARY KEY,
  `report_kind` int,
  `position_id` int,
  `user_id` int,
  `report_date` TIMESTAMP,
  FOREIGN KEY (`user_id`) REFERENCES Users(`user_id`),
  FOREIGN KEY (`report_kind`) REFERENCES Report_Kinds(`report_kind`),
  FOREIGN KEY (`position_id`) REFERENCES Positions(`position_id`)
);

CREATE TABLE `Alerts` (
  `alert_id` int PRIMARY KEY,
  `user_id` int,
  `group_id` int,
  `position_id` int,
  FOREIGN KEY (`user_id`) REFERENCES Users(`user_id`),
  FOREIGN KEY (`group_id`) REFERENCES User_Groups(`group_id`),
  FOREIGN KEY (`position_id`) REFERENCES Positions(`position_id`)
);

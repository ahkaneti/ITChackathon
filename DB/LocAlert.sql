"""
DROP TABLE IF EXISTS `teams_informations`;
DROP TABLE IF EXISTS `trophies`;
DROP TABLE IF EXISTS `matches`;
DROP TABLE IF EXISTS `top_players`;
DROP TABLE IF EXISTS `players_from_api`;
"""

CREATE TABLE `Users`
{
  user_id int PRIMARY KEY,
  user_name varchar(20)
  email varchar(30),
  address varchar(30),
  phone_number varchar(20)
};

CREATE TABLE `Reports` {
  report_id int PRIMARY KEY,
  report_kind int,
  user_id int,
  report_date TIMESTAMP
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
  FOREIGN KEY (report_kind) REFERENCES Report_Kinds(report_kind)
};

CREATE TABLE `Report_Kinds` {
  report_kind int PRIMARY KEY,
  report_name varchar(20),
  radius_dist int
};

CREATE TABLE `Groups` {
  group_number int,
  user_id int
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
};

CREATE TABLE `Positions` {
  report_id int PRIMARY KEY,
  longitude int,
  latitude int
  FOREIGN KEY (report_id) REFERENCES Reports(report_id)
};
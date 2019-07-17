DROP TABLE IF EXISTS `Users`;
DROP TABLE IF EXISTS `Reports`;
DROP TABLE IF EXISTS `Report_Kinds`;
DROP TABLE IF EXISTS `User_Groups`;
DROP TABLE IF EXISTS `Positions`;
DROP TABLE IF EXISTS `Alerts`;


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
  position_id int
  user_id int,
  report_date TIMESTAMP
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
  FOREIGN KEY (report_kind) REFERENCES Report_Kinds(report_kind)
  FOREIGN KEY (position_id) REFERENCES Positions(position_id)
};

CREATE TABLE `Report_Kinds` {
  report_kind int PRIMARY KEY,
  report_name varchar(20),
  radius_dist int
};

CREATE TABLE `User_Groups` {
  group_number int,
  user_id int
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
};

CREATE TABLE `Positions` {
  position_id int PRIMARY KEY,
  longitude int,
  latitude int
  FOREIGN KEY (position_id) REFERENCES Reports(position_id)
};

CREATE TABLE `Alerts` {
  alert_id int PRIMARY KEY,
  user_id int,
  group_number int
  position_id int
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
  FOREIGN KEY (group_number) REFERENCES User_Groups(group_number)
  FOREIGN KEY (position_id) REFERENCES Positions(position_id)
}

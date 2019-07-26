CREATE TABLE IF NOT EXISTS `BucketList`.`employees` (
`user_id` BIGINT UNIQUE AUTO_INCREMENT,
`first_name` VARCHAR(255) NULL,
PRIMARY KEY (`user_id`));

INSERT INTO `BucketList`.`employees` (`first_name`) VALUES ('Piter Parker');
INSERT INTO `BucketList`.`employees` (`first_name`) VALUES ('Superman');
INSERT INTO `BucketList`.`employees` (`first_name`) VALUES ('Wolverine');

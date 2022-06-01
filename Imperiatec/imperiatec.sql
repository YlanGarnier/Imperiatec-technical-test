CREATE DATABASE IF NOT EXISTS imperiatecdb;

use imperiatecdb;

CREATE TABLE IF NOT EXISTS `user` (
    `id` INT unsigned NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `login` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `reservation` (
    `id` INT unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `date` DATE NOT NULL,
    `debut_time` TIME NOT NULL,
    `end_time` TIME NOT NULL,
    `user_id` INT(20) unsigned NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `imperiatecdb`.`user`(`id`)
);

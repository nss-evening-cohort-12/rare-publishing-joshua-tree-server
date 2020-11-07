CREATE TABLE `Users` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  `display_name` VARCHAR(20) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `password` VARCHAR(12) NOT NULL
);

CREATE TABLE `Categories` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `category_name` VARCHAR(20) NOT NULL
);

CREATE TABLE `Posts` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `title` VARCHAR(30) NOT NULL,
  `content` TEXT NOT NULL,
  `category_id` INTEGER NOT NULL,
  `publication_date` DATE NOT NULL,
  `image_url` TEXT,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY (`category_id`) REFERENCES `Categories`(`id`)
);

CREATE TABLE `Tags` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(15) NOT NULL
);

CREATE TABLE `Post_Tags` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER NOT NULL,
  `tag_id` INTEGER NOT NULL,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE `Comments` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `post_id` INTEGER NOT NULL,
  `subject`  VARCHAR(30) NOT NULL,
  `content` TEXT NOT NULL,
  `creation_date` DATE NOT NULL,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

INSERT INTO `Users` VALUES (null, 'Bob', 'Smith', 'TitansFan2020', 'bobsmith@aol.com', 'password');
INSERT INTO `Users` VALUES (null, 'Kate', 'Johnson', 'ILoveCats', 'katejohnson2@yahoo.com', 'password');
INSERT INTO `Users` VALUES (null, 'Alex', 'Page', 'PythonR00lz', 'alexpage@gmail.com', 'password');

INSERT INTO `Categories` VALUES (null, 'Sports');
INSERT INTO `Categories` VALUES (null, 'Technology');
INSERT INTO `Categories` VALUES (null, 'Music');
INSERT INTO `Categories` VALUES (null, 'Pets');

INSERT INTO `Posts` VALUES (null, 2, 'The 5 Best Cat Breeds', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer bibendum sapien in mi congue varius. Vestibulum nec eros nec ante tempus porttitor. Nullam sit amet justo ligula. Nam eu tellus vel nisl tempus varius.', 4, '10/23/2020', 'https://www.animalclinicofwoodruff.com/files/cat-breeds1059943207.jpg');
INSERT INTO `Posts` VALUES (null, 1, 'How Covid Has Impacted the NFL', 'Duis eu libero enim. Donec gravida aliquam arcu, vitae viverra diam tincidunt a. Etiam luctus quis nisi ac malesuada.', 1, '11/01/2020', 'https://static.www.nfl.com/image/private/t_editorial_landscape_3_4_desktop_2x/f_auto/league/urdgxtnk14li98mcjcqv.jpg');

INSERT INTO `Tags` VALUES (null, 'Travel');
INSERT INTO `Tags` VALUES (null, 'Relationships');
INSERT INTO `Tags` VALUES (null, 'Cats');
INSERT INTO `Tags` VALUES (null, 'Football');
INSERT INTO `Tags` VALUES (null, 'Python');

INSERT INTO `Post_Tags` VALUES (null, 1, 3);
INSERT INTO `Post_Tags` VALUES (null, 2, 4);

INSERT INTO `Comments` VALUES (null, 3, 2, 'Football', 'Great article, thanks!', 11/01/2020);
INSERT INTO `Comments` VALUES (null, 1, 1, 'Cats', "I've owned three of the breeds you wrote about, and I agree that they make great pets!", 10/25/2020);

SELECT * FROM Users

SELECT * FROM Posts


-- TRUNCATE TABLE Comments;
drop TABLE Comments
drop table Tags
drop TABLE Post_Tags
DROP TABLE Posts
DROP TABLE Categories
DROP TABLE Users

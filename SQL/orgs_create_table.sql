CREATE TABLE `orgs` (
  `orgID` int(11) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `zip` varchar(10) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `fax` varchar(25) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `orgurl` varchar(250) DEFAULT NULL,
  `facebookUrl` varchar(250) DEFAULT NULL,
  `orgType` varchar(50) DEFAULT NULL,
  `orgSpecies` varchar(50) DEFAULT NULL,
  `serveAreas` text,
  `about` text,
  `meetPets` text,
  `services` text,
  `allowAppSubmissions` varchar(250) DEFAULT NULL,
  `messageOrg` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`orgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SELECT `user`.`userid`, `user`.`leaderid` FROM `user`
WHERE `user`.`leaderid` NOT IN (SELECT saler.userid FROM saler)
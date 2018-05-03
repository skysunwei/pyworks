1. 线上查询库：https://msn.youhaodongxi.com/index.php
    1. User name: readonly
    2. Password: Readonly2016





SELECT saler.userid,
       userweixin.nickname AS 'zxs',
       channel.nickname AS 'qd',
       shopping.buyerid,
       shopping.nickname AS 'hy',
       shopping.recipient AS 'xm',
       shopping.orderday,
       shopping.abbreviation AS 'sp',
       shopping.tel
FROM saler
LEFT JOIN userweixin ON userweixin.userid = saler.userid
LEFT JOIN channel ON channel.userid = saler.channeluserid,
  (SELECT payorder.buyerid,
          userweixin.nickname,
          `user`.`leaderid`,
          payorder.orderday,
          merchandise.abbreviation,
          recipientaddress.recipient,
          recipientaddress.tel
   FROM payorder,
        `user`,
        merchandise,
        `paysuborder`,
        `userweixin`,
        recipientaddress
   WHERE payorder.isneworder = 1
     AND paysuborder.orderid = payorder.orderid
     AND payorder.buyerid = `user`.`userid`
     AND paysuborder.merchandiseid = merchandise.merchandiseid
     AND payorder.buyerid = userweixin.userid
     AND payorder.addressid = recipientaddress.addressid) AS shopping
WHERE saler.userid IN (22, 1330159)
  AND shopping.`leaderid` = saler.userid
  AND shopping.`orderday` >= '2017-08-12'
  AND shopping.`orderday` <= '2017-08-14'

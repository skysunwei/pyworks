#查询一个规格团长的销量

	起始时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
	截止时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
	规格名称：`paysuborder`.`merchtypecontent` LIKE '%澳大利亚脐橙%'
	
修改下面对应的位置

```
SELECT
	`userweixin`.`nickname`, SUM(`paysuborder`.`quantity`)
FROM `paysuborder`, `payorder`, `saler`, `userweixin`
WHERE
`payorder`.`orderid` = `paysuborder`.`orderid`
AND `payorder`.`recommenduserid` = `saler`.`userid`
AND `userweixin`.`userid` = `saler`.`userid`
AND `saler`.`status` = 1
AND FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
AND FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
AND `paysuborder`.`orderstatus` IN (2, 5)
AND `paysuborder`.`merchtypecontent` LIKE '%澳大利亚脐橙%'
GROUP BY `userweixin`.`nickname`
```


#查询一个商品团长的销量

	起始时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
	截止时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
	商品编号：`payorder`.`merchandiseid` = 168
	
修改下面对应的位置

```
SELECT
	`userweixin`.`nickname`, SUM(`paysuborder`.`quantity`)
FROM `paysuborder`, `payorder`, `saler`, `userweixin`
WHERE
`payorder`.`orderid` = `paysuborder`.`orderid`
AND `payorder`.`recommenduserid` = `saler`.`userid`
AND `userweixin`.`userid` = `saler`.`userid`
AND `saler`.`status` = 1
AND FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
AND FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
AND `paysuborder`.`orderstatus` IN (2, 5)
AND `payorder`.`merchandiseid` = 168
GROUP BY `userweixin`.`nickname`
```

#一个月的零售订单

	起始月份：`orderday` >= '2016-08-01'
    截止时间：`orderday` <= '2016-08-31'

修改下面对应的位置

```
SELECT `userweixin`.`nickname`, `recipientaddress`.`recipient`, `recipientaddress`.`address`,  `merchandise`.`abbreviation`,
`paysuborder`.`merchtypecontent`,
`recipientaddress`.`tel`, `recipientaddress`.`type`
FROM `payorder`, `user` , `userweixin`, `recipientaddress`, `paysuborder`, `merchandise`
WHERE `payorder`.`recommenduserid` = 0
AND `orderday` >= '2016-08-01'
AND `orderday` <= '2016-08-31'
AND `paysuborder`.`orderstatus` IN (2, 5)
AND `payorder`.`buyerid` = `user`.`userid`
AND `payorder`.`orderid` = `paysuborder`.`orderid`
AND `user`.`userid` = `userweixin`.`userid`
AND `payorder`.`merchandiseid` = `merchandise`.`merchandiseid`
AND `user`.`leaderid` =0 
AND `recipientaddress`.`addressid` = `payorder`.`addressid` 
```

#给团长生成文字的版本

    团长ID：`saler`.`userid` = 21

修改下面对应的位置

```
SELECT
 concat(`merchandise`.`abbreviation`,'\n',`groupon`.`slogon`,'\n',
        'http://yhdx.5ixc.com/hao/share.php?grouponid=', `groupon`.`grouponid`, '&mid=', `merchandise`.`merchandiseid`, '\n' )
AS '内容'
FROM `saler`, `groupon`, `merchandise`
WHERE `saler`.`userid` = 21
AND `groupon`.`merchandiseid` = `merchandise`.`merchandiseid`
AND `saler`.`userid` = `groupon`.`salerid`
AND `saler`.`status` = 1
AND `groupon`.`grouponstatus` = 2
ORDER BY `groupon`.`dateline` DESC
```
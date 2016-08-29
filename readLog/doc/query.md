#查询一个规格的销量

	起始时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
	截止时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
	规格名称：`paysuborder`.`merchtypecontent` LIKE '%澳大利亚脐橙%'
	
修改下面对应的位置

```SQL
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


#查询一个商品的销量

	起始时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') >= '2016-08-24 20:00:00'
	截止时间：FROM_UNIXTIME(`payorder`.`dateline`, '%Y-%m-%d %H:%m:%s') <= '2016-08-25 20:00:00'
	商品编号：`payorder`.`merchandiseid` = 168
	
修改下面对应的位置

```SQL
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
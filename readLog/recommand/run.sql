# 线上查询库：https://msn.youhaodongxi.com/index.php   User name: readonly   Password: Readonly2016
# https://cp.youhaodongxi.com/admin/sales/setchannel

-- 购买人和推荐人关系表

SELECT payorder.buyerid,
       saler.pid,
       concat(recipientaddress.tel,',',payorder.orderday, ',', userweixin.nickname) AS info,
       '1' AS '1'
FROM
  payorder
    LEFT JOIN saler ON payorder.buyerid = saler.userid
    LEFT JOIN userweixin ON payorder.buyerid = userweixin.userid
, paysuborder, recipientaddress
WHERE payorder.orderid = paysuborder.orderid
AND payorder.addressid = recipientaddress.addressid
AND paysuborder.merchandiseid = 998
AND saler.pid != 0
AND payorder.orderday >= '2018-03-12'

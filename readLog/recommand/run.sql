# 线上查询库：https://msn.youhaodongxi.com/index.php   User name: readonly   Password: Readonly2016
# https://cp.youhaodongxi.com/admin/sales/setchannel

-- 购买人和推荐人关系表

SELECT payorder.buyerid,
       saler.pid,
       recipientaddress.tel,
       '1' AS '1'
FROM
  payorder
    LEFT JOIN saler ON payorder.buyerid = saler.userid
, paysuborder, recipientaddress
WHERE payorder.orderid = paysuborder.orderid
AND payorder.addressid = recipientaddress.addressid
AND paysuborder.merchandiseid = 998
AND saler.pid != 0

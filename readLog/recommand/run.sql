# 线上查询库：https://msn.youhaodongxi.com/index.php   User name: readonly   Password: Readonly2016
# https://cp.youhaodongxi.com/admin/sales/setchannel

SELECT DISTINCT saler.userid, saler.pid, a.tel ,
(CASE
  WHEN a.buyerid > 0 THEN 1
                                             ELSE 0
                                         END) 'vip'
FROM saler
LEFT JOIN
(
	SELECT
    	payorder.buyerid,
    	recipientaddress.tel
    FROM payorder, paysuborder, recipientaddress
    WHERE
    	payorder.addressid = recipientaddress.addressid
    	AND payorder.orderid = paysuborder.orderid
    	AND paysuborder.merchandiseid = 998
) a ON a.buyerid=saler.userid
WHERE saler.status=1
  AND saler.pid != 0
  AND saler.userid NOT IN (27997,
                           38617,
                           67413,
                           145007,
                           48416,
                           89159,
                           237)
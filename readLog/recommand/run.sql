# 线上查询库：https://msn.youhaodongxi.com/index.php   User name: readonly   Password: Readonly2016

SELECT saler.userid, saler.pid,
	'' AS orders,
(CASE
     WHEN vipuser_rebate.user_id > 0 THEN 1
     ELSE 0
 END) 'vip'
FROM saler
	LEFT JOIN vipuser_rebate ON saler.userid = vipuser_rebate.user_id
WHERE saler.status=1
	AND saler.pid != 0
    AND saler.userid NOT IN (27997,38617,67413,145007,48416,89159,237,81560)
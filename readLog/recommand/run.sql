# 线上查询库：https://msn.youhaodongxi.com/index.php   User name: readonly   Password: Readonly2016
# https://cp.youhaodongxi.com/admin/sales/setchannel

-- 购买人和推荐人关系表

SELECT a.user_id,
       a.recommend_user_id,
       b.tel,
       '1' AS '1'
FROM
  (SELECT vipuser_rebate.order_id,
          vipuser_rebate.user_id,
          vipuser_rebate.recommend_user_id
   FROM vipuser_rebate
   WHERE vipuser_rebate.order_status=2) a
LEFT JOIN
  (SELECT payorder.orderid,
          recipientaddress.userid,
          recipientaddress.tel
   FROM payorder,
        recipientaddress
   WHERE payorder.addressid=recipientaddress.addressid) b ON a.order_id=b.orderid
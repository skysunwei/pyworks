
-- 支付成功状态信息：
-- 交易流水=实际支付金额
-- 应结金额=交易流水*0.25-团队收益-甄选收益

-- 退款状态信息：
-- 撤单金额=实际支付金额
-- 应结金额=团队收益 + 甄选收益 - 撤单金额*0.25

SELECT payhistory.transactionid '微信订单号',
       payhistory.orderid,
       FROM_unixtime(payhistory.paydateline) '支付时间',
       concat(a.nickname,'(',a.userid,')') '用户昵称（id）',
       concat(b.nickname,'(',b.userid,')') '甄选师昵称（id）',
       round(payhistory.money/100,2) '交易流水',
       ROUND(SUM(rebate.amount * rebate.leaderbrokerage * rebate.leaderrankratio *rebate.taxingpoint/100)/10000,2) AS '团队收益',
       ROUND(SUM(rebate.amount * rebate.rankratio * rebate.taxingpoint/100)/100,2) AS '甄选收益',
       ROUND(round(payhistory.money/100,2)*0.25/*0.25是提成比例可修改*/- ROUND(SUM(rebate.amount * rebate.leaderbrokerage * rebate.leaderrankratio *rebate.taxingpoint/100)/10000,2)- ROUND(SUM(rebate.amount * rebate.rankratio * rebate.taxingpoint/100)/100,2),2) '应结金额'
FROM payhistory,
     paysuborder
LEFT JOIN userweixin AS a ON paysuborder.userid=a.userid
LEFT JOIN userweixin AS b ON paysuborder.ordersalerid=b.userid
LEFT JOIN rebate ON paysuborder.suborderid=rebate.suborderid
WHERE paysuborder.orderid=payhistory.orderid
  AND payhistory.paystatus=2
  AND FROM_unixtime(payhistory.paydateline,'%Y-%m-%d')='2018-03-07'
  AND paysuborder.ordersalerid IN (1167969,1185784)
GROUP BY paysuborder.orderid

UNION ALL

SELECT payhistory.transactionid '微信订单号',
       paysuborder.orderid,
       FROM_unixtime(paysuborder.revokedateline) '退款时间',
       concat(a.nickname,'(',a.userid,')') '用户昵称（id）',
       concat(b.nickname,'(',b.userid,')') '甄选师昵称（id）',
       ROUND(SUM(IF((paysuborder.quantity*(paysuborder.price-paysuborder.promotionfee)+ paysuborder.expressfee-paysuborder.couponmoney-paysuborder.gold-paysuborder.giftcardmoney)>0, (paysuborder.quantity*(paysuborder.price-paysuborder.promotionfee) +paysuborder.expressfee-paysuborder.couponmoney-paysuborder.gold-paysuborder.giftcardmoney),0)) /100,2) '撤单金额',
       '' AS '',
       '' AS '',
       ROUND(SUM(rebate.amount * rebate.leaderbrokerage * rebate.leaderrankratio *rebate.taxingpoint/100)/10000,2) + ROUND(SUM(rebate.amount * rebate.rankratio * rebate.taxingpoint/100)/100,2),2) - ROUND(ROUND(SUM(IF((paysuborder.quantity*(paysuborder.price-paysuborder.promotionfee)+ paysuborder.expressfee-paysuborder.couponmoney-paysuborder.gold-paysuborder.giftcardmoney)>0, (paysuborder.quantity*(paysuborder.price-paysuborder.promotionfee) +paysuborder.expressfee-paysuborder.couponmoney-paysuborder.gold-paysuborder.giftcardmoney),0)) /100,2) *0.25 '应结金额'
FROM payhistory,
     paysuborder
LEFT JOIN userweixin AS a ON paysuborder.userid=a.userid
LEFT JOIN userweixin AS b ON paysuborder.ordersalerid=b.userid
LEFT JOIN rebate ON paysuborder.suborderid=rebate.suborderid
WHERE paysuborder.orderid=payhistory.orderid
  AND paysuborder.orderstatus=4
  AND FROM_unixtime(paysuborder.revokedateline,'%Y-%m-%d')='2018-03-07'
  AND paysuborder.ordersalerid IN (1167969,1185784)
GROUP BY paysuborder.orderid



# 卖399商品返利线下结算

SELECT yh.userid '购买者',
       yh.nickname,
       FROM_UNIXTIME(vipuser_rebate.`confirm_time`) '推荐时间',
       zxs.userid '推荐人',
       zxs.nickname,
       vipuser_rebate.amount/100 '推荐人收益金额',
       30 '结算金额'
FROM vipuser_rebate
LEFT JOIN userweixin AS zxs ON vipuser_rebate.`recommend_user_id` = zxs.userid
LEFT JOIN userweixin AS yh ON vipuser_rebate.`user_id` = yh.userid
WHERE vipuser_rebate.`recommend_user_id` IN (1167969,1185784)
  AND FROM_UNIXTIME(vipuser_rebate.`confirm_time`, '%Y-%m-%d') = '2018-03-07'

SELECT merchandise.merchandiseid,
       merchandise.abbreviation,
       category.title,
       merchtype.content,
       grouponrulemerchtype.grouponprice / 100 AS money,
       merchandise.saleitem
FROM merchandise
		LEFT JOIN category ON merchandise.tagid = category.categoryid,
     merchtype,
     grouponrule,
     grouponrulemerchtype
WHERE merchandise.merchandiseid = merchtype.merchandiseid
  AND grouponrulemerchtype.merchtypeid = merchtype.merchtypeid
  AND grouponrule.grouponruleid = grouponrulemerchtype.grouponruleid
  AND grouponrulemerchtype.merchtypeid = merchtype.merchtypeid
  AND grouponrule.merchandiseid = merchandise.merchandiseid
  AND merchandise.onsale = 1
  AND merchtype.valid = 1
  AND merchandise.rank > 0
  AND grouponrule.grouponruletype = 2
  AND grouponrule.valid = 1
  AND grouponrulemerchtype.valid = 1
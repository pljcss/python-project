--
SELECT * FROM table_a;

--<>--
SELECT * FROM table_a;


SELECT * FROM table_a;


SELECT * FROM table_a;


select t.*,row_number() over(order by annual_money desc,max_time asc) as rn
from (select cf.id,
va.user_id,
max(va.create_time) as max_time,
sum(va.amount) as amount,
sum(
    case when fp.scope = 28 then round(va.amount,2) * csi.locking_expect / if(csi.locking_expect_unit = 0, 12, 365)
    else round(va.amount,2) * fp.expect / if(fp.expect_unit = 0, 12, 365)
    end) annual_money
from rt.finance_plan fp
join rt.mkt_invest_ranking_config cf
on cf.stat_start_time <='2019-05-14'
and cf.stat_end_time>='2019-05-14'
join rt.vip_account_mark_ranking_01 va
on va.fp_id=fp.id
and va.platform = 1
and va.is_cash=0
and to_date(va.create_time)='2019-05-14'
left join rt.invt_custom_trans_info csi
on csi.trans_id = va.trans_id
where find_in_set(cast(fp.scope as string),cf.stat_product_scope)>=1
group by cf.id,va.user_id) t;
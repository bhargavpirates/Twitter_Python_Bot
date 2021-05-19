import pandas as pd
from openpyxl.workbook import Workbook



lst=[['select count(*) from  bcbsmi_ts_curated_temp.hsc_input;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_hlth_srvc_cd_type_pairs_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_srvc_int_1_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_srvc_int_15_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_srvc_int_2_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_srvc_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_srvc_rndrg_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_plos_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_proc_mdfr_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_txnmy_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_line_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_clm_temp;', 270452], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grn_rsr_temp;', 247637], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_grn_rsr_temp;', 6507], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_line_filter_temp;', 247637], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_clm_grp_brkr_temp;', 4977], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_line_collect_temp;', 90624], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_key_map_temp;', 4978], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_claim_level_one_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_key_map_exp_temp;', 6507], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_key_2_clm_temp;', 6507], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_claim_level_two_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_claim_level_three_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_date_joiner_temp;', 6507], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_claim_level_join_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_out_temp;', 23227], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_line_level_one_temp;', 90624], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_line_level_two_temp;', 247637], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_grouper_line_level_join_temp;', 251073], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_out_temp;', 251073], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_visit_counter_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_settlement_row_counter_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_settlement_out_temp;', 251073], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_visit_union_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_diag_icd_pairs_temp;', 6105], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_hlth_srvc_type_pairs_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_set_admit_dt_temp;', 95602], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_select_orgntg_clm_temp;', 95602], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_int_1_temp;', 6105], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_int_2_temp;', 6105], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_int_3_temp;', 6105], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_rr_1_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_rr_2_temp;', 4655], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_set_dschrg_dt_temp;', 95602], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_select_dschrg_temp;', 95602], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_line_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_case_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_mnthly_casing_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_mnthly_casing_date_temp;', 0], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_mnthly_casing_out_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_cd_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_anlytc_clm_line_proc_temp;', 226554], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_anlytc_clm_line_srvc_temp;', 90624], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_admit_visit_cnt_temp;', 95602], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_out_temp;', 274300], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_anlytc_proc_cnt_temp;', 226554], ['select count(*) from  bcbsmi_ts_curated_temp.hsc_anlytc_srvc_cnt_temp;', 90624], ['select count(*) from  bcbsmi_ts_curated_wh.hsc_output;', 274300]]

df=pd.DataFrame(lst,columns=['Query',"count"])

print(df.shape)
df.to_excel('{}.xlsx'.format("hsc_count"))
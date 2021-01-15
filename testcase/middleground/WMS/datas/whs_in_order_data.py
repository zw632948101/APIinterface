from testcase.middleground.WMS.common.Mysql import mp_label
class whs_in_order:

    admin_whs_receipt_detail = [{"title":"待入库订单-详情","data":{"code_":"RK202101050011"},"expect":"OK"},
                                {"title":"已入库完成订单-详情","data":{"code_":"RK202101060102"},"expect":"OK"},
                                {"title":"入库单详情-单据为空","data":{"code_":None},"expect":"ERROR"},
                                {"title":"关联订单-详情","data":{"code_":"RT202101050050"},"expect":"OK"}]

    admin_whs_receipt_page_list=[{"title":"状态=1","data":{"pn":"","ps":"","code":"","status":"1","type":"","warehouseCode":"","creatorId":""},"expect":"OK"},
                                 {"title":"状态=0","data":{"pn":"","ps":"","code":"","status":"0","type":"","warehouseCode":"","creatorId":""},"expect":"OK"},
                                 {"title":"状态=2","data":{"pn":"","ps":"","code":"","status":"2","type":"","warehouseCode":"","creatorId":""},"expect":"OK"},
                                 {"title":"默认","data":{"pn":"","ps":"","code":"","status":"","type":"","warehouseCode":"","creatorId":""},"expect":"OK"},
                                 {"title":"单据类型","data":{"pn":"","ps":"","code":"","status":"","type":"RK05","warehouseCode":"","creatorId":""},"expect":"OK"}]

    admin_whs_receipt_tracing_list = [{"title":"商品明细列表","data":{"pn":"","ps":"","orderCode":"RT202101050014","productCode":"T0103020009","tracingCode":""},"expect":"OK"},
                                      {"title":"必填参数不填","data":{"pn":"","ps":"","orderCode":"","productCode":"","tracingCode":""},"expect":"OK"},
                                      {"title":"参数字段为空","data":{"pn":None,"ps":None,"orderCode":None,"productCode":None,"tracingCode":None},"expect":"ERROR"}]

    admin_receipt_cancel = [{"title":"取消入库单-待确认订单","data":{"code":mp_label().git_whs_receipt(0)[0]['code']},"expect":"OK"},
                            {"title":"取消入库单-已确认订单","data":{"code":mp_label().git_whs_receipt(1)[0]['code']},"expect":"ERROR"},
                            {"title":"取消入库单-单号为空","data":{"code":None},"expect":"ERROR"},
                            {"title":"取消入库单-重复取消","data":{"code":mp_label().git_whs_receipt(2)[0]['code']},"expect":"ERROR"}]
from django.db import migrations

xarray_in_pyplan_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 0,
            "width": 4,
            "height": 12,
            "itemId": "8a8a4da8-4e2e-44c2-b7d6-9d1f3e5cd599",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "diagramviewer",
            "itemProperties": {
                "diagramOptions": {
                    "id": "06ffa1fc-35e7-41f3-9692-4ded605f5390",
                    "posx": 0,
                    "posy": 0,
                    "zoom": 1,
                    "autoCenter": False,
                    "breadCrumb": True,
                    "contextMenu": False,
                    "currentModule": "xarray_in_pyplan",
                    "showBreadcrumb": True,
                    "listenMouseDown": True
                }
            }
        },
        {
            "x": 4,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 1,
            "width": 8,
            "height": 2,
            "itemId": "d5f657d3-a8c9-4313-b6c4-b1fc3d63956c",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                        "htmlcontent": "<span class=\"\" style=\"font-size: 2vmin;\"><font color=\"#006fdf\">Standard Xarray broadcasting and math operations using Pyplan indexes.&nbsp;</font></span><div><span class=\"\" style=\"font-size: 2vmin;\"><font color=\"#006fdf\">Click on indexes \"Product\" &amp; \"Region\" to see how filters work on interfaces</font></span></div>",
                        "generalBackgroundColor": "#eeeeee"
            }
        },
        {
            "x": 4,
            "y": 2,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 2,
            "height": 1,
            "itemId": "beac876b-3019-4dd4-aeec-ec1bfe01b75b",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                        "htmlcontent": "<font color=\"#006fdf\"><span style=\"font-size: 18.56px;\">Filters</span></font>",
                        "generalBackgroundColor": "#eeeeee"
            }
        },
        {
            "x": 6,
            "y": 2,
            "dims": [],
            "rows": [
                {
                    "name": "Product",
                    "field": "product.fruits_prices",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Banana",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 3,
            "width": 2,
            "height": 3,
            "itemId": "708fd53a-ffb1-4d69-a907-ffba8503edd8",
            "nodeId": "fruits_prices",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Fruits Prices",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 8,
            "y": 2,
            "dims": [],
            "rows": [
                {
                    "name": "Product",
                    "field": "product.fruits_quantities",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Banana",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 4,
            "width": 2,
            "height": 3,
            "itemId": "5b3df4d3-723d-4dae-8127-f9fb8f11c4be",
            "nodeId": "fruits_quantities",
            "columns": [
                {
                    "name": "Region",
                    "field": "region.fruits_quantities",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "North",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "South",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "West",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Fruits Quantities",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 10,
            "y": 2,
            "dims": [],
            "rows": [
                {
                    "name": "Product",
                    "field": "product.revenue",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Banana",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 5,
            "width": 2,
            "height": 3,
            "itemId": "2800edb6-25f5-4f2e-ab82-6a30981cc85a",
            "nodeId": "revenue",
            "columns": [
                {
                    "name": "Region",
                    "field": "region.revenue",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "North",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "South",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "West",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Revenue",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 2,
            "height": 1,
            "itemId": "b7c46667-c85c-4714-b057-2b18d0cbe6bf",
            "nodeId": "product",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "index": {
                            "ui": "default",
                            "dynamic": False,
                            "related": False,
                            "orientation": "h",
                            "singleSelect": False,
                            "currentSelectedValues": [
                                "Orange",
                                "Apple",
                                "Banana"
                            ]
                        },
                "title": {
                            "text": "Product",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "nodeId": "product",
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 4,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 2,
            "height": 1,
            "itemId": "d408c672-8d8b-4e55-a739-5b864796cfb6",
            "nodeId": "region",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "index": {
                            "ui": "default",
                            "dynamic": False,
                            "related": False,
                            "orientation": "h",
                            "singleSelect": False,
                            "currentSelectedValues": [
                                "North",
                                "South",
                                "West"
                            ]
                        },
                "title": {
                            "text": "Region",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "nodeId": "region",
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 8,
            "width": 8,
            "height": 2,
            "itemId": "dc639535-a455-4d4f-82ef-82dc625dda36",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                        "htmlcontent": "          \n        <font color=\"#006fdf\"><span style=\"caret-color: rgb(0, 111, 223); font-size: 20.34000015258789px;\">Pyplan solving dimensions intersection&nbsp;and alignment with indexes</span></font><div><span style=\"color: rgb(0, 111, 223); font-size: 18.56px;\">Click on indexes \"New Products\" &amp; \"Region\" to see how filters work on interfaces</span><font color=\"#006fdf\"><span style=\"caret-color: rgb(0, 111, 223); font-size: 20.34000015258789px;\"><br></span></font></div>",
                        "generalBackgroundColor": "#eeeeee"
            }
        },
        {
            "x": 4,
            "y": 7,
            "dims": [],
            "rows": [],
            "index": 9,
            "width": 2,
            "height": 1,
            "itemId": "f0b26a7b-57bc-4791-b61d-8aa7e797fb56",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                        "htmlcontent": "            \n        <font color=\"#006fdf\"><span style=\"font-size: 18.56px;\">Other Filters</span></font>",
                        "generalBackgroundColor": "#eeeeee"
            }
        },
        {
            "x": 6,
            "y": 7,
            "dims": [],
            "rows": [
                {
                    "name": "New Products",
                    "field": "new_products.fruits_prices_new_list",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Grapes",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 10,
            "width": 2,
            "height": 3,
            "itemId": "8f11ca49-741b-47dc-a914-c0e7fbf50768",
            "nodeId": "fruits_prices_new_list",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Fruits Prices New List",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 8,
            "y": 7,
            "dims": [],
            "rows": [
                {
                    "name": "New Products",
                    "field": "new_products.fruits_quantities_new_list",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Grapes",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 11,
            "width": 2,
            "height": 3,
            "itemId": "4e9e90e7-e16b-48f5-a172-a10c10994bed",
            "nodeId": "fruits_quantities_new_list",
            "columns": [
                {
                    "name": "Region",
                    "field": "region.fruits_quantities_new_list",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "North",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "South",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "West",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Fruits Quantities New List",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 10,
            "y": 7,
            "dims": [],
            "rows": [
                {
                    "name": "New Products",
                    "field": "new_products.revenue_new_price_order",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "Apple",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Orange",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "Grapes",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 12,
            "width": 2,
            "height": 3,
            "itemId": "7d8ef5bb-d753-49c6-9dc9-f33bc88d83b7",
            "nodeId": "revenue_new_price_order",
            "columns": [
                {
                    "name": "Region",
                    "field": "region.revenue_new_price_order",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": "",
                            "value": "North",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "South",
                            "geoDef": None,
                            "selected": True
                        },
                        {
                            "type": "",
                            "value": "West",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "table": {
                            "styles": [
                                {
                                    "pos": 0,
                                    "index": "_alltable_",
                                    "style": {
                                        "pagination": 100
                                    },
                                    "value": -1
                                }
                            ]
                        },
                "title": {
                            "text": "Revenue new price order",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 8,
            "dims": [],
            "rows": [],
            "index": 13,
            "width": 2,
            "height": 1,
            "itemId": "c6627b5e-8695-4ae3-984f-113833e8bcef",
            "nodeId": "new_products",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "index": {
                            "ui": "default",
                            "dynamic": False,
                            "related": False,
                            "orientation": "h",
                            "singleSelect": False,
                            "currentSelectedValues": [
                                "Apple",
                                "Orange",
                                "Grapes"
                            ]
                        },
                "title": {
                            "text": "New Products",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "nodeId": "new_products",
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 9,
            "dims": [],
            "rows": [],
            "index": 14,
            "width": 2,
            "height": 1,
            "itemId": "65998326-c990-464e-af3c-81f562a5356e",
            "nodeId": "region",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                        "axes": {
                            "xAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "yAxis": {
                                "max": None,
                                "min": None,
                                "title": {
                                    "text": ""
                                },
                                "labels": {
                                    "align": None,
                                    "enabled": "True",
                                    "rotation": None
                                },
                                "isSumList": [],
                                "showTitle": True
                            },
                            "enabled": True
                        },
                "unit": "",
                        "zoom": True,
                        "index": {
                            "ui": "default",
                            "dynamic": False,
                            "related": False,
                            "orientation": "h",
                            "singleSelect": False,
                            "currentSelectedValues": [
                                "North",
                                "South",
                                "West"
                            ]
                        },
                "title": {
                            "text": "Region",
                            "align": "center",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "margin": "",
                            "enabled": True,
                            "isCustom": False,
                            "verticalAlign": "top"
                        },
                "detail": True,
                "legend": {
                            "y": 0,
                            "align": "right",
                            "title": {
                                "text": ""
                            },
                            "layout": "vertical",
                            "enabled": True,
                            "borderWidth": 0,
                            "verticalAlign": "middle"
                        },
                "nodeId": "region",
                "tooltip": {
                            "valueSuffix": None,
                            "valueDecimals": 2
                        },
                "subtitle": {
                            "text": "",
                            "style": {
                                "text": "#000000",
                                "fontWeight": "normal"
                            },
                            "enabled": True,
                            "verticalAlign": "top"
                        },
                "drilldown": True,
                "timeChart": {
                            "active": False,
                            "possible": False
                        },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 10,
            "dims": [],
            "rows": [],
            "index": 15,
            "width": 8,
            "height": 2,
            "itemId": "9f2a5270-7ffd-4893-aab4-c8b2102bbc24",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                "htmlcontent": "<p class=\"MsoNormal\" style=\"margin-bottom:0cm;margin-bottom:.0001pt;line-height:\nnormal\"><span lang=\"EN-GB\" style=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;\nmso-fareast-font-family:&quot;Times New Roman&quot;;color:#BF2F00;mso-ansi-language:EN-GB;\nmso-fareast-language:ES-AR\">In the last case, the dimension\n\"Products\" has been changed for the&nbsp;dimension \"New\nProducts\". Fruits quantities New List has been&nbsp;defined using \u201cchange\nindex\u201d in order to make it match with Fruits prices new list dimensions.</span><span lang=\"EN-GB\" style=\"font-size: 10pt; font-family: Arial, sans-serif;\"><o:p></o:p></span></p>\n\n<p class=\"MsoNormal\" style=\"margin-bottom:0cm;margin-bottom:.0001pt;line-height:\nnormal\"><span lang=\"EN-GB\" style=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;\nmso-fareast-font-family:&quot;Times New Roman&quot;;color:#BF2F00;mso-ansi-language:EN-GB;\nmso-fareast-language:ES-AR\">Pyplan keeps intersection between the two indexes\nadding 0 to elements which do not exist in the resultant index in this\ncase&nbsp;[\"Grapes\"].</span><span lang=\"EN-GB\" style=\"font-size: 10pt; font-family: Arial, sans-serif;\"><o:p></o:p></span></p>",
                "generalBackgroundColor": "#eeeeee"
            }
        }
    ]
}

pyplan_qs_tutorials_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 0,
            "width": 1,
            "height": 6,
            "itemId": "3a9adaff-9914-4b4c-a5a0-b6edf5d46701",
            "nodeId": "year",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Year",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "year",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 1,
            "width": 3,
            "height": 5,
            "itemId": "63fe07f9-9b16-4adc-8fe2-834e5882aad8",
            "nodeId": "pd_print",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Wins and Double Faults Statistics",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None
            }
        },
        {
            "x": 4,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Surface",
                    "field": "surface.pd_groupby_1",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 2,
            "width": 4,
            "height": 5,
            "itemId": "03acd820-b71e-484b-b632-2f9b8e325095",
            "nodeId": "pd_groupby_1",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_groupby_1",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": "1",
                        "min": "0",
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": True
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "% of Wins by Year and Surface",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "3",
                "emptyTotal": False,
                "indexEvents": {
                    "surface.pd_groupby_1": True
                },
                "numberFormat": "2,%,4,0,0,0,4,0,$,5,,0"
            }
        },
        {
            "x": 8,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 3,
            "width": 4,
            "height": 5,
            "itemId": "1f6dd0e7-c79d-4f4e-a2cb-169975f1ca0e",
            "nodeId": "pd_groupby_2",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_groupby_2",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "% of Double Faults by Year",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": True
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": False,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "43",
                "numberFormat": "2,%,4,1,0,0,4,0,$,5,,0"
            }
        },
        {
            "x": 1,
            "y": 5,
            "dims": [
                {
                    "name": "Year",
                    "field": "year.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Tournament Country",
                    "field": "tournament_country.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Surface",
                    "field": "surface.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 4,
            "width": 4,
            "height": 8,
            "itemId": "4d7ba842-6102-4748-94f5-f005dfdb32bc",
            "nodeId": "pd_set_index",
            "columns": [
                {
                    "name": "Tournament Continent",
                    "field": "tournament_continent.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "piechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "# of Wins by Year, Surface and Tournament's Location",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": False,
                    "enabled": True
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": False,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "3",
                "indexEvents": {
                    "surface.pd_set_index": True
                }
            }
        },
        {
            "x": 5,
            "y": 5,
            "dims": [
                {
                    "name": "Tournament Continent",
                    "field": "tournament_continent.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Tournament Country",
                    "field": "tournament_country.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Surface",
                    "field": "surface.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 5,
            "width": 3,
            "height": 8,
            "itemId": "84e2f6b6-6953-4e20-b93c-5232cc63d5a2",
            "nodeId": "pd_set_index",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "columnchartstacked",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "# of Wins by Year, Surface and Tournament's Location",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": True,
                    "enabled": True
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "grouping": False,
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "3"
            }
        },
        {
            "x": 8,
            "y": 5,
            "dims": [
                {
                    "name": "Surface",
                    "field": "surface.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Tournament Country",
                    "field": "tournament_country.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Tournament Continent",
                    "field": "tournament_continent.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 6,
            "width": 4,
            "height": 8,
            "itemId": "26579fb8-0903-47fe-8326-5afbfda3bb2c",
            "nodeId": "pd_set_index",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "barchartstacked",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "# of Wins by Year, Surface and Tournament's Location",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": True,
                    "enabled": True
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "grouping": False,
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "21",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 1,
            "height": 3,
            "itemId": "ead6c262-97e0-4199-bb7b-2d45da5a748d",
            "nodeId": "surface",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False,
                    "currentSelectedValues": []
                },
                "title": {
                    "text": "Surface",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "surface",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 0,
            "y": 9,
            "dims": [],
            "rows": [],
            "index": 8,
            "width": 1,
            "height": 4,
            "itemId": "90b87f64-1abf-48d6-843b-4ecd0c8a1c19",
            "nodeId": "tournament_continent",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Tournament Continent",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "tournament_continent",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 1,
            "y": 13,
            "dims": [],
            "rows": [
                {
                    "name": "Surface",
                    "field": "surface.pd_groupby_1",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 9,
            "width": 5,
            "height": 8,
            "itemId": "163cb351-2478-4e4c-8c67-767ebdba8bc1",
            "nodeId": "pd_groupby_1",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_groupby_1",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "heatMap": "by_column",
                                "pagination": 100,
                                "heatMapColor": "#ffffff,#00ff00",
                                "numberFormat": "2,%,4,1,0,0,4,0,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "% of Wins by Year and Surface",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "numberFormat": "2,%,4,1,0,0,4,0,$,5,,0"
            }
        },
        {
            "x": 6,
            "y": 13,
            "dims": [
                {
                    "name": "Tournament Continent",
                    "field": "tournament_continent.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Tournament Country",
                    "field": "tournament_country.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Surface",
                    "field": "surface.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 10,
            "width": 6,
            "height": 8,
            "itemId": "4379a87e-927f-451a-b93f-a9e5b5d84165",
            "nodeId": "pd_set_index",
            "columns": [
                {
                    "name": "Year",
                    "field": "year.pd_set_index",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "surface.pd_set_index",
                            "style": {
                                "fontBold": True
                            },
                            "value": "Total"
                        },
                        {
                            "pos": 1,
                            "index": "_alltable_",
                            "style": {
                                "heatMap": "by_column",
                                "pagination": 100,
                                "heatMapColor": "#ffffff,#00ff00",
                                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "# of Wins by Year, Surface and Tournament's Location",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "bottomTotal": True,
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        }
    ]
}

creating_my_first_model_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Market Scenarios",
                    "field": "market_scenarios_.market_growth",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 9,
            "height": 3,
            "itemId": "84dff6e1-aeb5-4b00-8318-a772f59e9a5d",
            "nodeId": "market_growth",
            "columns": [
                {
                    "name": "Time",
                    "field": "time.market_growth",
                    "isGeo": False,
                    "isTime": True,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "nodetable",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Market Growth",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": True
                },
                "validation": {},
                "cubeOptions": {
                    "cols": [
                        "time"
                    ],
                    "rows": [
                        "market_scenarios_"
                    ],
                    "nodeId": "market_growth",
                    "editMode": False,
                    "aggregator": "genericSum",
                    "rendererName": "Pivot Table",
                    "selectedMeasures": [
                        "datavalue"
                    ]
                },
                "showRowTotal": False,
                "showColumnTotal": False
            }
        },
        {
            "x": 9,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Records",
                    "field": "records.discounts_input",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 3,
            "height": 3,
            "itemId": "55eac2dd-04de-4155-b2b3-40bbf57aaf36",
            "nodeId": "discounts_input",
            "columns": [
                {
                    "name": "Columns",
                    "field": "columns.discounts_input",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        },
                        {
                            "pos": 1,
                            "index": "columns.discounts_input",
                            "style": {
                                "cellType": "choice",
                                "choiceProperties": {
                                    "index": "region",
                                    "includeAll": False
                                }
                            },
                            "value": "Region"
                        },
                        {
                            "pos": 2,
                            "index": "columns.discounts_input",
                            "style": {
                                "cellType": "choice",
                                "choiceProperties": {
                                    "index": "time",
                                    "includeAll": False
                                }
                            },
                            "value": "Time"
                        },
                        {
                            "pos": 3,
                            "index": "columns.discounts_input",
                            "style": {
                                "cellType": "choice",
                                "choiceProperties": {
                                    "index": "discounts",
                                    "includeAll": False
                                }
                            },
                            "value": "Discount (%)"
                        }
                    ]
                },
                "title": {
                    "text": "Discounts Input",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "validation": {},
                "cubeOptions": {
                    "cols": [
                        "columns"
                    ],
                    "rows": [
                        "records"
                    ],
                    "nodeId": "discounts_input",
                    "filters": {},
                    "editMode": False,
                    "aggregator": "genericSum",
                    "rendererName": "Pivot Table",
                    "positionFilters": {},
                    "selectedMeasures": [
                        "datavalue"
                    ]
                },
                "showRowTotal": False,
                "showColumnTotal": False
            }
        },
        {
            "x": 0,
            "y": 6,
            "index": 2,
            "width": 3,
            "height": 2,
            "itemId": "42bde222-efa7-46a9-979c-0a9192053bbf",
            "nodeId": "",
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                "htmlcontent": "<b><span class=\"\" style=\"font-size: 3vmin;\">Controls</span></b>",
                "generalBackgroundColor": "#cfe2f3"
            }
        },
        {
            "x": 3,
            "y": 3,
            "index": 3,
            "width": 9,
            "height": 2,
            "itemId": "a09692c0-84f4-4f20-bb96-85821d2b4162",
            "nodeId": "",
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                "htmlcontent": "<b><span class=\"\" style=\"font-size: 3vmin;\">Outputs</span></b>",
                "generalBackgroundColor": "#7cb5ec"
            }
        },
        {
            "x": 0,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 3,
            "height": 1,
            "itemId": "24d562ef-49e6-421c-8dd4-f4c37aaf52cb",
            "nodeId": "market_scenario_selector_choice",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Scenario",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None,
                "multiselect": "0"
            }
        },
        {
            "x": 3,
            "y": 5,
            "dims": [
                {
                    "name": "Region",
                    "field": "region.projected_units_sold",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Item Type",
                    "field": "item_type.projected_units_sold",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Sales Channel",
                    "field": "Sales Channel.projected_units_sold",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 5,
            "width": 9,
            "height": 5,
            "itemId": "95b0ba28-471e-44b2-9481-de8b073f81f6",
            "nodeId": "projected_units_sold",
            "columns": [
                {
                    "name": "Time",
                    "field": "time.projected_units_sold",
                    "isGeo": False,
                    "isTime": True,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "columnchartstacked",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "unit": "( units)",
                "zoom": True,
                "title": {
                    "text": "Projected Units Sold",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": True,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": " units",
                    "valueDecimals": 2
                },
                "grouping": False,
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": True
                }
            }
        },
        {
            "x": 0,
            "y": 8,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 3,
            "height": 6,
            "itemId": "04e8709d-4eae-4e11-abaa-745bfec61dbf",
            "nodeId": "item_type",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Item Type",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "item_type",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#cfe2f3"
            }
        },
        {
            "x": 3,
            "y": 10,
            "dims": [
                {
                    "name": "Report",
                    "field": "Report.output_dashboard",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Region",
                    "field": "region.output_dashboard",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Item Type",
                    "field": "item_type.output_dashboard",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Sales Channel",
                    "field": "Sales Channel.output_dashboard",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": "",
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 7,
            "width": 9,
            "height": 4,
            "itemId": "07cf3e44-be72-42d4-bfbe-9b8b29d819bc",
            "nodeId": "output_dashboard",
            "columns": [
                {
                    "name": "Time",
                    "field": "time.output_dashboard",
                    "isGeo": False,
                    "isTime": True,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "unit": "( millions $)",
                "zoom": True,
                "title": {
                    "text": "Output Dashboard",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": " millions $",
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": True
                }
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 8,
            "width": 3,
            "height": 2,
            "itemId": "8d30a3eb-e7e7-4268-816b-3a03f9efd9fd",
            "nodeId": "sales_channel",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Chanel",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channel",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#cfe2f3"
            }
        },
        {
            "x": 0,
            "y": 14,
            "dims": [],
            "rows": [],
            "index": 9,
            "width": 12,
            "height": 1,
            "itemId": "056875b4-1229-4bef-8f70-9b1d192ed10c",
            "nodeId": "time",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "range"
                },
                "title": {
                    "text": "Time",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "time",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

iris_sample_model_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "index": 0,
            "width": 3,
            "height": 2,
            "itemId": "54f0c76b-1ceb-4d38-ad2c-189c66cbc3b0",
            "nodeId": "",
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                "htmlcontent": "<b><span class=\"\" style=\"font-size: 4vmin;\">Iris Sample Interface</span></b>",
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 3,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 1,
            "width": 9,
            "height": 6,
            "itemId": "182ffa63-76ec-49b2-b815-25a73e2a0d2d",
            "nodeId": "fullchart",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "full chart ",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        },
        {
            "x": 0,
            "y": 2,
            "dims": [
                {
                    "name": "Items to tests",
                    "field": "items_to_tests_copy.input_data_to_predict",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Iris properties",
                    "field": "iris_properties.input_data_to_predict",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 2,
            "width": 3,
            "height": 11,
            "itemId": "7db317a4-2964-4c9a-9529-89208c1f4f21",
            "nodeId": "input_data_to_predict",
            "columns": [],
            "itemType": "nodetable",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Input data to predict",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "validation": {},
                "cubeOptions": {
                    "cols": [
                        "items_to_tests"
                    ],
                    "rows": [
                        "iris_properties"
                    ],
                    "nodeId": "input_data_to_predict",
                    "filters": {},
                    "editMode": True,
                    "aggregator": "listUnique",
                    "rendererName": "Input Table",
                    "positionFilters": {
                        "items_to_tests": {
                            "values": ""
                        }
                    },
                    "selectedMeasures": [
                        "datavalue"
                    ]
                },
                "showRowTotal": False,
                "showColumnTotal": False,
                "generalBackgroundColor": "#fff2cc"
            }
        },
        {
            "x": 3,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 3,
            "width": 9,
            "height": 7,
            "itemId": "af7a7109-3ce8-477c-b2a1-5a85995a37a3",
            "nodeId": "chart3d",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "chart3d",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

variable_exploration_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 7,
            "height": 6,
            "itemId": "d9e9d646-d000-4660-836e-11a9462b5ab4",
            "nodeId": "cdm_hist_sales_sales_chn_prod_family",
            "columns": [
                {
                    "name": "Historic Time",
                    "field": "historic_time.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "columnchartstacked",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Historical Sales by Sales Channel and Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": True
                },
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "grouping": False,
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "1",
                "cubeOptions": {
                    "editMode": False
                },
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 8,
            "y": 0,
            "dims": [
                {
                    "name": "Historic Time",
                    "field": "historic_time.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_hist_sales_sales_chn_prod_family",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 2,
            "width": 4,
            "height": 6,
            "itemId": "df26be3a-7b54-44d7-8e24-648d70ddf80f",
            "nodeId": "cdm_hist_sales_sales_chn_prod_family",
            "columns": [],
            "itemType": "piechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Historical Sales by Sales Channel and Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": True
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "1",
                "cubeOptions": {
                    "editMode": False
                }
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 3,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 6,
            "dims": [
                {
                    "name": "Historic Time",
                    "field": "historic_time.cdm_hist_gdp_temperature",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "GDP and Temperature",
                    "field": "gdp_and_temperature.cdm_hist_gdp_temperature",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 4,
            "width": 5,
            "height": 7,
            "itemId": "c5f4b4a2-07c0-46f5-be8f-90e48d877ed0",
            "nodeId": "cdm_hist_population",
            "columns": [
                {
                    "name": "Historic Time",
                    "field": "historic_time.cdm_hist_population",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "complexchart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Population",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "alignMax": 119613.276,
                "alignMin": 16.3,
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "nodesArray": [
                    {
                        "dims": [],
                        "rows": [
                            {
                                "name": "GDP and Temperature",
                                "field": "gdp_and_temperature.cdm_hist_gdp_temperature",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            }
                        ],
                        "nodeId": "cdm_hist_gdp_temperature",
                        "columns": [
                            {
                                "name": "Historic Time",
                                "field": "historic_time.cdm_hist_gdp_temperature",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            }
                        ],
                        "newDims": [
                            {
                                "name": "GDP and Temperature",
                                "field": "gdp_and_temperature.cdm_hist_gdp_temperature",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            },
                            {
                                "name": "Historic Time",
                                "field": "historic_time.cdm_hist_gdp_temperature",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            }
                        ],
                        "lineStyle": "",
                        "nodeIndex": 0,
                        "itemSubType": "line",
                        "itemProperties": {
                            "axes": {
                                "xAxis": {
                                    "max": None,
                                    "min": None,
                                    "title": {
                                        "text": ""
                                    },
                                    "labels": {
                                        "align": None,
                                        "style": {
                                            "fontSize": "11px"
                                        },
                                        "enabled": True,
                                        "rotation": None
                                    },
                                    "isSumList": [],
                                    "showTitle": True
                                },
                                "yAxis": {
                                    "max": None,
                                    "min": None,
                                    "index": 0,
                                    "title": {
                                        "text": "",
                                        "style": {
                                            "color": "#7cb5ec"
                                        }
                                    },
                                    "labels": {
                                        "style": {
                                            "color": "#7cb5ec"
                                        },
                                        "enabled": True,
                                        "rotation": None
                                    },
                                    "opposite": True,
                                    "showTitle": True
                                },
                                "enabled": False
                            },
                            "zoom": True,
                            "table": {
                                "styles": [
                                    {
                                        "pos": 0,
                                        "index": "_alltable_",
                                        "style": {
                                            "pagination": 100
                                        },
                                        "value": -1
                                    }
                                ]
                            },
                            "title": {
                                "text": "GDP and Temperature",
                                "align": "center",
                                "style": {
                                    "color": "#000000"
                                },
                                "margin": "",
                                "enabled": True,
                                "isCustom": False,
                                "verticalAlign": "top"
                            },
                            "detail": True,
                            "legend": {
                                "y": 0,
                                "align": "center",
                                "title": {
                                    "text": ""
                                },
                                "layout": "horizontal",
                                "margin": 2,
                                "enabled": True,
                                "borderWidth": 0,
                                "verticalAlign": "bottom"
                            },
                            "tooltip": {
                                "valueSuffix": None,
                                "valueDecimals": 2
                            },
                            "subtitle": {
                                "text": "",
                                "style": {
                                    "color": "#000000",
                                    "fontWeight": "normal"
                                },
                                "enabled": True,
                                "verticalAlign": "top"
                            },
                            "drilldown": True,
                            "timeChart": {
                                "active": False,
                                "possible": False
                            },
                            "colorSerie": "15",
                            "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
                        }
                    },
                    {
                        "dims": [],
                        "rows": [],
                        "nodeId": "cdm_hist_population",
                        "columns": [
                            {
                                "name": "Historic Time",
                                "field": "historic_time.cdm_hist_population",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            }
                        ],
                        "newDims": [
                            {
                                "name": "Historic Time",
                                "field": "historic_time.cdm_hist_population",
                                "isGeo": False,
                                "isTime": False,
                                "levels": [],
                                "values": [],
                                "description": None,
                                "currentLevel": None,
                                "numberFormat": None
                            }
                        ],
                        "nodeName": "Population",
                        "lineStyle": "",
                        "nodeIndex": 1,
                        "itemSubType": "line",
                        "itemProperties": {
                            "axes": {
                                "yAxis": {
                                    "max": None,
                                    "min": None,
                                    "index": 1,
                                    "title": {
                                        "text": "",
                                        "style": {
                                            "color": "#f7a35c"
                                        }
                                    },
                                    "labels": {
                                        "style": {
                                            "color": "#f7a35c"
                                        },
                                        "enabled": True,
                                        "rotation": 0
                                    },
                                    "showTitle": True
                                }
                            },
                            "title": {
                                "text": "Population"
                            },
                            "colorSerie": "15",
                            "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
                        }
                    }
                ]
            }
        },
        {
            "x": 6,
            "y": 6,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_normalized_independent_vars",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 5,
            "width": 6,
            "height": 7,
            "itemId": "b4a8217f-a121-4038-94c0-74b4d3030108",
            "nodeId": "cdm_normalized_independent_vars",
            "columns": [
                {
                    "name": "Historic Time",
                    "field": "historic_time.cdm_normalized_independent_vars",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": "1",
                        "min": "0",
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": True
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Normalized Independent Variables",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "15",
                "emptyTotal": False
            }
        }
    ]
}

linear_regression_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_ind_variables_sel",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "724df6a7-cb1e-463d-b051-d867d3bc3173",
            "nodeId": "cdm_ind_variables_sel",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "cellType": "choice",
                                "pagination": 100,
                                "columnWidth": 48,
                                "autoColumnWidth": False,
                                "choiceProperties": {
                                    "index": "yes_no",
                                    "includeAll": False
                                }
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Independent Variables Selection",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "defMode": False,
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "cubeOptions": {
                    "editMode": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_linear_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_linear_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression and Confidence Levels",
                    "field": "regression_and_confid_levels.cdm_ols_linear_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 11,
            "height": 5,
            "itemId": "6aa7bac9-dade-4750-9274-885604fa6f4e",
            "nodeId": "cdm_ols_linear_reg_model_confid_bands_an",
            "columns": [
                {
                    "name": "Historic & Projected Time",
                    "field": "historic_projected_time.cdm_ols_linear_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Linear Regression Model Confidence Bands Analysis",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "16",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 5,
            "dims": [],
            "rows": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_linear_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 3,
            "width": 6,
            "height": 8,
            "itemId": "13ab474b-f34d-40c4-904f-9412e5173806",
            "nodeId": "cdm_ols_linear_reg_model_adj_rsqr",
            "columns": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_linear_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "conditional": [
                                    {
                                        "to": "0.5",
                                        "pos": "0",
                                        "from": "0",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#e6b8af"
                                    },
                                    {
                                        "to": "0.95",
                                        "pos": 1,
                                        "from": "0.8501",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff2cc"
                                    },
                                    {
                                        "to": "1",
                                        "pos": 2,
                                        "from": "0.95001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#d9ead3"
                                    },
                                    {
                                        "to": "-0.0001",
                                        "pos": 3,
                                        "from": "-1",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#ffffff"
                                    },
                                    {
                                        "to": "0.85",
                                        "pos": 4,
                                        "from": "0.5",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#f7d5b2"
                                    },
                                    {
                                        "to": "1000",
                                        "pos": 5,
                                        "from": "1.0001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    }
                                ],
                                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Linear Regression Model Adjusted R-Squared",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "indexEvents": {
                    "sales_channels.cdm_ols_linear_reg_model_adj_rsqr": True,
                    "product_families.cdm_ols_linear_reg_model_adj_rsqr": True
                },
                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
            }
        },
        {
            "x": 7,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 2,
            "height": 1,
            "itemId": "17efc6e3-23cc-4a98-8e02-d8335b653cb5",
            "nodeId": "cdm_choice_product_family",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 9,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 5,
            "width": 3,
            "height": 1,
            "itemId": "114b0bb8-bf43-4c54-9e00-31030b79f59c",
            "nodeId": "cdm_choice_sales_channel",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Sales Channel",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 7,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 5,
            "height": 7,
            "itemId": "52c8e6bd-1d99-4898-b200-497d440eeede",
            "nodeId": "cdm_ols_linear_reg_summary",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "OLS Linear Regression Summary",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "indicator": {
                    "fontBold": False,
                    "fontSize": 13,
                    "fontColor": "#000",
                    "fontItalic": False,
                    "numberFormat": ",.",
                    "styleLibrary": "",
                    "decimalPlaces": 2,
                    "fontUnderline": False
                },
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

quadratic_regression_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_ind_variables_sel",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "724df6a7-cb1e-463d-b051-d867d3bc3173",
            "nodeId": "cdm_ind_variables_sel",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "cellType": "choice",
                                "pagination": 100,
                                "columnWidth": 48,
                                "autoColumnWidth": False,
                                "choiceProperties": {
                                    "index": "yes_no",
                                    "includeAll": False
                                }
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Independent Variables Selection",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "defMode": False,
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "cubeOptions": {
                    "editMode": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_quad_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_quad_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression and Confidence Levels",
                    "field": "regression_and_confid_levels.cdm_ols_quad_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 11,
            "height": 5,
            "itemId": "8c5ab7ae-bfbb-42d3-94ab-7bcff61aa5d1",
            "nodeId": "cdm_ols_quad_reg_model_confid_bands_an",
            "columns": [
                {
                    "name": "Historic & Projected Time",
                    "field": "historic_projected_time.cdm_ols_quad_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Quadratic Reg Model Confidence Bands Analysis",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "16",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 5,
            "dims": [],
            "rows": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_quad_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 3,
            "width": 6,
            "height": 8,
            "itemId": "5c0edcbb-76ed-49a5-83d1-4230e4ef9fba",
            "nodeId": "cdm_ols_quad_reg_model_adj_rsqr",
            "columns": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_quad_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "conditional": [
                                    {
                                        "to": "0.5",
                                        "pos": 0,
                                        "from": "0",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#e6b8af"
                                    },
                                    {
                                        "to": "0.95",
                                        "pos": 1,
                                        "from": "0.8501",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff2cc"
                                    },
                                    {
                                        "to": "1",
                                        "pos": 2,
                                        "from": "0.95001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#d9ead3"
                                    },
                                    {
                                        "to": "-0.0001",
                                        "pos": 3,
                                        "from": "-1",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    },
                                    {
                                        "to": "0.85",
                                        "pos": 4,
                                        "from": "0.5001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#f7d5b2"
                                    },
                                    {
                                        "to": "1000",
                                        "pos": 5,
                                        "from": "1.0001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    }
                                ],
                                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Quadratic Regression Model Adjusted R-Squared",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "indexEvents": {
                    "sales_channels.cdm_ols_quad_reg_model_adj_rsqr": True,
                    "product_families.cdm_ols_quad_reg_model_adj_rsqr": True
                },
                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
            }
        },
        {
            "x": 7,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 2,
            "height": 1,
            "itemId": "17efc6e3-23cc-4a98-8e02-d8335b653cb5",
            "nodeId": "cdm_choice_product_family",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 9,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 5,
            "width": 3,
            "height": 1,
            "itemId": "114b0bb8-bf43-4c54-9e00-31030b79f59c",
            "nodeId": "cdm_choice_sales_channel",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Sales Channel",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 7,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 5,
            "height": 7,
            "itemId": "b7331a07-77ef-4cab-b654-e6b757df09c4",
            "nodeId": "cdm_ols_quad_reg_summary",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "OLS Quadratic Regression Summary",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

cubic_regression_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_ind_variables_sel",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "724df6a7-cb1e-463d-b051-d867d3bc3173",
            "nodeId": "cdm_ind_variables_sel",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "cellType": "choice",
                                "pagination": 100,
                                "columnWidth": 48,
                                "autoColumnWidth": False,
                                "choiceProperties": {
                                    "index": "yes_no",
                                    "includeAll": False
                                }
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Independent Variables Selection",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "defMode": False,
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "cubeOptions": {
                    "editMode": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_cubic_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_cubic_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression and Confidence Levels",
                    "field": "regression_and_confid_levels.cdm_ols_cubic_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 11,
            "height": 5,
            "itemId": "6358c710-f85e-4db5-86c7-d444af91abb6",
            "nodeId": "cdm_ols_cubic_reg_model_confid_bands_an",
            "columns": [
                {
                    "name": "Historic & Projected Time",
                    "field": "historic_projected_time.cdm_ols_cubic_reg_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Cubic Reg Model Confidence Bands Analysis",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "16",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 5,
            "dims": [],
            "rows": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_ols_cubic_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 3,
            "width": 6,
            "height": 8,
            "itemId": "155ca38b-854f-45b1-a6e3-bef5ac7ad711",
            "nodeId": "cdm_ols_cubic_reg_model_adj_rsqr",
            "columns": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_ols_cubic_reg_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "conditional": [
                                    {
                                        "to": "0.5",
                                        "pos": 0,
                                        "from": "0",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#e6b8af"
                                    },
                                    {
                                        "to": "0.95",
                                        "pos": 1,
                                        "from": "0.8501",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff2cc"
                                    },
                                    {
                                        "to": "1",
                                        "pos": 2,
                                        "from": "0.95001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#d9ead3"
                                    },
                                    {
                                        "to": "-0.0001",
                                        "pos": 3,
                                        "from": "-1",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    },
                                    {
                                        "to": "0.85",
                                        "pos": 4,
                                        "from": "0.5001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#f7d5b2"
                                    },
                                    {
                                        "to": "1000",
                                        "pos": 5,
                                        "from": "1.0001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    }
                                ],
                                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "OLS Cubic Regression Model Adjusted R-Squared",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "indexEvents": {
                    "sales_channels.cdm_ols_cubic_reg_model_adj_rsqr": True,
                    "product_families.cdm_ols_cubic_reg_model_adj_rsqr": True
                },
                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
            }
        },
        {
            "x": 7,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 2,
            "height": 1,
            "itemId": "17efc6e3-23cc-4a98-8e02-d8335b653cb5",
            "nodeId": "cdm_choice_product_family",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 9,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 5,
            "width": 3,
            "height": 1,
            "itemId": "114b0bb8-bf43-4c54-9e00-31030b79f59c",
            "nodeId": "cdm_choice_sales_channel",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Sales Channel",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 7,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 5,
            "height": 7,
            "itemId": "e2af3f5a-cefb-4151-a22a-b84578b94487",
            "nodeId": "cdm_ols_cubic_reg_summary",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "OLS Cubic Regression Summary",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

arima_regression_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_ind_variables_sel",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "724df6a7-cb1e-463d-b051-d867d3bc3173",
            "nodeId": "cdm_ind_variables_sel",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "cellType": "choice",
                                "pagination": 100,
                                "columnWidth": 48,
                                "autoColumnWidth": False,
                                "choiceProperties": {
                                    "index": "yes_no",
                                    "includeAll": False
                                }
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Independent Variables Selection",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "defMode": False,
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "cubeOptions": {
                    "editMode": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_arima_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_arima_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression and Confidence Levels",
                    "field": "regression_and_confid_levels.cdm_arima_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 11,
            "height": 5,
            "itemId": "1e7ca668-179f-43f9-a2ee-a82052e43bc8",
            "nodeId": "cdm_arima_model_confid_bands_an",
            "columns": [
                {
                    "name": "Historic & Projected Time",
                    "field": "historic_projected_time.cdm_arima_model_confid_bands_an",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "ARIMA Model Confidence Bands Analysis",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "16",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 5,
            "dims": [],
            "rows": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_arima_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 3,
            "width": 6,
            "height": 8,
            "itemId": "039bfa1a-f7f1-4bf0-a023-11e835adbf81",
            "nodeId": "cdm_arima_model_adj_rsqr",
            "columns": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_arima_model_adj_rsqr",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "conditional": [
                                    {
                                        "to": "0.5",
                                        "pos": 0,
                                        "from": "0",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#e6b8af"
                                    },
                                    {
                                        "to": "0.95",
                                        "pos": 1,
                                        "from": "0.8501",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff2cc"
                                    },
                                    {
                                        "to": "1",
                                        "pos": 2,
                                        "from": "0.95001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#d9ead3"
                                    },
                                    {
                                        "to": "-0.0001",
                                        "pos": 3,
                                        "from": "-1",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    },
                                    {
                                        "to": "0.85",
                                        "pos": 4,
                                        "from": "0.5001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#000",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#f7d5b2"
                                    },
                                    {
                                        "to": "1000",
                                        "pos": 5,
                                        "from": "1.0001",
                                        "shape": "none",
                                        "fontBold": False,
                                        "fontSize": "11",
                                        "fontColor": "#ffffff",
                                        "fontItalic": False,
                                        "fontUnderline": False,
                                        "shapePosition": "right",
                                        "backgroundColor": "#fff"
                                    }
                                ],
                                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "ARIMA Model Adjusted R-Squared",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "indexEvents": {
                    "sales_channels.cdm_arima_model_adj_rsqr": True,
                    "product_families.cdm_arima_model_adj_rsqr": True
                },
                "numberFormat": "2,F,4,3,0,0,4,1,$,5,,0"
            }
        },
        {
            "x": 7,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 2,
            "height": 1,
            "itemId": "17efc6e3-23cc-4a98-8e02-d8335b653cb5",
            "nodeId": "cdm_choice_product_family",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Product Family",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 9,
            "y": 5,
            "dims": [],
            "rows": [],
            "index": 5,
            "width": 3,
            "height": 1,
            "itemId": "114b0bb8-bf43-4c54-9e00-31030b79f59c",
            "nodeId": "cdm_choice_sales_channel",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "Sales Channel",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": False,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 6,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": False
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 7,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 7,
            "width": 5,
            "height": 7,
            "itemId": "ff1abf5b-f437-4797-bfa7-6bfcbf5b989b",
            "nodeId": "cdm_arima_summary",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "title": {
                    "text": "ARIMA Summary",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

models_comparison_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [
                {
                    "name": "Independent Variables",
                    "field": "independent_variables.cdm_ind_variables_sel",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 0,
            "width": 1,
            "height": 3,
            "itemId": "724df6a7-cb1e-463d-b051-d867d3bc3173",
            "nodeId": "cdm_ind_variables_sel",
            "columns": [],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "cellType": "choice",
                                "pagination": 100,
                                "columnWidth": 48,
                                "autoColumnWidth": False,
                                "choiceProperties": {
                                    "index": "yes_no",
                                    "includeAll": False
                                }
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Independent Variables Selection",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "defMode": False,
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "cubeOptions": {
                    "editMode": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 0,
            "dims": [
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_models_prediction_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Sales Channel 4",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_models_prediction_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Product Family 17",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression Models + Observed Data",
                    "field": "regression_models_observed_data.cdm_models_prediction_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 1,
            "width": 11,
            "height": 10,
            "itemId": "be6d4e12-35e9-4d19-89a0-2fbd0227ca18",
            "nodeId": "cdm_models_prediction_comp",
            "columns": [
                {
                    "name": "Historic & Projected Time",
                    "field": "historic_projected_time.cdm_models_prediction_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "linechart",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": False
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "style": {
                                "fontSize": "11px"
                            },
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Models Predictions Comparison",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "labels": {
                    "inside": False,
                    "enabled": False
                },
                "legend": {
                    "y": 0,
                    "align": "center",
                    "title": {
                        "text": ""
                    },
                    "layout": "horizontal",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "bottom"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "colorSerie": "17",
                "numberFormat": "2,I,4,,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 0,
            "y": 3,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 1,
            "height": 3,
            "itemId": "bad29a65-ce06-40b7-ad95-b810598ac043",
            "nodeId": "sales_channels",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": True,
                    "currentSelectedValues": [
                        "Sales Channel 4"
                    ]
                },
                "title": {
                    "text": "Sales Channels",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "sales_channels",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 0,
            "y": 6,
            "dims": [],
            "rows": [],
            "index": 3,
            "width": 1,
            "height": 7,
            "itemId": "42a4f078-dec4-432c-8076-ba6e182a78f2",
            "nodeId": "product_families",
            "columns": [],
            "itemType": "indexlist",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "index": {
                    "ui": "default",
                    "dynamic": False,
                    "related": False,
                    "orientation": "v",
                    "singleSelect": True,
                    "currentSelectedValues": [
                        "Product Family 17"
                    ]
                },
                "title": {
                    "text": "Product Families",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "nodeId": "product_families",
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "generalBackgroundColor": "#e5e5e5"
            }
        },
        {
            "x": 1,
            "y": 10,
            "dims": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_models_reg_results_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Product Family 17",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_models_reg_results_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Sales Channel 4",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression Models",
                    "field": "regression_models.cdm_models_reg_results_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 4,
            "width": 7,
            "height": 3,
            "itemId": "49f48f46-9589-4e19-818a-cb16aa3d432d",
            "nodeId": "cdm_models_reg_results_comp",
            "columns": [
                {
                    "name": "Regression Results",
                    "field": "regression_results.cdm_models_reg_results_comp",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "numberFormat": "2,F,4,2,1,0,4,0,$,5,,0",
                                "backgroundColor": "#fff2cc"
                            },
                            "value": -1
                        },
                        {
                            "pos": 1,
                            "index": "regression_results.cdm_models_reg_results_comp",
                            "style": {
                                "numberFormat": "2,F,4,3,1,0,4,0,$,5,,0"
                            },
                            "value": "R-Squared"
                        },
                        {
                            "pos": 2,
                            "index": "regression_results.cdm_models_reg_results_comp",
                            "style": {
                                "numberFormat": "2,F,4,3,1,0,4,0,$,5,,0"
                            },
                            "value": "Adjusted R-Squared"
                        }
                    ]
                },
                "title": {
                    "text": "Models Regression Results Comparison",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "numberFormat": "2,F,4,2,1,0,4,0,$,5,,0"
            }
        },
        {
            "x": 8,
            "y": 10,
            "dims": [
                {
                    "name": "Product Families",
                    "field": "product_families.cdm_models_reg_results_best_fit_value",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Product Family 17",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                },
                {
                    "name": "Sales Channels",
                    "field": "sales_channels.cdm_models_reg_results_best_fit_value",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [
                        {
                            "type": None,
                            "value": "Sales Channel 4",
                            "geoDef": None,
                            "selected": True
                        }
                    ],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "rows": [
                {
                    "name": "Regression Results",
                    "field": "regression_results.cdm_models_reg_results_best_fit_value",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "index": 5,
            "width": 4,
            "height": 3,
            "itemId": "dfadbf63-4dbe-487e-8ab8-afdc4596322a",
            "nodeId": "cdm_models_reg_results_best_fit_value",
            "columns": [
                {
                    "name": "Regression Comparison Concepts",
                    "field": "regression_comparison_concepts.cdm_models_reg_results_best_fit_value",
                    "isGeo": False,
                    "isTime": False,
                    "levels": [],
                    "values": [],
                    "description": None,
                    "currentLevel": None,
                    "numberFormat": None
                }
            ],
            "itemType": "table",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": True,
                            "rotation": None
                        },
                        "showTitle": True
                    },
                    "enabled": False
                },
                "zoom": True,
                "table": {
                    "styles": [
                        {
                            "pos": 0,
                            "index": "_alltable_",
                            "style": {
                                "pagination": 100,
                                "backgroundColor": "#fff2cc"
                            },
                            "value": -1
                        }
                    ]
                },
                "title": {
                    "text": "Models Regression Results - Best Fit Value",
                    "align": "center",
                    "style": {
                        "color": "#000000"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "margin": 2,
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "color": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": False,
                "timeChart": {
                    "active": False,
                    "possible": False
                }
            }
        }
    ]
}

gapminder_data_analysis_definition = {
    "definitionLarge": [
        {
            "x": 0,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 0,
            "width": 4,
            "height": 1,
            "itemId": "4963e4bb-f2ea-4f59-b38a-4a4582d4b755",
            "nodeId": "",
            "columns": [],
            "itemType": "objectItem",
            "objectType": "texteditor",
            "itemProperties": {
                "htmlcontent": "<span class=\"\" style=\"font-size: 2vmin;\"><font color=\"#005f7f\">Gapminder Dataset Analysis</font></span>",
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 4,
            "y": 0,
            "dims": [],
            "rows": [],
            "index": 1,
            "width": 8,
            "height": 1,
            "itemId": "5f8f06b6-80dd-4ce4-bf20-06604c68bd3a",
            "nodeId": "continent_selector",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Continent Selector",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "color": "#4572a7",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None,
                "multiselect": "0",
                "selectorFormat": "options",
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 0,
            "y": 1,
            "dims": [],
            "rows": [],
            "index": 2,
            "width": 2,
            "height": 1,
            "itemId": "19d1ce4b-3a7e-4eb3-affb-512b23e2e8f1",
            "nodeId": "country__one_vs_all",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Country: One / All",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None,
                "selectorFormat": "options",
                "generalBackgroundColor": "#d9d9d9"
            }
        },
        {
            "x": 2,
            "y": 1,
            "dims": [],
            "rows": [],
            "index": 3,
            "width": 10,
            "height": 13,
            "itemId": "b7b71112-d0f5-4260-9801-1b829dfdd850",
            "nodeId": "exploratory_analysis1",
            "columns": [],
            "itemType": "indicator",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Graph Exploratory Analysis",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": False,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None
            }
        },
        {
            "x": 0,
            "y": 2,
            "dims": [],
            "rows": [],
            "index": 4,
            "width": 2,
            "height": 12,
            "itemId": "3b28d2df-9d6e-4474-b796-d21813094352",
            "nodeId": "country_selector",
            "columns": [],
            "itemType": "selector",
            "objectType": None,
            "itemProperties": {
                "axes": {
                    "xAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "yAxis": {
                        "max": None,
                        "min": None,
                        "title": {
                            "text": ""
                        },
                        "labels": {
                            "align": None,
                            "enabled": "True",
                            "rotation": None
                        },
                        "isSumList": [],
                        "showTitle": True
                    },
                    "enabled": True
                },
                "unit": "",
                "zoom": True,
                "title": {
                    "text": "Single Country Selector",
                    "align": "center",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "margin": "",
                    "enabled": True,
                    "isCustom": False,
                    "verticalAlign": "top"
                },
                "detail": True,
                "legend": {
                    "y": 0,
                    "align": "right",
                    "title": {
                        "text": ""
                    },
                    "layout": "vertical",
                    "enabled": True,
                    "borderWidth": 0,
                    "verticalAlign": "middle"
                },
                "tooltip": {
                    "valueSuffix": None,
                    "valueDecimals": 2
                },
                "subtitle": {
                    "text": "",
                    "style": {
                        "text": "#000000",
                        "fontWeight": "normal"
                    },
                    "enabled": True,
                    "verticalAlign": "top"
                },
                "drilldown": True,
                "timeChart": {
                    "active": False,
                    "possible": False
                },
                "originalId": None,
                "selectorFormat": "options",
                "selectorOrientation": "v",
                "generalBackgroundColor": "#d9d9d9"
            }
        }
    ]
}


def add_demo_dashboards(apps, schema_editor):
    Report = apps.get_model('pyplan', 'Report')
    Dashboard = apps.get_model('pyplan', 'Dashboard')

    Dashboard.objects.create(
        model='xarray_in_pyplan',
        name='Xarray in Pyplan',
        node=None,
        order=1,
        owner_id=1,
        definition=xarray_in_pyplan_definition,
    )

    Dashboard.objects.create(
        model='pyplan_qs_tutorials',
        name="Federer's Statistics Analysis",
        node=None,
        order=1,
        owner_id=1,
        definition=pyplan_qs_tutorials_definition,
    )

    Dashboard.objects.create(
        model='creating_my_first_model',
        name='Interface 1',
        node=None,
        order=1,
        owner_id=1,
        definition=creating_my_first_model_definition,
    )

    Dashboard.objects.create(
        model='iris_sample_model',
        name='Iris Sample',
        node=None,
        order=1,
        owner_id=1,
        definition=iris_sample_model_definition,
    )

    report = Report.objects.create(
        model='ex_regressions',
        name='Regressions',
        parent_id=None,
        owner_id=1,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='Variables Exploration',
        node=None,
        order=1,
        owner_id=1,
        definition=variable_exploration_definition,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='Linear Regression',
        node=None,
        order=2,
        owner_id=1,
        definition=linear_regression_definition,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='Quadratic Regression',
        node=None,
        order=3,
        owner_id=1,
        definition=quadratic_regression_definition,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='Cubic Regression',
        node=None,
        order=4,
        owner_id=1,
        definition=cubic_regression_definition,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='ARIMA Regression',
        node=None,
        order=5,
        owner_id=1,
        definition=arima_regression_definition,
    )

    Dashboard.objects.create(
        report=report,
        model='ex_regressions',
        name='Models Comparison',
        node=None,
        order=6,
        owner_id=1,
        definition=models_comparison_definition,
    )

    Dashboard.objects.create(
        model='gapminder_data_analysis',
        name='Exploratory Analysis',
        node=None,
        order=1,
        owner_id=1,
        definition=gapminder_data_analysis_definition,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('pyplan', '0013_guestuser_permissions_20190919_1715'),
    ]

    operations = [
        migrations.RunPython(add_demo_dashboards),
    ]

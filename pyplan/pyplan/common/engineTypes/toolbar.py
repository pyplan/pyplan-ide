default_toolbar = [
    {
        "label": "Code",
        "active": True,
        "items": [
            {
                "label": "Node",
                "icon": "variable",
                "nodeClass": "variable",
                "active": True,
                "format": {
                    "color": "#4CBCFF",
                    "nodeClass": "variable",
                    "definition": "result = 0",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 1,
                        "showLabel": 1,
                        "showOutputs": 1,
                        "useNodeFont": 0
                    },
                    "w": 96,
                    "h": 48
                }
            },
            {
                "label": "Function",
                "icon": "function",
                "nodeClass": "function",
                "active": True,
                "format": {
                    "color": "#cb98ff",
                    "nodeClass": "function",
                    "definition": "def _fn(param1,param2):\n    return param1+param2\n\nresult = _fn",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 0,
                        "showLabel": 1,
                        "showOutputs": 0,
                        "useNodeFont": 0
                    },
                    "h": 40,
                    "w": 100
                }
            },
            {
                "label": "Decision",
                "icon": "decision",
                "nodeClass": "decision",
                "active": True,
                "format": {
                    "color": "#4cffa6",
                    "nodeClass": "decision",
                    "definition": "result = selector(['Item 1','Item 2','Item 3'],1,False)",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 1,
                        "showLabel": 1,
                        "showOutputs": 1,
                        "useNodeFont": 0
                    },
                    "h": 50,
                    "w": 100
                }
            },
            {
                "label": "Index",
                "icon": "index",
                "nodeClass": "pdindex",
                "active": True,
                "format": {
                    "color": "#9999ff",
                    "nodeClass": "index",
                    "definition": "result = pd.Index(['Item 1','Item 2','Item 3'])",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 0,
                        "showLabel": 1,
                        "showOutputs": 0,
                        "useNodeFont": 0
                    },
                    "w": 96,
                    "h": 48
                }
            },
            {
                "label": "Button",
                "icon": "button",
                "nodeClass": "button",
                "active": True,
                "format": {
                    "color": "#CBCBCB",
                    "nodeClass": "button",
                    "definition": "",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 0,
                        "showLabel": 1,
                        "showOutputs": 0,
                        "useNodeFont": 0
                    },
                    "h": 40,
                    "w": 154
                }
            },
            {
                "label": "Module",
                "icon": "module",
                "nodeClass": "module",
                "active": True,
                "format": {
                    "color": "#9FC5E8",
                    "nodeClass": "module",
                    "definition": "",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 1,
                        "showLabel": 1,
                        "showOutputs": 1,
                        "useNodeFont": 0
                    },
                    "h": 50,
                    "w": 100
                }
            },
            {
                "label": "Text",
                "icon": "text",
                "nodeClass": "text",
                "active": True,
                "format": {
                    "color": "#EEEEEE",
                    "nodeClass": "text",
                    "definition": "",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 0,
                        "showInputs": 0,
                        "showLabel": 1,
                        "showOutputs": 0,
                        "useNodeFont": 0
                    },
                    "h": 164,
                    "w": 376,
                    "z": -1
                }
            }
        ]
    },
    {
        "label": "Data sources",
        "active": True,
        "items": [
            {
                "label": "CSV",
                "icon": "variable",
                "nodeClass": "sourcecsv",
                "wizard": "sourcecsv",
                "active": True,
                "format": {
                    "color": "#d9ead3",
                    "nodeClass": "variable",
                    "definition": "result = 0",
                    "nodeInfo": {
                        "fill": 1,
                        "showBorder": 1,
                        "showInputs": 1,
                        "showLabel": 1,
                        "showOutputs": 1,
                        "useNodeFont": 0
                    },
                    "w": 96,
                    "h": 48
                }
            }
        ]
    }
]
